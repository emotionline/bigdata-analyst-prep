# 1
# 만족도(wellness_score)의 모집단 평균이 75보다 큰지 일표본 t-검정하세요.
# 결측값을 제외하고 popmean=75, alternative='greater'를 사용하세요.
# t통계량, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

from scipy.stats import ttest_1samp

clean_df = df.dropna(subset='wellness_score')

stats, pvalue = ttest_1samp(clean_df['wellness_score'], popmean=75, alternative='greater')
print(round(stats, 3), round(pvalue, 3))

# 2
# 한 행은 같은 고객의 관리 전(bp_before)·후(bp_after) 혈압입니다. 두 값이 모두 있는 행만 사용하세요.
# 전 혈압이 후 혈압보다 큰지 대응표본 t-검정하세요(전, 후 순서, alternative='greater').
# 감소량(bp_before - bp_after)의 평균, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

from scipy.stats import ttest_rel

diff = df['bp_befor']

stats, pvalue = ttest_rel()

# 3
# 서로 다른 참가자인 program A, C의 관리 후 혈압(bp_after)을 비교하세요. 결측값은 제외하세요.
# A의 평균이 C보다 큰지 Welch t-검정하세요(A, C 순서, equal_var=False, alternative='greater').
# t통계량, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')
# print(df)

from scipy.stats import ttest_ind

df_A = df[df['program'] == 'A']
df_C = df[df['program'] == 'C']

stats, pvalue = ttest_ind(df_A['bp_after'], df_C['bp_after'], equal_var = False, alternative = 'greater', )
print(round(stats, 3), round(pvalue, 3))

# 4
# program A, B, C의 관리 후 혈압(bp_after) 분산이 같은지 Levene 검정하세요(center='median').
# A, B, C 순서로 표본을 넣고 통계량, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

# print(df)

df_A = df[df['program'] == 'A']
df_B = df[df['program'] == 'B']
df_C = df[df['program'] == 'C']

from scipy.stats import levene

stats, pvalue = levene(df_A['bp_after'], df_B['bp_after'], df_C['bp_after'])

print(round(stats, 3), round(pvalue, 3))

# 5
# program A, B, C의 만족도(wellness_score) 평균이 같은지 일원분산분석하세요.
# 집단별 정규성과 등분산을 가정하며, 각 집단의 결측값을 제외하고 A, B, C 순서로 넣으세요.
# F통계량, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

# print(df)

df = df.dropna(subset='wellness_score')

# print(df['program'].unique())

g1 = df[df['program'] == 'A']['wellness_score']
g2 = df[df['program'] == 'B']['wellness_score']
g3 = df[df['program'] == 'C']['wellness_score']

from scipy.stats import f_oneway

stats, pvalue = f_oneway(g1, g2, g3)
print(round(stats, 3), round(pvalue, 3))

# 6
# 서로 다른 참가자인 program A, B, C의 회복일수(recovery_days) 분포를 Kruskal-Wallis 검정으로 비교하세요.
# 정규성을 가정하지 않으며, 각 집단의 결측값을 제외하세요.
# 통계량, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

from scipy.stats import kruskal

df = df.dropna(subset='recovery_days')

g1 = df[df['program'] == 'A']['recovery_days']
g2 = df[df['program'] == 'B']['recovery_days']
g3 = df[df['program'] == 'C']['recovery_days']

stats, pvalue = kruskal(g1, g2, g3)
print(round(stats, 3), round(pvalue, 3))

# 7
# 비흡연자(smoker=0)의 cholesterol이 흡연자(smoker=1)보다 낮은지 Mann-Whitney U 검정하세요.
# cholesterol 결측값을 제외하고 비흡연자, 흡연자 순서로 표본을 넣으세요.
# alternative='less', method='auto', use_continuity=True를 사용하세요.
# U통계량, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

df = df.dropna(subset=['smoker', 'cholesterol'])

g1 = df[df['smoker'] == 0]['cholesterol']
g2 = df[df['smoker'] == 1]['cholesterol']

from scipy.stats import mannwhitneyu

stats, pvalue = mannwhitneyu(g1, g2, alternative='less')
print(round(stats, 3), round(pvalue, 3))

# 8
# 파일 원래 순서의 앞 80행에서 혈압 감소량(bp_before - bp_after)을 구하세요. 두 혈압 값은 모두 주어집니다.
# 감소량을 Shapiro-Wilk 정규성 검정하고, 통계량과 p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

df = df.dropna(subset = ['bp_before', 'bp_after'])

