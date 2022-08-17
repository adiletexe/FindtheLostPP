from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class FoundItems(models.Model):
    title = models.CharField(max_length=100)
    textfield = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=False, blank=False)
    email = models.EmailField(max_length=50, blank=True)
    phonenumber = models.CharField(max_length=16, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Found Item'
        verbose_name_plural = 'Found Items'


