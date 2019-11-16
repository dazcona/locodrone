FROM ubuntu:16.04

# Install general dependencies
RUN apt-get update && apt-get install -y \
    git \
    cmake

# install python 2.7
RUN apt-get install python2.7 python-pip -y
RUN pip install --upgrade pip

# switch to python2.7
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2 150 
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 100

# Install dependencies
RUN apt-get update && apt-get install -y \
    libboost-all-dev \
    libavcodec-dev \
    libswscale-dev 

# Python dependencies
RUN pip install \
    numpy \
    matplotlib \
    opencv-python

# imaging-tk

RUN mkdir /tools

# Install h264decoder
RUN mkdir -p /tools/h264decoder/
ADD h264decoder/ /tools/h264decoder
WORKDIR /tools/h264decoder
RUN mkdir build
WORKDIR /tools/h264decoder/build
RUN cmake ..
RUN make -j4 && make install

# Remove unneeded files
RUN rm -rf /tools

WORKDIR /code