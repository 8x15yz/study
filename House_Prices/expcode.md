#### 모듈 import + 데이터 불러오기

모듈 :  `pandas`  `numpy`  `scipy.stats.norm`  `matpoltlib`  `seaboen`

`train.csv`  = 데이터 fit용 (정답 레이블이 있는 학습용 데이터)

`test.csv `  = 학습한 데이터로 prediction (정답 레이블이 없는 테스트용 데이터)

`sample_submission.csv`  = 제출용 데이터 예시(결과 틀을 이 파일의 테이블 형식으로)

```python
import pandas as pd
import numpy as np
from scipy.stats import norm
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.simplefilter('ignore')

train = pd.read_csv('train.csv', index_col='Id')
test = pd.read_csv('test.csv', index_col='Id')
submission = pd.read_csv('sample_submission.csv', index_col='Id')
data = train #데이터 겹침 방지
```

```python
print(train.shape, test.shape, submission.shape)
```

```결과
(1460, 80) (1459, 79) (1459, 1)
```

test 파일 인덱스가 79개

NaN값이나 str 자료형들은 이따가 결측치 제거하는 작업이나 가중치 할당이 필요함





#### target class 확인 (SalePrice) 

train 파일에서 타겟 요인인 SalePrice값들을 히스토그램으로 표현

```python
sns.distplot(data['SalePrice'], fit=norm)
```

(이미지 넣기)

데이터가 Right Skewed 됐으므로 정규분포에 가깝게 보일수 있도록 log적용하여 보정:

