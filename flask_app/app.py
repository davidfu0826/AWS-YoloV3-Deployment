from flask import Flask, request, jsonify

# Process images
from PIL import Image
#import json
#import base64
#from io import BytesIO


server = Flask(__name__)

#@server.route('/')
#def hello_world():
#    return 'Hello world!'
    
def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    return list[index]

    """
    json_data = request.get_json() #Get the POSTed json
    dict_data = json.loads(json_data) #Convert json to dictionary

    img = dict_data["img"] #Take out base64# str
    img = base64.b64decode(img) #Convert image data converted to base64 to original binary data# bytes
    img = BytesIO(img) # _io.Converted to be handled by BytesIO pillow
    img = Image.open(img) 
    img_shape = img.size #Appropriately process the acquired image

    #Return the processing result to the client
    response = {
        "img_shape":img_shape        
    }

    return jsonify(response)
    """

@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()