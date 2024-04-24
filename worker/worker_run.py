import worker_functions
import pika
import samples
import infofile
import uproot # for reading .root files
import awkward as ak # to represent nested data in columnar format
import vector # for 4-momentum calculations
import time # to measure time to analyse
import math # for mathematical functions such as square root
import numpy as np # for numerical calculations such as histogramming
import pika

#CONSTANTS
lumi = 10 # fb-1 # data_A,data_B,data_C,data_D
fraction = 1.0 # reduce this is if you want the code to run quicker
tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/" # web address
MeV = 0.001


#RABBITMQ CONSUMER
#recieves files one at a time from inputter service
#connect to rabbit server
params = pika.ConnectionParameters('rabbit', heartbeat=0)
#create the connection to broker
connection = pika.BlockingConnection(params)
channel = connection.channel()
# define a function to call when message is received
def callback(ch, method, properties, body):
    body = file
    print(f" [x] Received {inputfiles}")
# setup to listen for messages on queue 'messages'
channel.basic_consume(queue='inputfiles',auto_ack=True, on_message_callback=callback)
# log message to show we've started
print('Waiting for input files')
# start listening
channel.start_consuming()



# ==================== MAIN PROCESSER ======================== #
#PROCESS INPUT FILE
temp_array = worker_functions.read_file(file[0], file[1])
# ============================================================ #



#RABBITMQ PRODUCER
#sends processed file arrays 1 at a time to plotter service

# when starting services with docker compose
params = pika.ConnectionParameters('rabbit', heartbeat=0)
# create the connection to broker
connection = pika.BlockingConnection(params)
channel = connection.channel()
# create the queue, if it doesn't already exist
channel.queue_declare(queue='temp')
# send a simple message
channel.basic_publish(exchange='',routing_key='temp', body=temp_array)
# log message sending
print("temp_array sent")
