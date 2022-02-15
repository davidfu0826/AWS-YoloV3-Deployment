**Background**

Yolov3 model:
https://github.com/ultralytics/yolov3/tree/0f80f2f9054dd06d34c51e73ea1bc5ba808fed18

Guide for web server: 
https://towardsdatascience.com/how-to-deploy-ml-models-using-flask-gunicorn-nginx-docker-9b32055b3d0


**Prerequisites:**

Docker installed

**Usage:**

Start server:
```
>> git clone https://github.com/davidfu0826/AWS-YoloV3-Deployment.git
>> cd AWS-YoloV3-Deployment
>> ./run_docker.sh
```

Run image client:
```
>> cd client
>> python image_client.py
```
