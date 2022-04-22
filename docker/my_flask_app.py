from genericpath import exists
import string
import random
from pathlib import Path
import pickle
import numpy as np
from flask import Flask, request
from PIL import Image

from predict import run_prediction, read_detection_results

model = None
app = Flask(__name__)

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

@app.route('/')
def home_endpoint():
    return 'Hello World!'

@app.route('/ping')
def ping_response():
    return 'Ping back to you!'

@app.route('/invocations', methods=['POST'])
def get_prediction():

    if request.method == 'POST':
        print(request.files)
        #data = request.get_json()  # Get data posted as a json
        #data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
        image=request.files['image']
        print(image)
        Path("data/input/").mkdir(exist_ok=True, parents=True)
        pil_image = Image.open(image)
        print(type(pil_image), pil_image)

        filename = random_string(20)
        pil_image.save(f"data/input/{filename}.jpg")

        run_prediction(f"data/input/{filename}.jpg")
        response = read_detection_results(f"data/input/{filename}.jpg", f"data/output/{filename}/labels/*.txt", "yolov3/data/coco128.yaml")
    return str(response)


#if __name__ == '__main__':
#    #load_model()  # load model at the beginning once only
#    app.run(host='0.0.0.0', port=8080)
    