FROM python:3.9-slim-buster

# Install base Python dependencies
RUN apt-get update -y && \
    apt-get install -y \
        curl \
        build-essential \
        iputils-ping \
        gnupg2 \
        wget \
        make && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt Makefile viewer-start.sh /serivce/

WORKDIR /serivce

RUN make deps
RUN chmod +x /serivce/viewer-start.sh

COPY viewer /serivce/viewer
