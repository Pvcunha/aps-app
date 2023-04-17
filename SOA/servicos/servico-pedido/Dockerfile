FROM python:3.10-slim-buster

COPY ./requirements.txt /root/servico-pedido/requirements.txt

WORKDIR /root/servico-pedido

RUN pip3 install -r requirements.txt 

EXPOSE 3001
CMD ["python3", "app.py"]