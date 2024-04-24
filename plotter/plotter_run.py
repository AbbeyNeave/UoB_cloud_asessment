import pika
import plotter_functions
import awkward


#RABBITMQ CONSUMER
#recieves processed files 1 at a time from worker service
# connect to rabbit server
params = pika.ConnectionParameters('rabbit', heartbeat=0)
# create the connection to broker
connection = pika.BlockingConnection(params)
channel = connection.channel()
# define a function to call when message is received
def callback(ch, method, properties, body):
    ch= 
    method=
    properties=
    body = temp_array
    print(f" [x] Received {temp}")
# setup to listen for messages on queue 'messages' 
channel.basic_consume(queue='temp',
                      auto_ack=True,
                      on_message_callback=callback)
# log message to show we've started
print('Waiting for temp')
# start listening
channel.start_consuming()

# ============== MAIN ============== #
data = prep_data(temp_array)
plot_data(data)
# ================================== #
