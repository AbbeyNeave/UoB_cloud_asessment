FROM python:latest

ADD worker/worker_functions.py worker/worker_run.py worker/samples.py ./

RUN pip install uproot awkward vector numpy matplotlib pika

CMD [ "python", "worker_run.py"]
