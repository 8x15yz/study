## 데이터 전처리_결측치 메우기

`참고사이트` : https://runebook.dev/ko/docs/scikit_learn/modules/generated/sklearn.impute.simpleimputer

![example_0120_1](https://user-images.githubusercontent.com/87743473/150446189-4cd93748-44ec-4121-8903-67c49a16debb.png)

 

**1. NaN 비율이 0.5 이상인 칼럼 삭제**

**2. obj 형태로 된 칼럼은 0/1으로 값 변환**

**3. NaN 데이터에 해당 칼럼의 평균값으로 채워주기**

 

##### 모듈 임포트하기

```python
import pandas as pd
import numpy as np
from scipy.stats import norm
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.simplefilter('ignore')
```


```python
train = pd.read_csv('0120.csv', index_col='id')
print(train.shape)
```

train이라는 변수에 파일을 불러오고 train.shape()

    (11, 7)

```python
train.head()
```

대강의 데이터 보기위해 헤드 띄우기

![example_0120_2](https://user-images.githubusercontent.com/87743473/150446190-3d0ac17d-2c92-43eb-8a60-86053b25cd84.png)

  

 

###  **1. NaN 비율이 0.5 이상인 칼럼 삭제**


```python
check_null = train.isna().sum() / len(train)
check_null[check_null >=0.5]
```

.isna().sum() => 즉 NaN의 갯수를 센 것이고 

len(train)을 사용해서 칼럼의 셀 수를 다 센 값을 나눠주는

결과:


    e    0.727273
    dtype: float64

e칼럼에 NuN 비율이 0.7

 

 

 


```python
remove_cols = check_null[check_null >= 0.5].keys()
train = train.drop(remove_cols, axis=1)
train.head()
```

![example_0120_3](https://user-images.githubusercontent.com/87743473/150446191-1c22d1c1-757f-4350-818f-8fb822a56f77.png)

e 칼럼이 사라진 모습

  

###   **2. obj 형태로 된 칼럼은 0/1으로 값 변환**


```python
obj_t = train.select_dtypes(include='object')
num_t = train.select_dtypes(exclude='object')
print('Object type columns:\n',obj_t.columns)
print('---------------------------------------------------------------------------------')
print('Numeric type columns:\n',num_t.columns)
```

![example_0120_4_1](https://user-images.githubusercontent.com/87743473/150446181-2279ae4b-42c0-4fbc-937e-14b30ec980f2.png)

 

 칼럼 유형을 숫자가 아닌 형태/숫자형태로 나눈것

pd.get_dummies() 함수를 사용해 obj 형태 데이터를 숫자형(0/1)으로 변환하는 작업

```python
index_t = train.index
dummy_t = pd.get_dummies(obj_t, drop_first=True) #첫번째 값을 기준으로 T/F으로 나눔
dummy_t.index = index_t
dummy_t.head()
```

![example_0120_4](https://user-images.githubusercontent.com/87743473/150446193-0da8362a-0198-4a20-bfd3-bf508af34750.png)



 

 

###   **3. NaN 데이터에 해당 칼럼의 평균값으로 채워주기


```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer()
```


```python
imp_mean = SimpleImputer(missing_values =np.nan, strategy= 'mean')
imp_mean.fit(num_t)
```

imp_mean 변수에 SimpleImputer 함수를 설정해줌 => 이번에는 NaN값을 평균치로 채우려고 strategy= 'mean'을 하였다


```python
imp_mean.transform(num_t)
num_t.head()
```

![example_0120_5](https://user-images.githubusercontent.com/87743473/150446184-a2a1f09b-6f6b-4386-abfd-1b3339f4524b.png)

 

 

 

##### 이때 주의할점이있는데

`imp_mean()`에 원형 데이터를 넣으면 안됨 

![example_0120_6](https://user-images.githubusercontent.com/87743473/150446186-d03418ac-adc5-45fe-952a-05f32e2eef80.png)



꼭 2번에서 `.select_dtypes(exclude='object')` 을 적용해준 변수를 집어넣어야 된다

![example_0120_7](https://user-images.githubusercontent.com/87743473/150446187-e880a6b1-9c29-4fc5-8407-1e94d4bafb11.png)
