# https://www.docker.com/blog/faster-multi-platform-builds-dockerfile-cross-compilation-guide/

FROM --platform=$BUILDPLATFORM python:3.10 as build
LABEL maintainer="danbobbutcher@gmail.com"
RUN pip install spyne pyyaml zeep
RUN apt update
RUN apt install -y tmux
COPY src/python/ src/python
COPY src/.sensorconfig.yaml src/
COPY src/.serverconfig.yaml src/
COPY src/logs src/logs

ARG TARGETPLATFORM
RUN compile --target=$TARGETPLATFORM -o /out/mybinary

