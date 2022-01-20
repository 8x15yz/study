## 데이터 전처리_SimpleImputer을 활용한 결측치 메우기 작업

`참고사이트` : https://runebook.dev/ko/docs/scikit_learn/modules/generated/sklearn.impute.simpleimputer

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

    (11, 7)



```python
train.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>\ta</th>
      <th>\tb</th>
      <th>\tc</th>
      <th>\td</th>
      <th>e</th>
      <th>f</th>
      <th>g</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1.00</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>2.00</td>
      <td>NaN</td>
      <td>x</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>-1.00</td>
      <td>NaN</td>
      <td>0.9</td>
      <td>45.00</td>
      <td>NaN</td>
      <td>o</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>5.00</td>
      <td>7.0</td>
      <td>78.0</td>
      <td>-35.00</td>
      <td>NaN</td>
      <td>o</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>2.00</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>1.00</td>
      <td>NaN</td>
      <td>o</td>
      <td>-35.00</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0.22</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.84</td>
      <td>NaN</td>
      <td>o</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>



```python
check_null = train.isna().sum() / len(train)
check_null[check_null >=0.5]
```


    e    0.727273
    dtype: float64




```python
remove_cols = check_null[check_null >= 0.5].keys()
train = train.drop(remove_cols, axis=1)
train.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>\ta</th>
      <th>\tb</th>
      <th>\tc</th>
      <th>\td</th>
      <th>f</th>
      <th>g</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1.00</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>2.00</td>
      <td>x</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>-1.00</td>
      <td>NaN</td>
      <td>0.9</td>
      <td>45.00</td>
      <td>o</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>5.00</td>
      <td>7.0</td>
      <td>78.0</td>
      <td>-35.00</td>
      <td>o</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>2.00</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>1.00</td>
      <td>o</td>
      <td>-35.00</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0.22</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.84</td>
      <td>o</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
obj_t = train.select_dtypes(include='object')
num_t = train.select_dtypes(exclude='object')
print('Object type columns:\n',obj_t.columns)
print('---------------------------------------------------------------------------------')
print('Numeric type columns:\n',num_t.columns)
```

    Object type columns:
     Index(['f'], dtype='object')
    ---------------------------------------------------------------------------------
    Numeric type columns:
     Index(['\ta', '\tb', '\tc', '\td', 'g'], dtype='object')



```python
index_t = train.index
dummy_t = pd.get_dummies(obj_t, drop_first=True) #첫번째 값을 기준으로 T/F으로 나눔
dummy_t.index = index_t
dummy_t.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f_x</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>0</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>0</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0</td>
    </tr>
  </tbody>
</table>





```python
train.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>\ta</th>
      <th>\tb</th>
      <th>\tc</th>
      <th>\td</th>
      <th>f</th>
      <th>g</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1.00</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>2.00</td>
      <td>x</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>-1.00</td>
      <td>NaN</td>
      <td>0.9</td>
      <td>45.00</td>
      <td>o</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>5.00</td>
      <td>7.0</td>
      <td>78.0</td>
      <td>-35.00</td>
      <td>o</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>2.00</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>1.00</td>
      <td>o</td>
      <td>-35.00</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0.22</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.84</td>
      <td>o</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>





```python
dummy_t.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f_x</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>0</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>0</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer()
```


```python
imp_mean = SimpleImputer(missing_values =np.nan, strategy= 'mean')
imp_mean.fit(num_t)
```


    SimpleImputer()






```python
train.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>\ta</th>
      <th>\tb</th>
      <th>\tc</th>
      <th>\td</th>
      <th>f</th>
      <th>g</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1.00</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>2.00</td>
      <td>x</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>-1.00</td>
      <td>NaN</td>
      <td>0.9</td>
      <td>45.00</td>
      <td>o</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>5.00</td>
      <td>7.0</td>
      <td>78.0</td>
      <td>-35.00</td>
      <td>o</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>2.00</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>1.00</td>
      <td>o</td>
      <td>-35.00</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0.22</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.84</td>
      <td>o</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
num_t.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>\ta</th>
      <th>\tb</th>
      <th>\tc</th>
      <th>\td</th>
      <th>g</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1.00</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>2.00</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>-1.00</td>
      <td>NaN</td>
      <td>0.9</td>
      <td>45.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>5.00</td>
      <td>7.0</td>
      <td>78.0</td>
      <td>-35.00</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>2.00</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>1.00</td>
      <td>-35.00</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0.22</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.84</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>





```python
imp_mean.transform(num_t)
```




    array([[  1.        ,   2.        ,  -3.        ,   2.        ,
              0.84      ],
           [ -1.        ,   2.6       ,   0.9       ,  45.        ,
              5.        ],
           [  5.        ,   7.        ,  78.        , -35.        ,
              0.51      ],
           [  2.        ,   2.        ,   7.        ,   1.        ,
            -35.        ],
           [  0.22      ,   0.        ,  19.65555556,   0.84      ,
              1.        ],
           [  2.16      ,   1.        ,   1.        ,   5.        ,
              0.84      ],
           [  5.        ,   4.        ,   7.        ,   0.51      ,
              0.        ],
           [  5.        ,   7.        ,  78.        , -35.        ,
              1.        ],
           [  2.        ,   2.        ,   7.        ,   1.        ,
              4.        ],
           [  0.22      ,   0.        ,  19.65555556,   0.84      ,
              7.        ],
           [  2.16      ,   1.        ,   1.        ,   5.        ,
              2.        ]])




```python
num_t.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>\ta</th>
      <th>\tb</th>
      <th>\tc</th>
      <th>\td</th>
      <th>g</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aa</th>
      <td>1.00</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>2.00</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>bb</th>
      <td>-1.00</td>
      <td>NaN</td>
      <td>0.9</td>
      <td>45.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>cc</th>
      <td>5.00</td>
      <td>7.0</td>
      <td>78.0</td>
      <td>-35.00</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>dd</th>
      <td>2.00</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>1.00</td>
      <td>-35.00</td>
    </tr>
    <tr>
      <th>ee</th>
      <td>0.22</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.84</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
