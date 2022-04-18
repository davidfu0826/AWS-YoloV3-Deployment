FROM python:3.8-slim-buster

WORKDIR /blabla

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#CMD [ "python3", "my_flask_app.py"]
#ENTRYPOINT [ "python3", "my_flask_app.py" ]
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app" ]

# https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html
# Containers need to implement a web server that responds to /invocations and /ping on port 8080.