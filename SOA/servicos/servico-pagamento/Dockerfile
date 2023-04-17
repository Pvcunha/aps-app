FROM python:3.10-slim-buster

COPY ./requirements.txt /root/servico-pagamento/requirements.txt

WORKDIR /root/servico-pagamento

RUN pip3 install -r requirements.txt 

EXPOSE 3003
CMD ["python3", "app.py"]