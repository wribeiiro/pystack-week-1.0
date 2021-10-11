FROM python:3.8

WORKDIR /plataforma_cursos/
ENV PYTHONUNBUFFERED=1
RUN apt update && apt upgrade -y && apt install -y python3-pip 
COPY docker/requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./src/ .
CMD bash start.sh