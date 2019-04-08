FROM ubuntu:latest AS base
WORKDIR /app
# copy files into container
COPY . /app
# update apt-get
RUN echo "===update apt-get ===" && apt-get update
# install python3 and default interactive behavior is 'yes'
RUN echo "===install python and pip===" && apt-get install -y python3 && apt-get install -y python3-pip
# install required python package
RUN echo "===install python package===" && pip3 install --trusted-host pypi.python.org -r requirements.txt
# install editor
RUN apt-get install -y vim
# export 8000 port
EXPOSE 8000

FROM base AS app
#run app
CMD ["python3", "./server/app.py"]
