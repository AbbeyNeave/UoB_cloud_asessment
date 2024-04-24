FROM python:latest

ADD inputter/infofile.py inputter/inputter_functions.py inputter/inputter_run.py inputter/samples.py ./

RUN pip install uproot awkward vector numpy matplotlib pika

CMD [ "python", "inputter_run.py"]
