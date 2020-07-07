FROM python:3.6

RUN pip3 install streamsets
COPY get_pipeline.py /actions/get_pipeline.py
