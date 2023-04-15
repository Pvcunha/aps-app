FROM python:3.10-slim-buster

COPY ./requirements.txt /root/servico-conta/requirements.txt

WORKDIR /root/servico-conta

RUN pip3 install -r requirements.txt 

EXPOSE 3000
CMD ["python3", "app.py"]