df['diff'] = df['bp_before'] - df['bp_after']

g1 = df['diff'].head(80)

from scipy.stats import shapiro

stats, pvalue = shapiro(g1)
print(round(stats, 3), round(pvalue, 3))

# 9
# 운동시간(exercise_minutes, 분)과 회복일수(recovery_days)의 선형 상관을 Pearson 양측 검정하세요.
# 두 열 중 결측값이 있는 행은 제외하세요. scipy.stats.pearsonr의 기본 양측 검정을 사용하세요.
# 상관계수, p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv').dropna(subset=['exercise_minutes', 'recovery_days'])

from scipy.stats import pearsonr

stats, pvalue = pearsonr(df['exercise_minutes'], df['recovery_days'], alternative = 'two-sided')

print(round(stats, 3), round(pvalue, 3))

# 10
# 나이(age)와 콜레스테롤(cholesterol)의 순위상관을 Spearman 양측 검정하세요(alternative='two-sided').
# 두 열 중 결측값이 있는 행은 제외하고, 상관계수와 p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv')

df = df.dropna(subset = ['age', 'cholesterol'])

from scipy.stats import spearmanr

stats, pvalue = spearmanr(df['age'], df['cholesterol'], alternative='two-sided')

print(round(stats, 3), round(pvalue, 3))

# 11
# treatment는 drug(약물군)·placebo(대조군), response는 1(치료 반응 있음)·0(없음)입니다.
# 두 열의 교차표로 카이제곱 독립성 검정하세요(correction=False).
# 통계량, 자유도(정수), 기대빈도 최솟값을 각각 한 줄씩 출력하세요. 소수는 round(..., 3)을 사용하며 p-value는 출력하지 않습니다.

import pandas as pd
df = pd.read_csv('/data/type3_practice_clinic.csv')

df = df.dropna(subset = ['treatment', 'response'])
crosstab = pd.crosstab(df['treatment'], df['response'])

from scipy.stats import chi2_contingency

chi2, pvalue, dof, expected = chi2_contingency(crosstab, correction=False)
print(round(chi2, 3), round(dof, 3), round(expected.min(), 3))

# 12
# 약물군의 치료 반응률이 대조군보다 높은지 Fisher 정확검정하세요.
# 교차표의 행은 treatment의 drug(약물군), placebo(대조군), 열은 response의 1(반응 있음), 0(없음) 순서입니다.
# alternative='greater'로 검정하고 오즈비(odds ratio), p-value를 각각 한 줄씩 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_clinic.csv')

# print(df.info())

crosstab = pd.crosstab(df['treatment'], df['response'])
crosstab = crosstab.loc[['drug', 'placebo'], [1, 0]]

from scipy.stats import fisher_exact

oddsratio, pvalue = fisher_exact(crosstab, alternative='greater')
print(round(oddsratio, 3), round(pvalue, 3), sep='\n')

# 13
# device는 기기 등급(standard, plus, premium), defect는 불량 여부(0: 정상, 1: 불량)입니다.
# 두 열의 교차표로 카이제곱 검정(correction=False)을 하고 Cramer's V를 구하세요.
# Cramer's V = sqrt(chi2 / (n * (min(r, c) - 1))). n은 전체 인원수, r·c는 교차표의 행·열 수입니다.
# 자유도(정수), Cramer's V(round(..., 3))를 각각 한 줄씩 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_clinic.csv')

from scipy.stats import chi2_contingency

crosstab = pd.crosstab(df['device'], df['defect'])
chi2, pvalue, dof, expected = chi2_contingency(crosstab, correction=False)

import numpy as np

n = crosstab.values.sum()
r = crosstab.shape[0]
c = crosstab.shape[1]

cramers_v = np.sqrt(chi2 / (n * (min(r, c) - 1)))
print(round(dof, 3), round(cramers_v, 3), sep="\n")

# 14
# 생산성 점수(productivity)를 예측하는 회귀식: productivity ~ experience + training_hours + overtime + project_count + C(department)
# 상수항을 포함한 OLS 회귀를 학습하세요. department는 범주형이며, 식에 쓰는 열의 결측 행은 제외하세요.
# training_hours 계수가 0보다 크면 'positive', 아니면 'negative'를 출력하세요.
# 이어 반올림 전 해당 계수의 p-value가 0.05 미만이면 1, 아니면 0, 마지막으로 R-squared를 출력하세요.
# 각 값을 한 줄씩 출력하고, 소수는 round(..., 3)으로 반올림하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_productivity.csv')

# print(df.columns)

import statsmodels.formula.api as smf

