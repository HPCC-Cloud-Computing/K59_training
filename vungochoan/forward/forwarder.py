import pika
import sys

file = open("configure.cfg", "r")
data = file.readlines()

# Connection rabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host = data[1].replace('\n', '')))
channel = connection.channel()

def get(channel):
	# Create exchange type topic
	channel.exchange_declare(exchange = data[4].replace('\n', ''), exchange_type = 'direct')

	# Create queue
	channel.queue_declare(queue = data[7].replace('\n', ''))

	binding_keys = [data[10].replace('\n', '')]

	for binding_key in binding_keys:
		# Link exchange to queue with routing_key
		channel.queue_bind(
			exchange = data[4].replace('\n', ''),
			queue = data[7].replace('\n', ''),
			routing_key = binding_key
			)

	print(' [+] Waiting for logs. To exit press CTRL+C')

	def callback(ch, method, properties, body):
		routing_data(method.routing_key, body)

	channel.basic_consume(callback, queue = data[7].replace('\n', ''), no_ack = True)
	channel.start_consuming()

def routing_data(routing_key, body):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host = data[1].replace('\n', '')))
	channel = connection.channel()

	# Create exchange type direct
	channel.exchange_declare(exchange = data[13].replace('\n', ''), exchange_type = 'direct')

	routing = routing_key
	message = body

	channel.basic_publish(exchange = data[13].replace('\n', ''), routing_key = routing, body = message)

	print(" [x] Sent %r:%r" % (routing, message))

	connection.close()

get(channel)
