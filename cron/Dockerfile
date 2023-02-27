FROM alpine:3

RUN apk --no-cache add curl
COPY crontab.txt /crontab.txt
COPY script.sh /script.sh
COPY consumer.py /consumer.py
COPY entrypoint.sh /entrypoint.sh
RUN bash consumer.sh
RUN /usr/bin/crontab /crontab.txt

ENTRYPOINT ["/entrypoint.sh"]
