FROM archlinux:latest
RUN pacman -Syu --noconfirm base-devel python python-pip
RUN pip install aiomqtt paho-mqtt typer --break-system-packages
COPY ./src/* /opt
WORKDIR /opt
CMD python ./mapper.py
