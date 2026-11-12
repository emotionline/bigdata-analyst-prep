# 76
# model(차종)별 행 수를 구하고, 행 수가 많은 상위 3개 차종의 행만 선택하세요.
# 선택한 데이터에서 model별 price(가격) 평균을 구하고 model 문자열의 사전순 오름차순으로 정렬하세요.
# 두 번째 차종의 price 평균을 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv("/data/6b1f0398.csv")

# print(df.columns)
top_3_columns = df['model'].value_counts().head(3).index
sub = df[df['model'].isin(top_3_columns)]

filtered_df = sub.groupby('model')['price'].mean().sort_index( ascending=True)

print(round(filtered_df.iloc[1], 3))

# 77
# Outcome(당뇨 여부, 1: 있음, 0: 없음)별로 각 숫자형 열의 평균을 구하세요.
# BloodPressure(혈압) 열에서 Outcome=1의 평균에서 Outcome=0의 평균을 뺀 값을 구하세요.
# 결과를 소수점 셋째 자리까지 반올림하여 출력하세요.

import pandas as pd
df = pd.read_csv("/data/d1528163.csv")

num_cols = df.select_dtypes(include='number').columns

filtered_df = df.groupby('Outcome')[num_cols].mean()
answer = filtered_df['BloodPressure']
print(round(answer.iloc[1] - answer.iloc[0], 3))

# 78
# Player(선수명)를 공백으로 나눈 첫 단어를 소문자로 바꾸어 first_name으로 사용하세요.
# first_name별 행 수를 구하고, 이 중 가장 큰 행 수를 출력하세요. 이름 자체는 출력하지 않습니다.

import pandas as pd
df = pd.read_csv("/data/3b431ce3.csv",encoding='latin',sep=';')

df['Player'] = df['Player'].str.casefold()

df['first_name'] = df['Player'].str.split(' ').str[0]
answer = df['first_name']
print(answer.value_counts().iloc[0])

# why1 = df['first_name'].idxmax()
# why2 = df['first_name'].max()

# 🦀 print(why1) 🦀 1. 알파벳 순서 상 가장 마지막에 있는 행 번호(인덱스)
# 🦀 print(why2) 🦀 2. 알파벳 순서 상 가장 마지막에 있는 값(문자열 자체)

# 79
# Tm(팀 코드)별 Age(나이) 평균을 구하세요.
# 평균 나이가 가장 낮은 팀의 Tm 값을 출력하세요.

import pandas as pd
df = pd.read_csv("/data/70b597ce.csv",encoding='latin',sep=';')

answer = df.groupby('Tm')['Age'].mean().idxmin()
print(answer)

# 80
# Pos(포지션)별 MP(출전 시간) 평균을 구하고, Pos 문자열의 사전순 오름차순으로 정렬하세요.
# 세 번째 포지션의 MP 평균을 소수점 셋째 자리까지 반올림하여 출력하세요. 평균값으로 정렬하지 않습니다.

import pandas as pd
df = pd.read_csv("/data/ad73cc23.csv",encoding='latin',sep=';')

answer = df.groupby('Pos')['MP'].mean().sort_index(ascending=True)
print(round(answer.iloc[2], 3))

# 81
# view_count(조회 수)가 가장 큰 행의 channelTitle(채널명)을 출력하세요.
# view_count 최댓값은 한 행만 존재한다고 가정합니다.

data_path = '/data/48bd152a.csv'

import pandas as pd
df = pd.read_csv(data_path)

answer = df['view_count'].max()
cond = df['view_count'] == answer
print(df[cond]['channelTitle'].iloc[0])

# 82
# 싫어요 수(dislikes)가 좋아요 수(likes)보다 많은 영상의 행만 선택하세요.
# 선택한 행에서 같은 channelTitle이 반복되면 처음 나온 값만 남기세요. 원본 순서는 유지하세요.
# 중복 제거 결과에서 두 번째 channelTitle을 출력하세요.

import pandas as pd
df = pd.read_csv("/data/89519fe7.csv")

cond = df['dislikes'] > df['likes']
df = df[cond]

df = df.drop_duplicates(subset=['channelTitle'], keep='first')
print(df['channelTitle'].iloc[1])

# 83
# channelId는 채널을 구분하는 고유 번호입니다.
# 같은 channelId에 서로 다른 channelTitle이 2개 이상 기록된 채널의 수를 출력하세요.

import pandas as pd
df = pd.read_csv("/data/8104d5a2.csv")

cond = df.groupby('channelId')['channelTitle'].nunique() >= 2
print(sum(cond))

# 84
# 1. trending_date2를 날짜로 바꾸고 일요일 행만 선택하세요.
# 2. categoryId(카테고리 ID)별 likes(좋아요 수) 중앙값, view_count(조회 수) 평균, 행 수를 구하세요.
# 3. 전체 일요일 집계에서 좋아요 중앙값들의 중앙값과 행 수의 평균을 구하세요.
# 4. 좋아요 중앙값과 행 수가 각각 3번 기준 이상인 카테고리만 남기세요.
# 5. 조회 수 평균 내림차순, categoryId 오름차순으로 정렬해 첫 categoryId를 출력하세요.

import pandas as pd
df = pd.read_csv('/data/64c6c650.csv')

df['trending_date2'] = pd.to_datetime(df['trending_date2'])
df['day_name'] = df['trending_date2'].dt.day_name()

cond1 = df['day_name'] == 'Sunday'
df = df[cond1]

result = df.groupby('categoryId').agg(
    likes_median = ('likes', 'median'),
    view_count_mean = ('view_count', 'mean'),
    categoryId_count = ('categoryId', 'count')
)

median = result['likes_median'].median()
mean = result['categoryId_count'].mean()

cond2 = result['likes_median'] >= median
cond3 = result['categoryId_count'] >= mean
result = result[cond2 & cond3].sort_values(by=['view_count_mean', 'categoryId'], ascending=[False, True])
print(result.index[0])

# 85
# view_count(조회 수)가 0이 아닌 행에서 comment_count(댓글 수)를 view_count로 나눈 비율을 구하세요.
# 계산한 비율이 결측인 행은 제외하고, 비율이 가장 큰 행의 title(영상 제목)을 출력하세요.

import pandas as pd
df = pd.read_csv("/data/32a20d6e.csv")

cond1 = df['view_count'] != 0
df = df[cond1]

# print(df)

df['ratio'] = df['comment_count'] / df['view_count']
df = df.dropna(subset=['ratio'])
answer = df['ratio'].idxmax()
print(df.loc[answer, 'title'])

# 86
# view_count(조회 수)가 0이 아닌 행에서 comment_count(댓글 수)를 view_count로 나눈 비율을 구하세요.
# 비율이 0인 행은 제외하고, 비율 오름차순, title(영상 제목) 오름차순으로 정렬하세요.
# 첫 번째 행의 title을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/8e655344.csv')

cond1 = df['view_count'] != 0
df = df[cond1]

df['ratio'] = df['comment_count'] / df['view_count']

cond2 = df['ratio'] != 0
df = df[cond2]

df = df.sort_values(by=['ratio', 'title'], ascending=[True, True])
print(df['title'].iloc[0])

# 🦀 1. 정렬(sort_values)이 끝난 상태에서 "맨 위 첫 번째 행의 특정 열"을 뽑을 때는 라벨(loc)이 아니라 위치(iloc)를 쓰거나 인덱스를 초기화해야 합니다.
