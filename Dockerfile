FROM thehq/crossbar:0.11.1
MAINTAINER Eric Chapman <eric@thehq.io>

RUN pip install coverage

ENV DIRECTORY=/home/ubuntu/python-crossbarhttp

COPY crossbarhttp/ ${DIRECTORY}/crossbarhttp
COPY tests/*.py ${DIRECTORY}/
COPY tests/run_test.sh ${DIRECTORY}/run_test.sh
RUN chmod +x ${DIRECTORY}/run_test.sh

ENTRYPOINT ["${DIRECTORY}/run_test.sh"]