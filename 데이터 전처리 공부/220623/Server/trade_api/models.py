from django.db import models

# Create your models here.
class Trade(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    num_ex = models.IntegerField()
    num_im = models.IntegerField()
    amo_ex = models.IntegerField()
    amo_im = models.IntegerField()
    trade_b = models.IntegerField()
    trade_pm = models.IntegerField()