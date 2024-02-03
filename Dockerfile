FROM python:3.10.11
WORKDIR /HID-Project-DevOps
COPY requirements.txt /HID-Project-DevOps/
RUN pip install -r requirements.txt
COPY . /HID-Project-DevOps/
