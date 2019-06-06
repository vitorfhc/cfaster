FROM python:3-stretch

WORKDIR /cfaster

COPY requirements.dev.txt /cfaster
RUN pip install -r requirements.dev.txt

COPY . /cfaster

ENTRYPOINT ["/bin/bash"]