formula = "productivity ~ experience + training_hours + overtime + project_count + C(department)"

model = smf.ols(formula=formula, data=df).fit()

coef = model.params['training_hours']
p_val = model.pvalues['training_hours']
r2 = model.rsquared

direction = 'positive' if coef > 0 else 'negative'
is_sig = 1 if p_val < 0.05 else 0
r2_rounded = round(r2, 3)

print(direction, is_sig, r2_rounded, sep='\n')

# 15
# quality_score를 종속변수, productivity·training_hours·team_size를 독립변수로 상수항을 포함한 sm.OLS를 학습하세요.
# 네 열 중 결측값이 있는 행은 제외하세요.
# productivity 계수가 0보다 크면 'positive', 아니면 'negative'를 출력하세요.
# 다음 줄에 반올림 전 해당 계수의 p-value가 0.05 미만이면 1, 아니면 0을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_productivity.csv')

import statsmodels.formula.api as smf

formula = "quality_score ~ productivity + training_hours + team_size"
model = smf.ols(formula=formula, data=df).fit()

# print(model.params)

coef = model.params['productivity']
p_val = model.pvalues['productivity']

direction = 'positive' if coef > 0 else 'negative'
is_sig = 1 if p_val < 0.05 else 0

print(direction, is_sig, sep='\n')

# 16
# 회귀식: productivity ~ experience + training_hours + overtime + project_count + C(department)
# 상수항을 포함한 OLS 회귀를 학습하세요. department는 범주형이며, 식에 쓰는 열의 결측 행은 제외하세요.
# 신규 직원은 department='tech', experience=6, training_hours=30, overtime=1, project_count=6입니다.
# 전체 df['productivity'].mean()과 예측값을 비교해, 예측값이 더 크면 1, 아니면 0을 출력하세요.
# 다음 줄에 예측값 - 전체 평균을 round(..., 3)으로 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_productivity.csv')

import statsmodels.formula.api as smf

formula = "productivity ~ experience + training_hours + overtime + project_count + C(department)"

model = smf.ols(formula=formula, data=df).fit()

new_data = pd.DataFrame({
    'department':['tech'],
    'experience':[6],
    'training_hours':[30],
    'overtime':[1],
    'project_count':[6]
})

pred = model.predict(new_data).iloc[0]
mean_val = df['productivity'].mean()

is_higher = 1 if pred > mean_val else 0
print(is_higher, round(pred - mean_val, 3), sep='\n')

# 17
# 회귀식: productivity ~ experience + training_hours + overtime + project_count + C(department)
# 상수항을 포함한 OLS 회귀를 학습하세요. department는 범주형이며, 식에 쓰는 열의 결측 행은 제외하세요.
# Type II 분산분석표의 C(department) F값을 round(..., 3)으로 출력하세요.
# 다음 줄에 반올림 전 해당 p-value가 0.05 미만이면 1, 아니면 0을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_productivity.csv')

import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm

formula = "productivity ~ experience + training_hours + overtime + project_count + C(department)"

model = smf.ols(formula=formula, data=df).fit()
# print(model.params)

anova_table = anova_lm(model, typ=2)
# print(anova_table)

F = anova_table.loc['C(department)', 'F']
p_val = 1 if anova_table.loc['C(department)', 'PR(>F)'] < 0.05 else 0

print(round(F, 3), round(p_val, 3), sep='\n')

# 18
# 서로 다른 참가자인 program A, B, C의 만족도(wellness_score)를 Tukey HSD(alpha=0.05)로 비교하세요.
# 준비 코드에서 만족도 결측값을 제외했습니다. 유의한 프로그램 쌍의 개수를 정수로 출력하세요.
# 다음 줄에 모든 쌍의 평균 차이 절댓값 중 최댓값을 round(..., 3)으로 출력하세요. 유의하지 않은 쌍도 포함합니다.

import pandas as pd
df = pd.read_csv('/data/type3_practice_health.csv').dropna(subset=['wellness_score'])

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=df['wellness_score'], groups=df['program'], alpha=0.05)

# print(tukey)

import numpy as np

sig_count = sum(tukey.reject)
max_diff = round(max(np.abs(tukey.meandiffs)), 3)

print(sig_count, max_diff, sep='\n')

# 19
# 회귀식: productivity ~ experience + training_hours + overtime + project_count + C(department)
# 상수항을 포함한 OLS 회귀를 학습하세요. department는 범주형이며, 식에 쓰는 열의 결측 행은 제외하세요.
# 모형 잔차의 Jarque-Bera 검정 p-value를 round(..., 3)으로 출력하세요. 원자료를 검정하지 않습니다.
# 다음 줄에 반올림 전 p-value가 0.05 미만이면 1, 아니면 0을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_productivity.csv')

