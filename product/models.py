from django.db import models
from django.contrib.auth import get_user_model
from master.models import TimeStamp

USER = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Unit(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    secondary_unit = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    conversion_rate = models.FloatField()

    def __str__(self) -> str:
        return f"{self.symbol}"


class Product(TimeStamp, models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="products/imgs", default='default/product.png')
    stock = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(
        USER, on_delete=models.SET_NULL, null=True, blank=True, default="1")
    unit = models.ForeignKey(
        Unit, on_delete=models.SET_NULL, null=True, blank=True, default="1")

    def __str__(self) -> str:
        return f"{self.name}"


class Cart(TimeStamp, models.Model):
    user = models.ForeignKey(
        USER, on_delete=models.SET_NULL, null=True, blank=True)

    def total(self):
        cart_item = CartItem.objects.filter(cart=self, status=True)

    def __str__(self) -> str:
        return f"customer:{self.Customer}, items in cart:{self.number_of_items}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
