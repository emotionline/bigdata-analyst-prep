# 23

# 회귀식: purchased ~ age + income + visits + premium + ad_exposure + C(channel)
# 상수항을 포함한 statsmodels 로지스틱 회귀를 학습하고, 식에 쓰는 열의 결측 행은 제외하세요.
# purchased=1은 구매, 0은 미구매입니다. 별도 검증 분할 없이 학습에 사용한 고객 전체를 평가하세요.
# 반올림 전 구매 확률이 0.55 이상이면 1, 아니면 0으로 분류하세요.
# 실제값과 예측값이 모두 1인 고객 수(정수), 전체 정확도(round(..., 3))를 각각 한 줄씩 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_campaign.csv')

cols = ['purchased', 'age', 'income', 'visits', 'premium', 'ad_exposure', 'channel']
df = df.dropna(subset=cols)

import statsmodels.formula.api as smf
formula = "purchased ~ age + income + visits + premium + ad_exposure + C(channel)"
model = smf.logit(formula=formula, data=df).fit(disp=False)
df['prob'] = model.predict(df)
cond1 = (df['prob'] >= 0.55) & (df['purchased'] == 1)
cond2 = (df['prob'] < 0.55) & (df['purchased'] == 0)
answer = df[cond1 | cond2]
print(sum(cond1), round(len(answer)/len(df), 3), sep='\n')

# ValueError: shapes (360,9) and (360,10) not aligned: 9 (dim 1) != 360 (dim 0)

# 24
# treatment가 'drug'인 약물군만 선택하세요. response는 1(치료 반응 있음), 0(없음)입니다.
# 약물군 안에서 response=1인 환자 수(count)와 response가 결측이 아닌 환자 수(nobs)를 구하세요.
# proportion_confint(alpha=0.05, method='wilson')로 반응률의 Wilson 95% 신뢰구간을 구하세요.
# 하한, 상한을 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_clinic.csv')

import statsmodels.stats.proportion as ssp

cond = df['treatment'] == 'drug'
df = df[cond]

cond1 = df['response'] == 1
count = cond1.sum()
nobs = len(df.dropna(subset='response'))

lower, upper = ssp.proportion_confint(count, nobs, alpha=0.05, method='wilson')
print(round(lower, 3), round(upper, 3), sep='\n')

# TypeError: proportion_confint() missing 2 required positional arguments: 'count' and 'nobs'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ValueError: could not convert string to float:

# 25
# 나이(age)가 50 이상인 비흡연자(smoker=0) 중 두 혈압 값이 모두 있는 행만 사용하세요.
# 감소량 = bp_before - bp_after로 구하고, 모집단 평균이 5보다 큰지 일표본 t-검정하세요.
# popmean=5, alternative='greater'를 사용하고 감소량 평균, t통계량, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

# print(len(df))

cond1 = df['age'] >= 50
cond2 = df['smoker'] == 0
df = df[cond1 & cond2]

# print(len(df))
# print(df.columns)

df = df.dropna(subset=['bp_before', 'bp_after'])
df['diff'] = df['bp_before'] - df['bp_after']

mean = df['diff'].mean()

from scipy.stats import ttest_1samp

t_stat, p_val = ttest_1samp(df['diff'], popmean=5, alternative='greater')
print(round(mean, 3), round(t_stat, 3), round(p_val, 3), sep="\n")

# 26
# program A, C는 서로 다른 참가자입니다. 두 혈압 값이 모두 있는 행에서 감소량 = bp_before - bp_after를 구하세요.
# A, C 순서로 Welch 독립표본 양측 t-검정하세요.
# A 평균 - C 평균, 그 차이의 95% 신뢰구간 하한·상한을 각각 한 줄씩 round(..., 3)으로 출력하세요.
# 구간은 검정 결과의 confidence_interval(confidence_level=0.95)로 구할 수 있습니다.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

from scipy.stats import ttest_ind

df = df.dropna(subset=['bp_before', 'bp_after'])
df['diff'] = df['bp_before'] - df['bp_after']

A_cond = df["program"] == 'A'
C_cond = df["program"] == 'C'

A_df = df[A_cond]
C_df = df[C_cond]

res = ttest_ind(A_df['diff'], C_df['diff'], equal_var=False, alternative='two-sided')
ci = res.confidence_interval(confidence_level=0.95)

# print(ci)
mean = A_df['diff'].mean() - C_df['diff'].mean()
print(round(mean, 3), round(ci.low, 3), round(ci.high, 3), sep="\n")

# 🦀 ttest_ind
# 🦀 equal_var = True : 두 집단의 분산이 같다. Student's t-test(표준 독립표본 t-검정)
# 🦀 equal_var = False : 두 집단의 분산이 다르다. Welch's t-test(웰치 t-검정)

