from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Product(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(default ='default.jpg', upload_to='profile_pics')
    #manufacturer = models.ForeignKey(Manufacturer, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
