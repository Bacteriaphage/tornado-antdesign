FROM ubuntu:latest
WORKDIR /app
COPY . /app
# update apt-get
RUN echo "===update apt-get ===" && apt-get update
# install python3 and default interactive behavior is 'yes'
RUN echo "===install python and pip===" && apt-get install -y python3 && apt-get install -y python3-pip
# install required python package
RUN echo "===install python package===" && pip3 install --trusted-host pypi.python.org -r requirements.txt
# export 80 port
EXPOSE 80
#CMD ["python3", "app.py"]
