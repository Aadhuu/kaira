from django.contrib.auth.models import User
from django.db import models
from shop.models import Product


class Cart(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.IntegerField(default=0)
    date_added =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def subtotal(self):
        return self.quantity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id=models.CharField(max_length=50,default="")
    amount =models.IntegerField(default=0)
    ordered_date =models.DateTimeField(auto_now_add=True)
    payment_method =models.CharField(max_length=50,default="")
    address =models.TextField(max_length=500,default="")
    phone =models.IntegerField(default=0)
    is_ordered =models.BooleanField(default=False)
    delivery_status=models.CharField(default='Pending',max_length=50)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.IntegerField(default=0)
