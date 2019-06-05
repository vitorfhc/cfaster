FROM python:3-stretch

WORKDIR /cfaster

COPY requirements.txt /cfaster
RUN pip install -r requirements.txt

COPY . /cfaster

ENTRYPOINT ["/bin/bash"]
