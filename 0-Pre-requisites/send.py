import pika
def get_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    return connection

def send_message(message):
    connection = get_connection()
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='hello')

    # Publish a message to the queue
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(f" [x] Sent {message}")
    connection.close()

# Test sending a message
send_message("Hello from RabbitMQ!")
