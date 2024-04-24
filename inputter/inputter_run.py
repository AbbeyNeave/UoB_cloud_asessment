import pika 
import inputter_functions

#RABBITMQ PRODUCER
params = pika.ConnectionParameters('rabbit',heartbeat=0)
# connect to broker
connection = pika.BlockingConnection(params)
channel = connection.channel()
# create inputfile queue
channel.queue_declare(queue='inputfiles')

#create body for producer
val_list = get_val_list()
fileString_list = get_fileString_list()
file_array = inputter_functions.get_file_array(fileString_list,val_list)

# send files to worker service individually
for file in file_array:
    channel.basic_publish(exchange='',
                      routing_key='inputfiles',
                      body=file)
    print(f'{file} sent')
print("All files have been sent to be processer")
# Close connection
connection.close()

    