( https://dining-developer.tistory.com/18 ) 

```python
sns.distplot(np.log(data['SalePrice']), fit=norm)
```

(이미지 넣기)





#### 히트맵 그리기

변수 간의 조합(상관관계)을 보기 위해 히트맵을 작성함 :

(https://seaborn.pydata.org/generated/seaborn.heatmap.html) 히트맵에 대해

(https://wikidocs.net/14604) (http://daplus.net/python-%EB%A7%8E%EC%9D%80-%EC%98%88%EC%A0%9C%EA%B0%80-matplotlib-pyplot-python%EC%97%90%EC%84%9Cfig-ax-plt-subplots-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EC%9D%B4%EC%9C%A0/) => fig,ax = plt.subplots()에 대해

plt.subplot()은 figure과 axes 객체를 포함하는 튜플을 반환하는 함수 - 보통 

nlargest를 이용해서 상관관계가 높은 순서대로 값을 히트맵에 작성

``` python
d_corr = data.corr()
top_corr = data[d_corr.nlargest(80,'SalePrice')['SalePrice'].index].corr()
fig, ax_1 = plt.subplots(nrows=1, ncols=1)
fig.set_size_inches(20,20)
sns.heatmap(top_corr, annot=True, ax=ax_1)
```

(이미지 넣기)



`.corr()` -> 피어슨 상관계수를 측정하는 함수: 절댓값이 높을 수록 관계가 있는

OverallQual이 제일 높고 상위 19정도까지 (BsmtUnfSF까지) 관계가 뚜렷해보임

##### 상위 19개 데이터 다 그려보기 (이상치 삭제하기 위함)

```python 
sns.regplot(data['인덱스이름'], data['SalePrice'])
```

- **OverallQual**: Overall material and finish quality
- (각각 이미지 첨부)
- **GrLivArea**: Above grade (ground) living area square feet
- **GarageCars**: Size of garage in car capacity
- **GarageArea**: Size of garage in square feet
- **TotalBsmtSF**: Total square feet of basement area
- **YearBuilt**: Original construction date
- **YearRemodAdd**: Remodel date
- **GarageYrBlt**: Year garage was bilt
- **MasVnrArea**: Masonry veneer area in square feet
- **Fireplaces**: Number of fireplaces
- **BsmtFinSF1**: Type 1 finished square feet
- **LotFrontage**: Linear feet of street connected to property
- **WoodDeckSF**: Wood deck area in square feet
- **2ndFlrSF**: Second floor square feet
- **OpenPorchSF**: Open porch area in square feet
- **HalfBath**: Half baths above grade
- **LotArea**: Lot size in square feet
- **BsmtFullBath**: Basement full bathrooms
- **BsmtUnfSF**: Unfinished square feet of basement area



아웃라이어 삭제하기:

```python
train=train.drop(train[(train['GrLivArea']>4000) & (train['SalePrice']<300000)].index) 
train=train.drop(train[(train['GarageArea']<1000) & (train['SalePrice']>700000)].index) 
train=train.drop(train[(train['TotalBsmtSF']>5000) & (train['SalePrice']<300000)].index) 
train=train.drop(train[(train['YearRemodAdd']>1990) & (train['SalePrice']>650000)].index) 
train=train.drop(train[(train['GarageYrBlt']>1980) & (train['SalePrice']>650000)].index) 
train=train.drop(train[(train['MasVnrArea']<1400) & (train['SalePrice']>650000)].index) 
train=train.drop(train[(train['BsmtUnfSF']<1500) & (train['SalePrice']>700000)].index) 
```

(바뀐 이미지 첨부)



####  데이터 처리 준비 : `train` + `test`  concat 하기

train과 test 셋에 동일한 feature engineering을 적용해주기 위해 입시로 합치기

```python
#t_plus 시작 = 임시로 concat 하는
train=train[list(test)]
t_plus=pd.concat((train, test), axis=0)
index_t_plus = t_plus.index 
print(t_plus.shape)
```

```python
(2915, 79)
```

```python
t_plus.head()
```

(헤드 결과 이미지 게시)





#### 결측치 삭제/대체 + 문자형자료 가중치 할당

##### 결측치 삭제

`.isna().sum()`  사용하고 (isna나 isnull이나 이름만 다르지 기능은 동일함) `.fillna()` 로 값을 채워주기 

https://www.delftstack.com/ko/howto/python-pandas/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe/

https://computer-science-student.tistory.com/306

https://workingwithpython.com/howtohandlemissingvaluewithpython/

절반 이상이 결측치인 인덱스는 삭제하고  나머지는 평균값으로 fillna하려고 함

```python
check_null = t_plus.isna().sum() / len(t_plus)
check_null[check_null >= 0.4]
```



`.isna().sum()` => 각 칼럼에서 NaN인것과 아닌것을 boolean type으로 변환`.isna()` 하고 갯수를 센 다음`.sum()`  각 칼럼의 전체 데이터 수로 나누면 `/ len(t_plus_t))`   비율으로 나올 것임

그리고 check_null 리스트에서 비율이 0.5 이상인 칼럼들을 지금 리턴한거임 => `4 칼럼이 나옴 `

+) 다른값도 대입해보니까 0.48도 있느넫 이것도 포함시키겠음

```결과
Alley          0.932075
PoolQC         0.997256
Fence          0.804460
MiscFeature    0.963979
FireplaceQu    0.487136
```

- **Alley**: Type of alley access
- **PoolQC**: Pool quality
- **Fence**: Fence quality
- **MiscFeature**: Miscellaneous feature not covered in other categories
- **FireplaceQu**: Fireplace quality



```python
remove_cols = check_null[check_null >= 0.4].keys()
t_plus = t_plus.drop(remove_cols, axis=1)
t_plus.head()
```

네개 항목 삭제한 모습 이미지 첨부



##### 가중치 할당

숫자가 아닌 자료형들을 obj_t_plus 변수에 할당하고 구분하는 코드

```python
obj_t_plus = t_plus.select_dtypes(include='object')
num_t_plus = t_plus.select_dtypes(exclude='object')
print('Object type columns:\n',obj_t_plus.columns)
print('---------------------------------------------------------------------------------')
print('Numeric type columns:\n',num_t_plus.columns)
```

```결과
Object type columns:
 Index(['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities',
       'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
       'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
       'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
       'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
       'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual',
       'Functional', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
       'PavedDrive', 'SaleType', 'SaleCondition'],
      dtype='object')
---------------------------------------------------------------------------------
Numeric type columns:
 Index(['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond',
       'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
       'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
       'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
       'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
       'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
       'MoSold', 'YrSold'],
      dtype='object')
```



obj로 구분한 값들에 대해 one-hot-encoding을 적용하기 위해 **pd.get_dummies()** 사용

(one-hot-encoding이란? https://wikidocs.net/22647)

(범주 데이터를 숫자로 인코딩하기 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=youji4ever&logNo=221698612004)

```python
dummy_t_plus = pd.get_dummies(obj_t_plus, drop_first=True)
dummy_t_plus.index = index_t_plus
dummy_t_plus.head()
```





##### 결측치 대체 https://wikidocs.net/83943

null값들을 그 칼럼의 평균으로 대체해줄것 (sklearn 사용)

```python
```





##### 