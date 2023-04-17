FROM python:3.10-slim-buster

COPY ./requirements.txt /root/servico-estoque/requirements.txt

WORKDIR /root/servico-estoque

RUN pip3 install -r requirements.txt 

EXPOSE 3002
CMD ["python3", "app.py"]