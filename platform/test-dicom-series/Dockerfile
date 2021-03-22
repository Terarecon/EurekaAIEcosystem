FROM python:3.7-slim

COPY ./ /opt
WORKDIR /opt

RUN apt-get update -y \
&& apt-get install -y gcc \
&& pip install --no-cache-dir pydicom==1.3.0 numpy Pillow  netifaces requests

CMD python /opt/main.py /eureka

LABEL com.eurekaai.metadata-version=3
