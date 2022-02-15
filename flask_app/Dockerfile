FROM python:3.6.7

WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install torch==1.10.2+cpu torchvision==0.11.3+cpu torchaudio==0.10.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

RUN git clone https://github.com/ultralytics/yolov3.git
WORKDIR yolov3
RUN git checkout 0f80f2f9054dd06d34c51e73ea1bc5ba808fed18
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pyyaml
WORKDIR /usr/src/flask_app
COPY . .
RUN python predict.py