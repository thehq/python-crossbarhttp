FROM thehq/crossbar:0.11.1
MAINTAINER Eric Chapman <eric@thehq.io>

RUN pip install coverage

COPY crossbarhttp/ /home/ubuntu/python-crossbarhttp/crossbarhttp
COPY tests/*.py /home/ubuntu/python-crossbarhttp/
COPY tests/run_test.sh /home/ubuntu/python-crossbarhttp/run_test.sh
RUN chmod +x /home/ubuntu/python-crossbarhttp/run_test.sh

ENTRYPOINT ["/home/ubuntu/python-crossbarhttp/run_test.sh"]