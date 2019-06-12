FROM python:3.5-stretch

WORKDIR /cfaster

RUN apt update
RUN apt -y install make

COPY dev-requirements.txt /cfaster
RUN pip install -r dev-requirements.txt

COPY . /cfaster

ENTRYPOINT ["/bin/bash"]
