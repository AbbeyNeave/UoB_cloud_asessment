FROM python:latest

ADD plotter/plotter_functions.py plotter/plotter.py ./

RUN pip install uproot awkward vector numpy matplotlib pika

CMD [ "python", "-u", "plotter_run.py"]
