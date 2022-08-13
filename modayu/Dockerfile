# GPU docker image CUDA 11.6 cuDNN 8302 ubuntu 20.04
# FROM nvidia/cuda:11.6.0-cudnn8-devel-ubuntu20.04
FROM python:3.8.13

# # 数据库连接支持
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list&&\
    apt-get clean && apt-get update && \
    apt-get install default-libmysqlclient-dev python3 python3-pip -y

ENV PYTHONUNBUFFERED 1
# 工作目录 
RUN mkdir -p /app &&\
    mkdir -p /root/.pip/
WORKDIR /app
COPY . /app/

# 镜像源 && 更新pip版本 && 安装依赖
COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
RUN chmod +x ./start.sh

