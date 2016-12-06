FROM ubuntu:14.04
MAINTAINER ZZC

RUN apt-get update
RUN sudo apt-get install python-pip
RUN wget https://pypi.python.org/packages/source/s/selenium/selenium-2.35.0.tar.gz
RUN tar xvf selenium-2.35.0
RUN mv selenium-2.35.0 /usr/local/lib/python2.7/dist-packages
RUN cd /usr/local/lib/python2.7/dist-packages/selenium-2.35.0
RUN python setup.py install
