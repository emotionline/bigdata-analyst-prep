# 69
# time(측정 시각)을 기준으로 6월, 7월, 8월의 행만 선택하세요.
# 그중 이화동기온이 수영동기온보다 큰 행이 몇 개인지 출력하세요. 서로 다른 시각이 아닌 행 수를 셉니다.

import pandas as pd
df = pd.read_csv("/data/c3a1414e.csv")

df['time'] = pd.to_datetime(df['time'])
df['month'] = df['time'].dt.month

select_cols = [6, 7, 8]
cond = df['month'].isin(select_cols)

df = df[cond]

cond2 = df['이화동기온'] > df['수영동기온']
print(cond2.sum())

# 70
# Gender(성별)가 'Male'(남성)인 고객만 선택하세요. Exited는 1이면 이탈, 0이면 유지입니다.
# 선택한 고객의 Geography(국가)별 Exited 합계를 구하고, 그 합계 중 가장 큰 값을 출력하세요.

import pandas as pd
df = pd.read_csv("/data/ef968029.csv")

cond = df['Gender'] == 'Male'
df = df[cond]

answer = df.groupby('Geography')['Exited'].sum().max()
print(answer)

# 71
# WHtR은 허리둘레를 '신장(5Cm단위)'로 나눈 값입니다. 두 열 모두 cm 단위 값을 사용하세요.
# 이 문제에서는 WHtR이 0.58 이상인 행만 선택하세요. 성별코드의 'M'은 남성, 'F'는 여성입니다.
# 선택한 행의 남성 수를 여성 수로 나눈 비율을 소수점 셋째 자리까지 반올림하여 출력하세요. 백분율로 바꾸지 않습니다.

import pandas as pd
df = pd.read_csv("/data/eb00e9e0.csv")
# print(df.columns)
# print(df.head(5))
df['WHtR'] = df['허리둘레'] / df['신장(5Cm단위)']
cond = df['WHtR'] >= 0.58
df = df[cond]

answer = df.groupby('성별코드').size()
print(round((answer["M"]/answer["F"]), 3))

# 72
# Gender(성별)와 Vehicle_Age(차량 연령 구간)별로 Annual_Premium(연 보험료) 평균을 구하세요.
# Vehicle_Age를 행, Gender를 열로 하는 피벗 테이블을 만들고, Vehicle_Age 문자열의 사전순 오름차순으로 정렬하세요.
# 두 번째 행의 'Female'(여성) 평균값을 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv("/data/9b3251cb.csv")
# print(df.columns)

pivot = pd.pivot_table(
    df,
    index = 'Vehicle_Age',
    columns = 'Gender',
    values = 'Annual_Premium',
    aggfunc = 'mean'
).sort_index(ascending=True)

print(round(pivot['Female'].iloc[1], 3))

# 🦀 sort_index에 대한 이해가 중요한 문제였다.

# 73
# 'Arrival Delay in Minutes'(도착 지연 시간)가 결측인 행만 선택하세요.
# Class(좌석 등급)를 행, satisfaction(만족도)을 열, 각 조합의 행 수를 값으로 하는 피벗 테이블을 만드세요.
# Class 문자열의 사전순 오름차순으로 정렬한 뒤, 두 번째 행의 'neutral or dissatisfied'(보통 또는 불만족) 행 수를 출력하세요.

import pandas as pd
df = pd.read_csv("/data/308ff749.csv")

import numpy as np
# print(df['Arrival Delay in Minutes'].value_counts(dropna=False))

cond = df['Arrival Delay in Minutes'].isna()
df = df[cond]

pivot = pd.pivot_table(
    df,
    index='Class',
    columns='satisfaction',
    aggfunc = 'size'
).sort_index()

print(pivot['neutral or dissatisfied'].iloc[1])

# 🦀 1. 열을 Series로 분리 후, 행 번호 선택 : pivot[?].iloc[?]
# 🦀 2. [행 라벨, 열 라벨] : loc, 끝 라벨 포함 X
# 🦀 3. [행 번호, 열 번호] : iloc, 끝 라벨 포함 O
# 🦀 4. 불가능 (KeyError) : pivot[?, ?] : pandas가 (?, ?) 튜플 이름의 단일 컬럼을 찾으려고 해서 안 됨.
# 🦀 5. 체인 인덱싱 : pivot[열][행] (O), pivot[행][열] (X) 

# 74
# ph 열의 결측값을 제외하고, 남은 ph 값의 25백분위수(quantile(0.25))를 구하세요.
# ph가 그 값 이하인 모든 행의 ph 평균을 구하세요. 경계값과 같은 행도 모두 포함합니다.
# 결과를 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv("/data/1ae0079b.csv")
# print(df.columns)

df = df.dropna(subset='ph')
quantile = df['ph'].quantile(0.25)
cond = df['ph'] <= quantile
df = df[cond]

print(round(df['ph'].mean(), 3))

# 75
# 'Serial No.'(일련번호)와 'Chance of Admit'(합격 확률)을 제외한 각 열에 대해 'Chance of Admit'과의 피어슨 상관계수를 구하세요.
# 상관계수의 절댓값이 가장 큰 열의 이름을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type1-practice-admission.csv')

# print(df.columns)

df = df.drop(columns=['Serial No.'])
# print(df.columns)

corr = df.corr()['Chance of Admit']
corr = corr.drop('Chance of Admit')
print(corr.idxmax())
