from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sale = models.BooleanField(default=False, editable=False)
    sale_count = models.FloatField(default=1)

    @property
    def current_price(self):
        return round(float(self.price) * self.sale_count)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    done = models.BooleanField(default=False)

    @property
    def price(self):
        result = 0
        for product in self.products.all():
            result += product.current_price
        return result

    def save(self, *a, **kw):
        if self.done:
            Order.objects.create(total_price=self.price, user=self.user)

class Order(models.Model):
    total_price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)