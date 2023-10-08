from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField, connect, CASCADE

connect(db="test", host='mongodb+srv://anatolii:maiden94@cluster0.wgxobak.mongodb.net/?retryWrites=true&w=majority')

class Author(Document):
    fullname = StringField(max_length=120, required=True)
    born_date = StringField(max_length=120)
    born_location = StringField(max_length=120)
    description = StringField()

class Quote(Document):
    tags = ListField(StringField(max_length=40))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()