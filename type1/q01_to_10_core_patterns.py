# 1
# 데이터프레임의 전체 행 수를 출력하세요.

import pandas as pd
df = pd.read_csv('/data/a1f3c920.csv')
print(df.shape[0])

# 2
# 이화동기온 열의 최댓값을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/b7d2e416.csv')
print(df['이화동기온'].max())

# 3
# Geography(국가) 열의 값이 'Germany'(독일)인 고객 수를 출력하세요.

import pandas as pd
df = pd.read_csv('/data/c4a8f731.csv')
cond = df['Geography'] == 'Germany'
print(cond.sum())

# 4
# Volume(거래량) 열의 최댓값을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/d9c0b524.csv')
print(df['Volume'].max())

# 5
# 측정회원성별 열에서 서로 다른 값이 몇 개인지 출력하세요.

import pandas as pd
df = pd.read_csv('/data/e2b6a803.csv')
print(df['측정회원성별'].nunique())

# 6
# 흡연상태가 1인 행의 개수를 출력하세요.

import pandas as pd
df = pd.read_csv('/data/f5e1d672.csv')
cond = df['흡연상태'] == 1
print(cond.sum())

# 7
# videoname별 데이터 개수를 구하라. 데이터 개수가 두 번째로 많은 videoname의 개수를 정수 하나로 출력하라.

import pandas as pd

channel =pd.read_csv('/data/f264a486.csv')
video =pd.read_csv('/data/d2f0c034.csv')

# 아래에 코드를 작성하세요.

df = video.groupby("videoname").size().sort_values(ascending = False)
print(df.iloc[1])

# 8
# video 데이터에서 videoname(영상명)별로 ct(수집 시각)가 가장 늦은 행을 하나씩 남기세요.
# 남은 각 행에서 dislikecnt(싫어요 수)를 likecnt(좋아요 수)로 나눈 비율을 구하세요.
# 비율이 작은 순서로 정렬한 뒤, 세 번째 행의 videoname을 출력하세요.

import pandas as pd
video =pd.read_csv('/data/2465e82d.csv')

result = video.sort_values(by='ct', ascending=False).drop_duplicates(subset='videoname', keep='last')
result['ratio'] = result['dislikecnt'] / result['likecnt']

answer = result.sort_values(by='ratio', ascending=True)
print(answer['videoname'].iloc[2])

# print(help(pd.DataFrame.drop_duplicates))
# print(help(pd.DataFrame.sort_values))
# print(help(pd.Series.sort_values))

# 9
# 1. Country(국가)마다 Goals(득점 수) 합계와 중복을 뺀 Player(선수명) 개수를 구하세요. 각각 국가별 득점 합계와 선수 수입니다.
# 2. 1번의 국가별 집계표에서 득점 합계의 평균과 선수 수의 중앙값을 구하세요. 각 국가는 한 번씩 반영합니다.
# 3. 득점 합계가 2번에서 구한 평균 이상이고, 선수 수가 2번에서 구한 중앙값 이상인 국가만 남기세요.
# 4. 득점 합계가 큰 순, 선수 수가 많은 순, Country 오름차순으로 정렬해 세 번째 Country를 출력하세요.

import pandas as pd
df = pd.read_csv('/data/18b53b08.csv')

result = df.groupby('Country').agg(
    sum = ('Goals', 'sum'),
    count = ('Player', 'nunique')
)

mean = result['sum'].mean()
median = result['count'].median()

cond1 = result['sum'] >= mean 
cond2 = result['count'] >= median

result = result[cond1 & cond2].reset_index()
answer = result.sort_values(by=['sum', 'count', 'Country'], ascending=[False, False, True])

print(answer['Country'].iloc[2])

# print(result)

# 10
# 2002년도에 출전한 전체 선수 수를 출력하라

import pandas as pd

df= pd.read_csv('/data/2c830abd.csv')

# 아래에 코드를 작성하세요.

# print(df.head(5))

df["2002"] = df["Years"].str.contains("2002")
print(df["2002"].sum())
# df = df[df["2002"] == True]
# print(len(df))
