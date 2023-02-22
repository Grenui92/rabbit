from configparser import ConfigParser
from mongoengine import connect
import pika


config = ConfigParser()
config.read('config.ini')
user_name = config.get('DB', 'user')
password = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
db_domain = config.get('DB', 'db_domain')

mq_user = config.get('MQ', 'user')
mq_password = config.get('MQ', 'pass')
mq_host = config.get('MQ', 'host')
mq_port = config.get('MQ', 'port')

connect(host=f"""mongodb+srv://{user_name}:{password}@{db_domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

credentials = pika.PlainCredentials(mq_user, mq_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host, port=int(mq_port), credentials=credentials))
