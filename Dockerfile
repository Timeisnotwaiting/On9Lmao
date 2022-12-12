FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

CMD ["python3", "yashu.py"]
