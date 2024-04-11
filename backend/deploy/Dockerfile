FROM debian:bullseye

RUN apt update && apt-get upgrade -y

RUN apt-get install -y git python3-pip libmariadb-dev-compat pkg-config

WORKDIR /opt

RUN git clone https://github.com/Auwate/backend.git

WORKDIR /opt/backend

RUN pip install -r requirements.txt

EXPOSE 80

COPY docker-startup.sh /
RUN chmod +x /docker-startup.sh

COPY api_key.txt /opt/backend/deploy/
RUN chmod +r /api_key.txt

CMD [ "/docker-startup.sh" ]