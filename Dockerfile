FROM python:3.7.9

WORKDIR /PCI-Prototype-IoT
COPY . /PCI-Prototype-IoT

WORKDIR /PCI-Prototype-IoT/demos/tensorflow_object_counting_api_v2

RUN pip install -r requirements.txt