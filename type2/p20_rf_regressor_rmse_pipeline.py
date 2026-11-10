# 정답 열은 amount이며 record_id는 행을 구분하는 식별자입니다.
# train['amount']를 정답 y로, train에서 record_id와 amount를 제외한 모든 열을 입력 X로 만드세요.
# train_test_split에 X와 y를 함께 전달해 학습용(train) 75%, 검증용(validation) 25%로 나누세요.
# 반환값은 X_train, X_valid, y_train, y_valid 순서로 받으세요. test_size=0.25, random_state=42를 사용하세요.
# stratify는 사용하지 마세요.
# X_train의 숫자 열에서 구한 중앙값으로 X_train과 X_valid의 숫자 빈칸을 채우세요.
# 문자 열의 빈칸은 두 자료 모두 'unknown'으로 채우세요.
# 문자 열은 pd.get_dummies(..., dtype=int, drop_first=False)로 각각 원핫 인코딩하세요.
# X_valid의 열 이름과 순서를 X_train에 맞추고, 없는 열은 0으로 채우세요.
# 모델 설정: RandomForestRegressor(n_estimators=70, max_depth=6, min_samples_leaf=3, random_state=42, n_jobs=1)
# X_train과 y_train으로 모델을 학습하고 X_valid를 예측해 y_valid와 비교하세요.
# y_valid와 회귀 예측값의 RMSE를 round(..., 4)로 출력하세요. RMSE는 mean_squared_error 결과의 제곱근이며 작을수록 좋습니다.

import pandas as pd
train = pd.read_csv('/data/p20_train.csv')
y = train['amount']
X = train.drop(columns = ['record_id', 'amount'])

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.25, random_state=42)

num_cols = X_train.select_dtypes(include='number').columns.tolist()
cat_cols = X_train.select_dtypes(include='object').columns.tolist()

num_median = X_train[num_cols].median()
X_train[num_cols] = X_train[num_cols].fillna(num_median)
X_valid[num_cols] = X_valid[num_cols].fillna(num_median)
X_train[cat_cols] = X_train[cat_cols].fillna('unknown')
X_valid[cat_cols] = X_valid[cat_cols].fillna('unknown')

X_train = pd.get_dummies(X_train, columns=cat_cols, dtype=int, drop_first=False)
X_valid = pd.get_dummies(X_valid, columns=cat_cols, dtype=int, drop_first=False)

X_valid = X_valid.reindex(columns = X_train.columns, fill_value=0)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=70, max_depth=6, min_samples_leaf=3, random_state=42, n_jobs=1)
model.fit(X_train, y_train)
pred = model.predict(X_valid)

from sklearn.metrics import root_mean_squared_error
print(round(root_mean_squared_error(pred, y_valid), 4))
