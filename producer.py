from connect import connection, connect
from model import Contact
from faker import Faker
from random import choice


rabbit_chanel = connection.channel()

rabbit_chanel.exchange_declare(exchange='new_ex', exchange_type='direct')
rabbit_chanel.queue_declare(queue='email', durable=True)
rabbit_chanel.queue_declare(queue='phone', durable=True)
rabbit_chanel.queue_bind(exchange='new_ex', queue='email', routing_key='email')
rabbit_chanel.queue_bind(exchange='new_ex', queue='phone', routing_key='phone')
fake_data = Faker()

def main():

    contacts = Contact.objects()
    for record in contacts:
        print(type(record.preference), record.preference)
        rabbit_chanel.basic_publish(exchange='new_ex',
                                    routing_key=record.preference,
                                    body=str(record.id))
    connection.close()

if __name__ == '__main__':
    main()