import statsmodels.formula.api as smf

formula = 'productivity ~ experience + training_hours + overtime + project_count + C(department)'

model = smf.ols(formula=formula, data=df).fit()
# print(model.params)

from statsmodels.stats.stattools import jarque_bera

jb_stat, p_raw, skew, kurt = jarque_bera(model.resid)

print(round(p_raw, 3), sep='\n')
answer = 1 if p_raw < 0.05 else 0
print(answer)

# 20
# 회귀식: productivity ~ experience + training_hours + overtime + project_count + C(department)
# 상수항을 포함한 OLS 회귀를 학습하세요. department는 범주형이며, 식에 쓰는 열의 결측 행은 제외하세요.
# 신규 직원은 department='ops', experience=5, training_hours=28, overtime=0, project_count=5입니다.
# 신규 직원의 예측값, 95% 관측값 예측구간의 폭(obs_ci_upper - obs_ci_lower)을 각각 한 줄씩 round(..., 3)으로 출력하세요.
# 평균의 신뢰구간이 아닌 직원 한 명의 관측값 예측구간을 사용하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_productivity.csv')

import statsmodels.formula.api as smf

formula = "productivity ~ experience + training_hours + overtime + project_count + C(department)"

model = smf.ols(formula = formula, data=df).fit()
# print(model.params)

new_data = pd.DataFrame([{
    'department' : 'ops',
    'experience' : 5,
    'training_hours' : 28,
    'overtime' : 0,
    'project_count' : 5
}])

pred_df = model.get_prediction(new_data).summary_frame(alpha=0.05)
# print(pred_df)

print(round(pred_df['mean'].iloc[0], 3))
print(round(pred_df['obs_ci_upper'].iloc[0] - pred_df['obs_ci_lower'].iloc[0], 3))

# 21
# 회귀식: purchased ~ age + income + visits + premium + ad_exposure + C(channel)
# 상수항을 포함한 statsmodels 로지스틱 회귀를 학습하고, 식에 쓰는 열의 결측 행은 제외하세요.
# purchased는 구매 여부, premium은 프리미엄 고객 여부이며 둘 다 1: 해당, 0: 해당 없음입니다.
# premium 오즈비 exp(계수)를 round(..., 3)으로 출력하세요. 다른 조건이 같을 때의 오즈 비율이며 확률 배수가 아닙니다.
# 다음 줄에 반올림 전 premium 계수의 p-value가 0.05 미만이면 1, 아니면 0을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_campaign.csv')

import statsmodels.formula.api as smf

formula = "purchased ~ age + income + visits + premium + ad_exposure + C(channel)"
model = smf.logit(formula=formula, data=df).fit(disp=False)

import numpy as np
odds_ratio = np.exp(model.params['premium'])
print(round(odds_ratio, 3))

p_val = model.pvalues['premium']
print(int(p_val < 0.05))

# 🦀 1. smf.ols : 선형 회귀
# 🦀 2. smf.logit : 로지스틱 회귀, 종속 변수 purchase가 0과 1로 이루어진 이진 분류(로지스틱 회귀)

# 22
# 회귀식: purchased ~ age + income + visits + premium + ad_exposure + C(channel)
# 상수항을 포함한 statsmodels 로지스틱 회귀를 학습하고, 식에 쓰는 열의 결측 행은 제외하세요.
# purchased=1은 구매, 0은 미구매입니다. 신규 고객은 channel='app', age=38, income=5200, visits=8, premium=1, ad_exposure=6입니다.
# 구매 확률을 round(..., 3)으로 출력하고, 다음 줄에 반올림 전 확률이 0.55 이상이면 1, 아니면 0을 출력하세요.

import pandas as pd
df = pd.read_csv('/data/type3_practice_campaign.csv')

import statsmodels.formula.api as smf
formula = "purchased ~ age + income + visits + premium + ad_exposure + C(channel)"
model = smf.logit(formula=formula, data=df).fit(disp=False)

new_data = pd.DataFrame([{
    'channel' : 'app',
    'age' : 38,
    'income' : 5200,
    'visits' : 8,
    'premium' : 1,
    'ad_exposure' : 6
}])

pred = model.predict(new_data)
print(round(pred.iloc[0], 3))
answer = round(pred.iloc[0], 3)
print(int(answer >= 0.55))
