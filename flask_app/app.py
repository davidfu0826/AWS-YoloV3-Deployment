from flask import Flask, request, jsonify

# Process images
from PIL import Image
import json
import base64
from io import BytesIO
from pathlib import Path

import shutil
from predict import run_prediction, read_detection_results

server = Flask(__name__)

def decode_json_b64_img(json_data):
    dict_data = json.loads(json_data) #Convert json to dictionary
    img = dict_data["img"] #Take out base64# str
    img = base64.b64decode(img) #Convert image data converted to base64 to original binary data# bytes
    img = BytesIO(img) # _io.Converted to be handled by BytesIO pillow
    img = Image.open(img) 
    return img

def run_request():
    json_data = request.get_json() #Get the POSTed json
    
    img = decode_json_b64_img(json_data)
    img_shape = img.size #Appropriately process the acquired image

    Path("data/input/").mkdir(exist_ok=True, parents=True)
    img = img.save("data/input/image.jpg") # Save image to input path (for inference)
    
    run_prediction("data/input/image.jpg")
    response = read_detection_results("output/results/labels/*.txt")

    # Clean
    shutil.rmtree("output/results/")

    # Return the processing result to the client
    #response = {
    #    "img_shape":img_shape        
    #}

    return jsonify(response)


@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()