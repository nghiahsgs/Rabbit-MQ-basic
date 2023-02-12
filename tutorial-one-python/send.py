#!/usr/bin/env python
import pika
RABBITMQ_URI="amqp://user:pass@localhost:5672"
connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URI))

channel = connection.channel()

# create a queue
channel.queue_declare(queue='hello')

# message -> exchange -> queue
# exchange = '' : default exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!1')
print("[x] Sent 'Hello World!'")

connection.close()
