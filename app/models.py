from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
   

    def __str__(self) :
        return str(self.id)


CATEGORY_CHOICES = (
    ('V','Vegetables'),
    ('F', 'Fruits'),
    ('LH', 'Leafy and Herbs'),
    ('SD', 'Sale of the day')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self) :
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return str(self.id)  


    @property  
    def total_cost(self):
        return self.quantity * self.product.selling_price        

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    
    @property  
    def total_cost(self):
        return self.quantity * self.product.selling_price        
