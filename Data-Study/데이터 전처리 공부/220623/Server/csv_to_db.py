import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from trade_api.models import Trade

with open('./trade_api/data_preprocessing.csv') as csvfile:
    data_reader = csv.reader(csvfile)
    next(data_reader, None)
    for row in data_reader:
        print(row)
        if int(row[6]) > 0:
            pm = 1
        else:
            pm = 0
        Trade.objects.create(
            year = row[0],
            month = row[1],
            num_ex = row[2],
            num_im = row[3],
            amo_ex = row[4],
            amo_im = row[5],
            trade_b = row[6],
            trade_pm = pm
        )