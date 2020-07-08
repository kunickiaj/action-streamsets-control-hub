FROM python:3.6

ENV actions /actions
WORKDIR ${actions}

COPY requirements.txt ${actions}/
RUN pip3 install -r requirements.txt

COPY get_pipeline.py ${actions}/
