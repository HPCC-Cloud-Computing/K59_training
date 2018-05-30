FROM python:2.7
MAINTAINER lananh loglamo@gmail.com
RUN apt-get update
RUN mkdir /filterdata
RUN mkdir /config
ADD ./filterdata/filterdata.py /filterdata
ADD ./config/config.cfg /config
RUN apt-get install -y python python-pip
RUN pip install pika
WORKDIR /filterdata
VOLUME /config
CMD [ "python", "./filterdata.py"]