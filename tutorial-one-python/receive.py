#!/usr/bin/env python
import pika
RABBITMQ_URI="amqp://user:pass@localhost:5672"
connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URI))

channel = connection.channel()

# create a queue
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
