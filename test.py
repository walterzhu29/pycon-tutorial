import time
import pika
import pika.spec

RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = '5672'
RABBITMQ_USER = 'root'
RABBITMQ_PASS = '1234'

# connection & channel
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                       port=RABBITMQ_PORT,
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


# ==================== produce message ====================

# channel.queue_declare(
#     queue='hello',
#     durable=True,
#     )

# msg = 'hello world!'
# channel.basic_publish(
#     exchange='', 
#     routing_key='hello', 
#     body=msg, 
#     properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
#     )
# print(f' [x] Sent: {msg}')

# for i in range(1,20+1):

#     msg = str(i)
#     channel.basic_publish(exchange='', routing_key='hello', body=msg)
#     print(f' [x] Sent: {msg}')

# connection.close()


# ==================== consume message [1] ====================

# channel.queue_declare(queue='hello', durable=True)

# method, properties, body = channel.basic_get(queue='hello')
# print(f' [x] Received: {body.decode()}')
# channel.basic_ack(method.delivery_tag)


# ==================== consume message [2] ====================

# channel.queue_declare(queue='hello', durable=True)

# def callback(ch, method, properties, body):

#     print(f" [x] Received {body.decode()}")
#     time.sleep(1)

# channel.basic_consume(queue='hello', on_message_callback=callback)

# try:
#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()
# except KeyboardInterrupt:
#     print('Interrupted.')
#     channel.stop_consuming()

# connection.close()


# ==================== consume message [3] ====================

# channel.queue_declare(queue='hello')

# for method, properties, body in channel.consume(queue='hello', inactivity_timeout=10):

#     print(f" [x] Received {body.decode()}")
#     time.sleep(1)

#     if method == None and properties == None and body == None:
#         break

# connection.close()
