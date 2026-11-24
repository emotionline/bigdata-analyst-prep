# 120
# 'motion_'으로 시작하는 각 열에서 pose=0과 pose=1 그룹의 중앙값 차이 절댓값을 구하세요.
# 차이가 최댓값인 열의 이름을 사전순 오름차순으로 정렬해 두 번째 열 이름을 출력하세요.

import pandas as pd
df = pd.read_csv("/data/d82f080c.csv")

cols = [col for col in df.columns if col.startswith('motion_')]

# print(df.info())
cond0 = df['pose'] == 0
cond1 = df['pose'] == 1

pose0 = df[cond0][cols].median()
pose1 = df[cond1][cols].median()

answer = abs(pose0 - pose1).sort_values(ascending=False).reset_index(name='diff')
# print(answer)

cond2 = answer['diff'] == answer['diff'].max()
# print(cond2.sum())
result = answer[cond2]['index'].sort_values(ascending=True)
print(result.iloc[1])
