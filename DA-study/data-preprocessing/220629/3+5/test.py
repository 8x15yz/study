import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threePlusFive.settings')
django.setup()

from tpf.models import BR

list05 = BR.objects.all()
for arr in list05:
    print(arr.zon_hlv)
    break
