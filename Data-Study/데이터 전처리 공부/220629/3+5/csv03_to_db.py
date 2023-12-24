import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threePlusFive.settings')
django.setup()

from tpf.models import CopUBr, BR

# 데이터를 합치기 위해 5번 데이터가 담긴 모델(BR)을 불러옴
# 아직 비어있는 CopUBr 모델에 담을예정

list05 = BR.objects.all() # BR 모델의 쿼리셋을 list05 변수에 담았음

with open('./LPOINT_BIG_COMP_03_COP_U.csv') as csv03:  # 3번 파일을 열고
    csv03 = csv.reader(csv03)
    zon_hlv = ''      # 추가할 데이터
    zon_mcls = ''     # 추가할 데이터
    next(csv03, None)
    cnt = 0           # 데이터 수가 너무 많아서 몇개 째 작업중인지 출력해보기 위한 변수
    for row03 in csv03:
        for arr in list05:                # list05 쿼리셋에서 하나씩 비교하기
            if arr.br_c == row03[12]:     # row03[12] = br_c 컬럼의 데이터를 기준으로 3번파일의 값이 현재 조회하는 값이면
                zon_hlv = arr.zon_hlv     # 해당 행에서 추가할 데이터 컬럼들 가져오기 
                zon_mcls = arr.zon_mcls
                cnt += 1                  # 데이터 하나 처리 완료했으므로 process 누적
                print(row03[12], zon_hlv, zon_mcls, cnt)

                CopUBr.objects.create(    # 모델에 데이터 넣어주기
                    cust = row03[0],
                    rct_no = row03[1],
                    cop_c = row03[2],
                    chnl_dv = row03[3],
                    de_dt_y = row03[4],
                    de_dt_m = row03[5],
                    de_dt_d = row03[6],
                    vst_dt_y = row03[7],
                    vst_dt_m = row03[8],
                    vst_dt_d = row03[9],
                    de_hr = row03[10],
                    buy_am = row03[11],
                    br_c = row03[12],
                    zon_hlv = zon_hlv,
                    zon_mcls = zon_mcls
                )
                # cnt += 1
                break                       # 더이상 비교할 필요 없으므로 break
        else:                               # 5번 파일에 일치하는 데이터가 없는 경우!! (예외처리)
            zon_hlv = '-'                   # 값을 - 으로 채우기
            zon_mcls = '-'
            cnt += 1
            print(row03[12], zon_hlv, zon_mcls, cnt)
            CopUBr.objects.create(
                cust = row03[0],
                rct_no = row03[1],
                cop_c = row03[2],
                chnl_dv = row03[3],
                de_dt_y = row03[4],
                de_dt_m = row03[5],
                de_dt_d = row03[6],
                vst_dt_y = row03[7],
                vst_dt_m = row03[8],
                vst_dt_d = row03[9],
                de_hr = row03[10],
                buy_am = row03[11],
                br_c = row03[12],
                zon_hlv = zon_hlv,
                zon_mcls = zon_mcls
            )

        # if cnt == 100:
        #     break