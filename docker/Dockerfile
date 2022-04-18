FROM python:3.8-slim-buster

RUN apt-get -y update && apt-get install -y --no-install-recommends nginx

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY . /opt/program
WORKDIR /opt/program

#CMD [ "python3", "my_flask_app.py"]
#ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app" ]
CMD [ "serve" ]

# https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html
# Containers need to implement a web server that responds to /invocations and /ping on port 8080.