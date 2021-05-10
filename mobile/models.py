from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=120)
    price=models.FloatField()
    specs=models.CharField(max_length=150)
    image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    address=models.CharField(max_length=150)
    choices=(
        ("Ordered","Ordered"),
        ("Delivered","Delivered"),
        ("Cancelled","Cancelled")
    )
    status=models.CharField(max_length=100,choices=choices,default="Ordered")
    user=models.CharField(max_length=120)



class cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    total_price=models.PositiveIntegerField(editable=False,blank=True,null=True)
    user=models.CharField(max_length=120)

    def save(self,*args,**kwargs):
        self.total_price=self.product.price*self.qty
        super(cart, self).save(*args,**kwargs)


    









