# 57
# 2018년과 2019년의 행복랭킹이 같은 나라의 수를 출력하세요

import pandas as pd
df = pd.read_csv('/data/95a776f2.csv',encoding='utf-8')

cond = df['년도'].isin([2018, 2019])
filtered_df = df[cond]

pv = filtered_df.pivot(index='나라명', columns='년도', values='행복랭킹')
print((pv[2018]==pv[2019]).sum())

# 58
# 2018년과 2019년 모두 기록이 있는 나라만 사용하세요.
# 각 나라의 행복점수 증가폭을 2019년 점수 - 2018년 점수로 계산하고, 증가폭이 가장 큰 값을 출력하세요
# 소수점이 있는 값은 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv('/data/55d2e889.csv',encoding='utf-8')

cond = df['년도'].isin([2018, 2019])
filtered_df = df[cond]

answer = filtered_df.pivot(index="나라명", columns="년도", values="점수").dropna()
answer['diff'] = answer[2019] - answer[2018]
print(round(answer['diff'].max(), 3))

# 59
# DateTime 컬럼에서 월을 추출해 월별 행 수를 계산하세요.
# 월 오름차순으로 정리한 결과에서 세 번째 월의 행 수를 출력하세요

data_path = '/data/47f808f1.csv'

import pandas as pd
df = pd.read_csv(data_path)

# 60
# print(df.info())
# print(df.isna().sum())

df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Month'] = df['DateTime'].dt.month
answer = df.groupby('Month').size().sort_index(ascending=True)
print(answer.iloc[2])

# 61
# 3월 데이터에서 시간대별 Temperature 평균을 계산하세요.
# 평균 Temperature가 가장 낮은 시간대의 평균값을 출력하세요
# 소수점이 있는 값은 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df= pd.read_csv('/data/17d68735.csv')

df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Month'] = df['DateTime'].dt.month
df['Hour'] = df['DateTime'].dt.hour

cond = df['Month'] == 3
filtered_df = df[cond]
answer = filtered_df.groupby('Hour')['Temperature'].mean().min()
print(round(answer, 3))

# 62
# 컬럼명 'Zone 2  Power Consumption'에는 공백이 2개 있다.
# 1. Zone 1 Power Consumption이 Zone 2  Power Consumption보다 큰 행만 남기세요.
# 2. Zone 1 Power Consumption이 전체 중앙값 이상인 행만 남기세요.
# 3. 두 조건을 모두 만족하는 행의 Humidity 평균을 구하세요.
# 4. 평균을 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv('/data/5dfbbe13.csv')

cond1 = df['Zone 1 Power Consumption'] > df['Zone 2  Power Consumption']
cond2 = df['Zone 1 Power Consumption'] >= df['Zone 1 Power Consumption'].median() 

filtered_df = df[cond1 & cond2]
print(round(filtered_df['Humidity'].mean(), 3))

# 63
# 1. Legendary가 False인 포켓몬만 남기세요.
# 2. Type 1별 Attack 중앙값을 구하세요.
# 3. Attack이 자신의 Type 1 중앙값 이상인 포켓몬만 남기세요.
# 4. 남은 데이터에서 Type 1별 HP 평균과 포켓몬 수를 구하세요.
# 5. 포켓몬 수가 Type 1별 포켓몬 수의 중앙값 이상인 Type 1만 남기세요.
# 6. HP 평균 내림차순으로 정렬한 첫 번째 Type 1을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/21d5d487.csv')

cond1 = df['Legendary'] == False
df = df[cond1]
median = df.groupby('Type 1')['Attack'].transform('median')
cond2 = df['Attack'] >= median

filtered_df = df[cond2]

summary = filtered_df.groupby('Type 1').agg(
    hp_mean = ('HP', 'mean'),
    cnt = ('HP', 'count')
)

cond3 = summary['cnt'] >= summary['cnt'].median()
answer_df = summary[cond3].sort_values('hp_mean', ascending=False)
print(answer_df.index[0])

# 64
# 1. Type 1별 포켓몬 수를 구하세요.
# 2. 포켓몬 수가 가장 많은 Type 1을 찾으세요.
# 3. 선택한 Type 1의 Attack 평균을 Defense 평균으로 나눈 값을 구하세요.
# 4. 결과를 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv('/data/bdfa9f68.csv')

count = df.groupby('Type 1').size()
answer = count.idxmax()

A_mean = df[df['Type 1'] == 'Water']['Attack'].mean()
D_mean = df[df['Type 1'] == 'Water']['Defense'].mean()
answer = A_mean / D_mean
print(round(answer, 3))

# 65
# Legendary가 True인 포켓몬만 사용하세요.
# 이 포켓몬 수가 가장 많은 Generation 값을 출력하세요

import pandas as pd
df = pd.read_csv('/data/8ca2e831.csv')

cond = df['Legendary'] == True
filtered_df = df[cond]

print(filtered_df.groupby('Generation').size().idxmax())

# 66
# 각 Generation에서 Attack이 가장 낮은 3개 행을 선택하세요.
# 선택된 전체 18개 행의 Attack 평균을 구하세요
# 계산 결과는 round(..., 3)으로 반올림해 출력하세요.

import pandas as pd
df = pd.read_csv('/data/328f8425.csv')

result = df.groupby('Generation')['Attack'].nsmallest(3)

print(round(result.mean(), 3))

# 67
# 한 번씩만 등장하는 (Type 1, Type 2) 쌍의 개수를 출력하세요

import pandas as pd
df = pd.read_csv('/data/f7d23065.csv')

counts = df.value_counts(subset=['Type 1', 'Type 2'], dropna=False)
answer = (counts == 1).sum()

print(int(answer))

# 68
# 남성 데이터에서 A등급과 D등급의 체지방률 평균을 각각 구하고, 큰 평균에서 작은 평균을 뺀 차이를 출력하세요
# 소수점이 있는 값은 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv('/data/0aac5aa1.csv')

cond1 = df['측정회원성별'] == "M"
df = df[cond1]

cond2 = df['등급'] == "A"
cond3 = df['등급'] == "D"

A_mean = df[cond2]['체지방율 : %'].mean()
B_mean = df[cond3]['체지방율 : %'].mean()

print(round(abs(A_mean - B_mean), 3))
