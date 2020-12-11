FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /project

WORKDIR /project

COPY requirements.txt /project/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /project/

ENV PYTHONPATH "${PYTONPATH}:/project/app"

EXPOSE 8000