FROM erichq/crossbar
MAINTAINER Eric Chapman <eric@headquartershq.com>

COPY .crossbar/ /app/.crossbar/
COPY src/ /app/src/

ENTRYPOINT cd /app/ && crossbar start
CMD ["--config", "/app/.crossbar/config.json"]