# 27
# productivity를 종속변수, experience·training_hours·overtime·project_count·team_size를 독립변수로 사용하세요.
# 여섯 열의 결측 행을 제외하고 상수항을 포함한 OLS 회귀를 학습하세요.
# 최초 모형에서 반올림 전 p-value < 0.05인 독립변수를 한 번만 골라 다시 학습하세요. 상수항은 항상 포함하며 선택 대상이 아닙니다.
# 선택된 독립변수 수(정수), 새 모형의 수정 결정계수(adj. R-squared), 모형 전체 F검정 p-value를 각각 한 줄씩 출력하세요.
# 개수 외 수치는 round(..., 3)으로 반올림하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_productivity.csv')

import statsmodels.formula.api as smf
formula = "productivity ~ experience + training_hours + overtime + project_count + team_size"

cols = ['productivity', 'experience', 'training_hours', 'overtime', 'project_count', 'team_size']

df = df.dropna(subset=cols)

model = smf.ols(formula=formula, data=df).fit()
pvalue = model.pvalues
# print(pvalue)

cond = pvalue < 0.05
cols = pvalue[cond]
# print(cols)

formula = "productivity ~ experience + training_hours + overtime + project_count"
final_model = smf.ols(formula=formula, data=df).fit()
# print(final_model.summary())
print(len(final_model.params)-1, round(final_model.rsquared_adj, 3), round(final_model.f_pvalue, 3), sep='\n')

# 🦀 model.params : 회귀계수
# 🦀 model.pvalues : 유의확률
# 🦀 다른 모든 조건을 똑같이 고정해 두었을 때, 해당 독립변수가 1단위 증가할 때마다 종속변수가 변하는 양(순수 기울기)
# 🦀 변수 간의 선형적인 연관성(조건부 기댓값의 변화)

# 28
# 회귀식: purchased ~ age + income + visits + premium + ad_exposure + C(channel)
# df 전체로 상수항을 포함한 로지스틱 회귀를 학습하세요. purchased는 구매 1, 미구매 0입니다.
# 다른 조건이 같을 때 방문 횟수(visits)가 3회 늘어나는 경우의 구매 오즈비를 구하세요. 구매 확률의 차이가 아닙니다.
# 학습에 쓴 df의 각 행에 대해 구매 예측 확률을 구하고, 반올림 전 확률이 0.7 이상인 행 수를 세세요.
# 구매 예측 확률이 가장 높은 행의 customer_id를 구하세요. 동률이면 customer_id 오름차순으로 첫 고객을 선택하세요.
# 오즈비(round(..., 3)), 고객 수(정수), customer_id(문자열)를 각각 한 줄씩 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_campaign.csv')

import statsmodels.formula.api as smf

formula = "purchased ~ age + income + visits + premium + ad_exposure + C(channel)"
model = smf.logit(formula=formula, data=df).fit(disp=False)
import numpy as np
ratio = np.exp(model.params['visits']) ** 3
print(round(ratio, 3))

df['prob'] = model.predict(df)
cond = df['prob'] >= 0.7
print(cond.sum())
result = df[cond].sort_values(['prob', 'customer_id'], ascending=[False, True])['customer_id'].iloc[0]
print(result)

# 29
# program이 'B'이고 나이(age)가 50 이상인 참가자 중, bp_before(전 혈압)·bp_after(후 혈압)가 모두 결측이 아닌 행만 사용하세요.
# 같은 참가자의 혈압 감소량(bp_before - bp_after)을 소수 둘째 자리까지 반올림하세요.
# 감소량 분포가 대칭이라고 가정하고, 그 중심(중앙값)이 8보다 큰지 Wilcoxon 부호순위 검정하세요.
# 검정에는 감소량에서 8을 뺀 값을 소수 둘째 자리까지 반올림해 넣으세요.
# zero_method='wilcox', correction=False, alternative='greater', method='approx'를 사용하세요.
# 참가자 수(정수), 통계량, p-value, 기각 여부를 각각 한 줄씩 출력하세요.
# 참가자 수에는 감소량이 8인 사람도 포함합니다. 검정에서 0인 차이를 제외하는 것과 구분하세요.
# 수치는 round(..., 4), 기각 여부는 반올림 전 p-value < 0.05의 True/False로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

cond1 = df['program'] == 'B'
cond2 = df['age'] >= 50

df = df[cond1 & cond2].dropna(subset=['bp_before', 'bp_after'])
df['diff'] = round(df['bp_before'] - df['bp_after'], 2)
diff = (df['diff'] - 8).round(2)

