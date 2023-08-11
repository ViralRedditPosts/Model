# Intended to be run from the top-level package directory
# This package is meant to be an all purpose container of this project.
# You should be able to develop, test, debug, and use it as a base layer for other layers.
# 
# docker build -t predict-etl-base:latest -f ./model/Dockerfile .
# docker run [-idt] --name predict-etl-base --rm predict-etl-base:latest
# test locally with:
#    docker run -it --name predict-etl-base \
#      -e AWS_ACCESS_KEY_ID=[access key] \
#      -e AWS_SECRET_ACCESS_KEY=[secret key] \
#      --rm predict-etl-base:latest

FROM --platform=linux/amd64 bitnami/spark:3.3.0-debian-11-r44 AS pyspark-build

USER root

RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install vim

COPY . ./app

# install the package requirements
# the -e in case you want use container to develop locally (necessary on Apple silicon Macs)
RUN cd ./app && pip install -e .

# safer to switch back to nobody, but you need root if you want to develop from VS Code
# USER nobody

CMD ["bash"]