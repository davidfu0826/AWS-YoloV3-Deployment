import pickle
import numpy as np
from flask import Flask, request
from PIL import Image

from pathlib import Path
import string
import random


from predict import run_prediction, read_detection_results

model = None
app = Flask(__name__)
Path("data/input/").mkdir(exist_ok=True, parents=True)

def random_filename(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

@app.route('/')
def home_endpoint():
    return 'Hello World!'

@app.route('/ping')
def ping_response():
    return 'Ping back to you!'

@app.route('/invocations', methods=['POST'])
def get_prediction():

    if request.method == 'POST':
        print(request.files.keys())
        image=request.files['image']
        pil_image = Image.open(image)
        img_name = random_filename(length=1)
        pil_image.save(f"data/input/{img_name}.jpg")

        # Run inference
        run_prediction(f"data/input/{img_name}.jpg", output_dir=img_name) 

        # Parse model output to json/dictionary
        response = read_detection_results(f"data/input/{img_name}.jpg", f"output/results/{img_name}/labels/*.txt", "yolov3/data/coco128.yaml")

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    