FROM python:3.10
LABEL maintainer="danbobbutcher@gmail.com"
RUN pip install spyne pyyaml zeep
RUN apt update
RUN apt install -y tmux
COPY src/python/ src/python
COPY src/.sensorconfig.yaml src/
COPY src/.serverconfig.yaml src/
COPY src/logs src/logs
WORKDIR /src
