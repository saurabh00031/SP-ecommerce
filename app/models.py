from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

STATE_CHOICES=(
('Andaman','Andaman'),
('Maharashtra','Maharashtra'),
('Madhya Pradesh','Madhya Pradesh'),
('Rajasthan','Rajasthan'),
('Chattisgarh','Chattisgarh'),
('Daman & Diu','Daman & Diu'),
('Goa','Goa'),
('Uttar Pradesh','Uttar Pradesh'),
('West Bengal','West Bengal'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Karnataka','Karnataka')
)

class Customerinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=60)


    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
('M','Mobile'),
('L','Laptop'),
('TW','Top Wear'),
('BW','Bottom Wear'),
('TV','Television'),
('W','Watch')
)

class Productinfo(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=3)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)   



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Productinfo,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id) 

    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price

STATUS_CHOICES=(
('Accpetd','Accepted'),
('Packed','Packed'),
('On The Way','On The Way'),
('Delivered','Delivered'),
('Cancel','Cancel'),
('Area Restriction','Area Restriction'),
('Pending','Pending')
)

class OrderPlaceinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customerinfo,on_delete=models.CASCADE)
    product=models.ForeignKey(Productinfo,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=60,choices=STATUS_CHOICES,default='Pending')

  

