from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator,MinValueValidator                        #positiveIntegerFieldil minimum value max value veraan

# Create your models here.

class Products(models.Model):

    name = models.CharField(unique=True,max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    catogory = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image',null=True)

    def __str__(self) :
        return self.name




class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)             #on_delete:user tablil delete ayaal ithinnum delete aavan
 
    product=models.ForeignKey(Products,on_delete=models.CASCADE)       #auto_now_add:automatic date veran

    date=models.DateTimeField(auto_now_add=True)                       


class Reviews(models.Model):

    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=200)

    def __str__(self) :
        return self.comment
