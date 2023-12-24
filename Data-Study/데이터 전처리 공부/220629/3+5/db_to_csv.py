import csv
import os, sys
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "threePlusFive.settings")
django.setup() 

from tpf.models import CopUBr

list03 = CopUBr.objects.all()
with open('./db_to_csv_v2.csv', 'w', newline='') as f_csv:
    field_names = ['id', 'cust', 'rct_no', 'cop_c', 'chnl_dv',\
        'de_dt_y', 'de_dt_m', 'de_dt_d', 'vst_dt_y', 'vst_dt_m', 'vst_dt_d',\
            'de_hr', 'buy_am', 'br_c', 'zon_hlv', 'zon_mcls']
    data_writer = csv.DictWriter(f_csv, fieldnames=field_names) 
    data_writer.writeheader()

    for row in list03:
        print(row)
        print(row.id)
        data_writer.writerow({
            'id':row.id,
            'cust':row.cust,
            'rct_no':row.rct_no,
            'cop_c':row.cop_c,
            'chnl_dv':row.chnl_dv,
            'de_dt_y':row.de_dt_y,
            'de_dt_m':row.de_dt_m,
            'de_dt_d':row.de_dt_d,
            'vst_dt_y':row.vst_dt_y,
            'vst_dt_m':row.vst_dt_m,
            'vst_dt_d':row.vst_dt_d,
            'de_hr':row.de_hr,
            'buy_am':row.buy_am,
            'br_c':row.br_c, 
            'zon_hlv':row.zon_hlv,
            'zon_mcls':row.zon_mcls
            })