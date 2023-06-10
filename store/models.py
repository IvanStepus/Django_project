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



class Department(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class Supermarket(models.Model):
    country_create = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    floor = models.IntegerField()
    #fresh = models.BooleanField(True)
    date_of_create = models.DateField()
    departments = models.ManyToManyField(Department)
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True,
                              limit_choices_to={'is_staff': True},
                              related_name='market'
                              )

    def __str__(self):
        return f"{self.brand}-{self.country_create}"





# FAKER - создаёт рандомных пользователей
# from django.contrib.auth.models import User
# from faker import Faker
# fake = Faker()
# for _ in range(10):
#     user = User.objects.create_user(
#         username=fake.unique.user_name(),
#         email=fake.unique.email(),
#         password=fake.password(length=10),
#         first_name=fake.first_name(),
#         last_name=fake.last_name(),
#     )
