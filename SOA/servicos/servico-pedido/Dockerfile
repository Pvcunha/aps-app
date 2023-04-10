FROM python:3.10-slim-buster

COPY . /root/servico-conta

WORKDIR /root/servico-conta

RUN pip3 install -r requirements.txt 

EXPOSE 3001
CMD ["python3", "app.py"]