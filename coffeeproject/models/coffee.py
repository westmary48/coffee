from django.db import models
from .shops import Shop
from .baristas import Barista

class Coffee(models.Model):

    name = models.CharField(max_length = 100)
    roast = models.CharField(max_length = 100)
    flavor = models.CharField(max_length = 100)
    aroma  = models.IntegerField(max_length = 100)
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
    barista = models.ForeignKey(Barista, on_delete=models.CASCADE)