from scipy.stats import wilcoxon

stats, p_val = wilcoxon(
    diff,
    zero_method='wilcox',
    correction=False,
    alternative='greater',
    method ='approx'
)

answer = True if p_val < 0.05 else False

print(len(diff), stats, round(p_val, 4), answer, sep='\n')

# 30
# 비흡연자(smoker=0)의 program A, B 중 recovery_days가 있는 행만 사용하세요. 서로 다른 참가자 집단입니다.
# A의 회복일수가 B보다 큰 경향이 있는지 Mann-Whitney U 검정하세요(A, B 순서).
# alternative='greater', method='asymptotic', use_continuity=True를 사용하세요.
# A의 U통계량, p-value, 기각 여부를 각각 한 줄씩 출력하세요.
# 수치는 round(..., 4), 기각 여부는 반올림 전 p-value < 0.05의 True/False로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

cond = df['smoker'] == 0
df = df[cond]

cond2 = df['program'].isin(['A', 'B'])
df = df[cond2].dropna(subset=['recovery_days'])

# print(df['program'].value_counts())

cond_A = df['program'] == "A" 
cond_B = df['program'] == "B"

df_A = df[cond_A]
df_B = df[cond_B]

from scipy.stats import mannwhitneyu
stats, p_val = mannwhitneyu(df_A['recovery_days'], df_B['recovery_days'], alternative='greater', method='asymptotic', use_continuity=True)

answer = True if p_val < 0.05 else False
print(stats, round(p_val, 4), answer, sep="\n")

# 31
# 나이(age)가 50 이상이고 운동시간(exercise_minutes, 분)이 있는 참가자만 사용하세요.
# 서로 다른 참가자인 program A, B, C의 운동시간 분포를 stats.kruskal로 비교하세요(A, B, C 순서).
# H통계량, p-value, 기각 여부를 각각 한 줄씩 출력하세요.
# 수치는 round(..., 4), 기각 여부는 반올림 전 p-value < 0.05의 True/False로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

cond = df['age'] >= 50
df = df[cond].dropna(subset=['exercise_minutes'])

from scipy.stats import kruskal

A = df['program'] == "A"
B = df['program'] == "B"
C = df['program'] == "C"

stats, p_val = kruskal(df[A]['exercise_minutes'], df[B]['exercise_minutes'], df[C]['exercise_minutes'])
answer = True if p_val < 0.05 else False
print(round(stats, 4), round(p_val, 4), answer, sep='\n')

# 32
# program(프로그램) 열의 A·B·C 집단을 비교합니다. recovery_days(회복까지 걸린 일수)가 결측인 행은 제외하세요.
# recovery_days를 비교할 값으로 사용해 A-B, A-C, B-C를 각각 Mann-Whitney U 양측 검정하세요.
# method='asymptotic', use_continuity=True를 사용하세요.
# 각 p-value에 3을 곱하고 최대 1로 제한하는 Bonferroni 보정을 적용하세요.
# 보정 p-value를 A-B, A-C, B-C 순서로 각각 한 줄씩 round(..., 4)로 출력하세요.
# 마지막 줄에 반올림 전 보정 p-value < 0.05인 쌍의 수를 정수로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

# print(df.info())

df = df.dropna(subset=['recovery_days'])
A = df['program'] == 'A'
B = df['program'] == 'B'
C = df['program'] == 'C'

from scipy.stats import mannwhitneyu

stats1, p_val1 = mannwhitneyu(df[A]['recovery_days'], df[B]['recovery_days'], method='asymptotic', use_continuity=True)
stats2, p_val2 = mannwhitneyu(df[A]['recovery_days'], df[C]['recovery_days'], method='asymptotic', use_continuity=True)
stats3, p_val3 = mannwhitneyu(df[B]['recovery_days'], df[C]['recovery_days'], method='asymptotic', use_continuity=True)

p_val1 = 3 * p_val1
p_val2 = 3 * p_val2
p_val3 = 3 * p_val3

import numpy as np

adj_arr = [p_val1, p_val2, p_val3]
ans_arr = np.minimum(adj_arr, 1)
print(round(p_val1, 4), round(p_val2, 4), round(p_val3, 4), sep='\n')
print(sum(ans_arr < 0.05))

# TypeError: ufunc 'isnan' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

# 33
# program이 'B'인 비흡연자(smoker=0) 중 exercise_minutes(운동시간)와 recovery_days(회복일수)가 모두 있는 행만 사용하세요.
# 운동시간이 길수록 회복일수가 짧아지는 경향을 Spearman 검정하세요(운동시간, 회복일수 순서, alternative='less').
# 상관계수, p-value, 기각 여부를 각각 한 줄씩 출력하세요.
# 수치는 round(..., 4), 기각 여부는 반올림 전 p-value < 0.05의 True/False로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

