from connect import connection, connect
from model import Contact

rabbit_chanel = connection.channel()

rabbit_chanel.queue_declare('email', durable=True)
rabbit_chanel.queue_declare('phone', durable=True)
print('Wait')


def main(ch, method, properties, body):
    print('ch: ', ch)
    print('method: ', method)
    print('properties: ', properties)
    print('body: ', body)
    rec = Contact.objects(id=body.decode()).first()
    rec.send = True
    rec.save()
    ch.basic_ack(delivery_tag=method.delivery_tag)


rabbit_chanel.basic_qos(prefetch_count=1)
rabbit_chanel.basic_consume(queue='email', on_message_callback=main)
rabbit_chanel.basic_consume(queue='phone', on_message_callback=main)

if __name__ == '__main__':
    rabbit_chanel.start_consuming()
