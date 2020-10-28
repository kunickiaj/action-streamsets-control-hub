FROM python:3.6

LABEL org.opencontainers.image.source https://github.com/kunickiaj/action-streamsets-control-hub

ENV actions /actions
WORKDIR ${actions}

COPY requirements.txt ${actions}/
RUN pip3 install -r requirements.txt

COPY get_pipeline.py ${actions}/
