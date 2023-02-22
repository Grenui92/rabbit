from mongoengine import StringField, Document, BooleanField

class Contact(Document):
    name = StringField()
    email = StringField()
    send = BooleanField(default=False)
    phone = StringField()
    preference = StringField()
