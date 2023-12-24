import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threePlusFive.settings')
django.setup()

from tpf.models import BR

with open('./LPOINT_BIG_COMP_05_BR.csv') as csv05: # 5번 파일을 열어서 
    csv05 = csv.reader(csv05)                      
    next(csv05, None)
    for row05 in csv05:                            # 각 행에 대해 
        print(row05)
        BR.objects.create(                         # BR 모델에 데이터를 담기
            br_c = row05[0],
            zon_hlv = row05[2],
            zon_mcls = row05[3]
        )