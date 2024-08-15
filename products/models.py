from django.db.models import Model , CharField ,ImageField , PositiveIntegerField ,ForeignKey, FloatField, TextField, IntegerField,CASCADE


class Category(Model):
    name = CharField(max_length=5000)
    # parent = 


    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=5000)
    narxi = FloatField()
    discount = PositiveIntegerField()
    rang = CharField(max_length=200)
    short_description = TextField()
    description = TextField()
    quantity = IntegerField()
    category = ForeignKey(Category, on_delete=CASCADE)


class ProductImage(Model):
    image = ImageField()
    Product = ForeignKey(Product, on_delete=CASCADE)