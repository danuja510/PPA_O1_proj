from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    def get_total(self):
        total = self.item.price * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal

#Order Model
class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=50, null=True)
    postal_code = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.filter(purchased=False).all():
            total += order_item.get_total()
        
        return total

    def get_totals_purchased(self):
        total = 0
        for order_item in self.orderitems.filter(purchased=True).all():
            total += order_item.get_total()
        
        return total
