# 타이타닉 퀴즈

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# titanic_df 라는 이름으로 data/titanic.csv 불러오기
titanic_df = pd.read_csv("../data/titanic.csv")
# print(titanic_df)

# --------------------------------------------------------------------------

# 상위 15줄의 데이터 확인하기
print(titanic_df.head(15))

# info 펑션으로 데이터 변수들 살펴보기
print(titanic_df.info())

# 위의 코드에서 확인한 결과, Name 변수의 Data Type은?
print(titanic_df['Name'].dtype)
# object

# describe로 데이터의 통계적 정보 확인하기
print(titanic_df.describe())

# 위의 코드에서 확인한 결과, Survived 변수의 표준편차는?
# 0.485011

# 컬럼별 결측치 비율 확인하기
print(titanic_df.isna().mean())

# Age 컬럼의 결측치를 평균(mean) 으로 채우기
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
print(titanic_df['Age'])

# Embarked 컬럼의 결측치를 'S'로 채우기
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df['Embarked'])

# Age 컬럼의 아웃라이어를 확인하기 위해, Box Plot 그리기
# sns.boxplot(titanic_df['Age'])

# Age 컬럼의 아웃라이어를 확인하기 위해, Scatter Plot 그리기 (x축은 인덱스로 설정)
sns.scatterplot(x=titanic_df.index , y=titanic_df['Age'])
plt.xlabel = 'Index'

# Age 컬럼에서 100 이상의 데이터 포인트(데이터 행) 제거하기
titanic_df['Age'] = titanic_df['Age'][titanic_df['Age'] < 100]
titanic_df = titanic_df.sort_values(by='Age', ascending=False)
print(titanic_df)

# 변수 이름 "Gendr"를 "Gender"로 변경하기
titanic_df = titanic_df.rename({'Gendr': 'Gender'}, axis=1)
print(titanic_df)

# Gender 변수의 male을 'M'으로, female을 'F'로 변경하기
titanic_df['Gender'] = titanic_df['Gender'].replace({'male': 'M', 'female': 'F'})
print(titanic_df)

# Ticket 변수를 띄어쓰기 기준으로 분류하고, 가장 앞부분을 "ticket_head" 라는 이름의 변수로 저장하기
titanic_df['ticket_head'] = titanic_df['Ticket'].str.split().apply(lambda x : x[0])
print(titanic_df['ticket_head'])

# ticket_head 변수를 소문자로 변경하기
titanic_df['ticket_head'] = titanic_df['ticket_head'].str.lower()
print(titanic_df['ticket_head'])

# ticket_date 변수의 데이터 타입을 datetime으로 변경하기
titanic_df['ticket_date'] = pd.to_datetime(titanic_df['ticket_date'])
print(titanic_df)

plt.show()