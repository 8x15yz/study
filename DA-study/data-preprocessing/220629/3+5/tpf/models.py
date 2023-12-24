from django.db import models

# Create your models here.
class CopUBr(models.Model):
    cust = models.CharField(max_length=200)
    rct_no = models.CharField(max_length=200)
    cop_c = models.CharField(max_length=200)
    chnl_dv = models.IntegerField()
    de_dt_y = models.IntegerField()
    de_dt_m = models.IntegerField()
    de_dt_d = models.IntegerField()
    vst_dt_y = models.IntegerField()
    vst_dt_m = models.IntegerField()
    vst_dt_d = models.IntegerField()
    de_hr = models.IntegerField()
    buy_am = models.IntegerField()
    br_c = models.CharField(max_length=200)
    zon_hlv = models.CharField(max_length=200)
    zon_mcls = models.CharField(max_length=200)

class BR(models.Model):
    br_c = models.CharField(max_length=200)
    zon_hlv = models.CharField(max_length=200)
    zon_mcls = models.CharField(max_length=200)