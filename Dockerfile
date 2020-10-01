FROM ubuntu:latest


RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /flask_app/requirements.txt

WORKDIR /flask_app

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . /flask_app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]