from django.db.models import Model , CharField ,ImageField , PositiveIntegerField ,ForeignKey, FloatField, TextField, IntegerField,CASCADE


class Category(Model):
    name = CharField(max_length=5000)
    parent = ForeignKey('self',CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=5000)
    narxi = FloatField()
    discount = PositiveIntegerField()
    rang = CharField(max_length=200, null=True,blank=True)
    short_description = TextField()
    description = TextField()
    quantity = PositiveIntegerField(default=1)
    category = ForeignKey(Category, on_delete=CASCADE,related_name='products')


class ProductImage(Model):
    image = ImageField(upload_to='products')
    Product = ForeignKey(Product, on_delete=CASCADE, related_name='images')