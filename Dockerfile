FROM python:3.7.9-slim

WORKDIR /PCI-Prototype-IoT
COPY . /PCI-Prototype-IoT

WORKDIR /PCI-Prototype-IoT/demos/yolov4-custom-functions

RUN pip install --upgrade pip && \ 
pip install -r requirements.txt