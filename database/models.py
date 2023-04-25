from itertools import product

from peewee import *

db = SqliteDatabase("market.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(max_length=200, null=True)
    balance = FloatField(default=0.0)
    address = TextField(null=True)

    class Meta:
        db_name = 'users'


class Cart(BaseModel):
    product = ForeignKeyField('Product', on_delete='CASCADE')
    user = ForeignKeyField('User', on_delete='CASCADE')

    class Meta:
        db_name = 'cart'


class Product(BaseModel):
    name = CharField(max_length=200)
    context = TextField()
    price = FloatField()
    img = CharField()
    available = BooleanField()
    category = ForeignKeyField('Category', on_delete="CASCADE")

    class Meta:
        db_name = 'product'


class Category(BaseModel):
    id = BigIntegerField(primary_key=True)
    name = CharField(max_length=200)

    class Meta:
        db_name = 'category'


class Order(BaseModel):
    payment = CharField()
    user = ForeignKeyField('User', on_delete='CASCADE')
    product = ForeignKeyField('Product', on_delete='CASCADE')

    class Meta:
        db_name = 'order'


class PaymentInfo(BaseModel):
    id = BigIntegerField(primary_key=True)
    card_number = BigIntegerField(primary_key=True)

    class Meta:
        db_name = 'order'