cond1 = df['program'] == 'B'
cond2 = df['smoker'] == 0

df = df[cond1 & cond2].dropna(subset=['exercise_minutes', 'recovery_days'])

from scipy.stats import spearmanr
stats, p_val = spearmanr(df['exercise_minutes'], df['recovery_days'], alternative='less')
answer = True if p_val < 0.05 else False
print(round(stats, 4), round(p_val, 4), answer, sep='\n')


# import numpy as np
# from scipy.stats import chi2_contingency

# obs = np.array([[30, 70],
#                [50, 50]])

# stats, p_val, dof, expected = chi2_contingency(obs, correction=False)
# print(expected)

# # TypeError: Field elements must be 2- or 3-tuples, got '50'

# 34
# 나이(age)가 50 이상인 비흡연자(smoker=0) 중 bp_before·bp_after가 모두 있는 행만 사용하세요.
# 감소량(bp_before - bp_after)을 소수 둘째 자리까지 반올림하고, 정확히 8인 사람은 제외하세요.
# 남은 인원 수를 n, 감소량이 8보다 큰 인원 수를 k로 하여 그 비율이 0.5를 넘는지 부호검정하세요.
# stats.binomtest(k, n, p=0.5, alternative='greater')를 사용하세요.
# n, k(정수), p-value, 기각 여부를 각각 한 줄씩 출력하세요.
# 수치는 round(..., 4), 기각 여부는 반올림 전 p-value < 0.05의 True/False로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

cond1 = df['age'] >= 50
cond2 = df['smoker'] == 0
df = df[cond1 & cond2].dropna(subset=['bp_before', 'bp_after'])
df['diff'] = (df['bp_before'] - df['bp_after']).round(2)

cond3 = df['diff'] != 8
df = df[cond3]

n = len(df)
k = sum(df['diff'] > 8)

from scipy.stats import binomtest
res = binomtest(k, n, p=0.5, alternative='greater')
answer = True if res.pvalue < 0.05 else False

print(n, k, round(res.pvalue, 4), answer, sep='\n')

# TypeError: cannot unpack non-iterable BinomTestResult object

# 35
# 약물군(treatment=drug) 중 response가 1(반응 있음) 또는 0(없음)인 행만 사용하세요.
# 반응 인원 k, 전체 인원 n으로 stats.binomtest(k, n, p=0.6, alternative='two-sided')를 수행해 반응률이 60%와 다른지 검정하세요.
# 반응률 k/n(0~1), p-value, 기각 여부를 각각 한 줄씩 출력하세요.
# 수치는 round(..., 4), 기각 여부는 반올림 전 p-value < 0.05의 True/False로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_clinic.csv')

cond1 = df['treatment'] == 'drug'
cond2 = df['response'].isin([0, 1])

df = df[cond1 & cond2]

n = len(df)
k = sum(df['response'] == 1)

from scipy.stats import binomtest
res = binomtest(k, n, p=0.6, alternative='two-sided')
answer = True if res.pvalue < 0.05 else False
print(round(k/n, 4), round(res.pvalue, 4), answer, sep='\n')

# print(df['treatment'].value_counts())
# print(df['response'].value_counts())

# 36
# device가 standard, plus, premium인 행만 사용하고, 이 순서로 관측도수를 세세요.
# 전체 인원 수에 계획 비율 0.4, 0.4, 0.2를 각각 곱해 기대도수를 구하세요.
# 실제 비율이 계획과 같은지 stats.chisquare(f_obs=관측도수, f_exp=기대도수)로 적합도 검정하세요.
# 카이제곱 통계량, p-value, 기각 여부를 각각 한 줄씩 출력하세요.
# 수치는 round(..., 4), 기각 여부는 반올림 전 p-value < 0.05의 True/False로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_clinic.csv')

A = len(df[df['device'] == 'standard'])
B = len(df[df['device'] == 'plus'])
C = len(df[df['device'] == 'premium'])

total = len(df)

from scipy.stats import chisquare
stats, p_val = chisquare([A, B, C], [0.4*total, 0.4*total, 0.2*total])
answer = True if p_val < 0.05 else False
print(round(stats, 4), round(p_val, 4), answer, sep='\n')

# ValueError: Array shapes are incompatible for broadcasting.
# ValueError: For each axis slice, the sum of the observed frequencies must agree with the sum of the expected frequencies to a relative tolerance of 1.4901161193847656e-08, but the percent differences are:
