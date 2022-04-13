import pickle
import numpy as np
from flask import Flask, request
from PIL import Image

from predict import run_prediction, read_detection_results

model = None
app = Flask(__name__)

def load_model():
    global model
    with open('iris_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route('/')
def home_endpoint():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        print(request.files)
        #data = request.get_json()  # Get data posted as a json
        #data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
        image=request.files['media']
        print(image)
        pil_image = Image.open(image)
        print(type(pil_image), pil_image)
        pil_image.save("data/input/image.jpg")

        run_prediction("data/input/image.jpg")
        response = read_detection_results("data/input/image.jpg", "output/results/labels/*.txt", "yolov3/data/coco128.yaml")
        #prediction = model.predict(data)  # runs globally loaded model on the data
    return str(response)

if __name__ == '__main__':
    #load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=81)