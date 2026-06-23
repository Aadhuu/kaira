from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField(null=True)
    availability =models.BooleanField(default=True,null=True)
    gender= models.CharField(max_length=200,default='unisex',null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

