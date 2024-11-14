import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

df = pd.DataFrame(tips)

# print(df.head())
# print(df.shape)
# print(df.describe())
# print(df.info())

# # Q. 다음 코드의 빈칸을 채워주세요.

# # 'sex' 변수의 카테고리별 개수
# print(df['sex'].value_counts())
# print("===========================")

# # 'time' 변수의 카테고리별 개수
# print(df['time'].value_counts())
# print("===========================")

# # 'smoker' 변수의 카테고리별 개수
# print(df['smoker'].value_counts())
# print("===========================")

# # 'day' 변수의 카테고리별 개수
# print(df['day'].value_counts())
# print("===========================")

# # 'size' 변수의 카테고리별 개수
# print(df['size'].value_counts())
# print("===========================")

# ------------------------------------------------------------------

# print(df.head())
# grouped = df['tip'].groupby(df['sex'])
# print(grouped.mean()) # 성별에 따른 팁의 평균
# print(grouped.size()) # 성별에 따른 데이터 량(팁 횟수)

# sex = dict(grouped.mean()) #평균 데이터를 딕셔너리 형태로 바꿔줍니다.
# print(sex)

# x = list(sex.keys())  
# print(x)

# y = list(sex.values())
# print(y)

# plt.bar(x = x, height = y)
# plt.ylabel('tip[$]')
# plt.title('Tip by Sex')

# # Q. 요일(day)에 따른 평균 tip의 그래프를 그려보세요.

# grouped_by_day = df['tip'].groupby(df['day'])
# day = dict(grouped_by_day.mean())
# x = list(day.keys())
# y = list(day.values())

# plt.bar(x = x, height = y)
# plt.ylabel('tip[$]')
# plt.title('Tip by Day')
# plt.show()

#  ------------------------------------------------------------------------------

# Seaborn과 Matplotlib을 활용한 간단한 방법

# sns.barplot(data=df, x='sex', y='tip')

# plt.figure(figsize=(10,6)) # 도화지 사이즈를 정합니다.
# sns.barplot(data=df, x='sex', y='tip')
# plt.ylim(0, 4) # y값의 범위를 정합니다.
# plt.title('Tip by sex') # 그래프 제목을 정합니다.

# plt.figure(figsize=(10,6))
# sns.barplot(data=df, x='day', y='tip')
# plt.ylim(0, 4)
# plt.title('Tip by day')

# fig = plt.figure(figsize=(10,7))

# ax1 = fig.add_subplot(2,2,1)
# sns.barplot(data=df, x='day', y='tip', palette="ch:.25")

# ax2 = fig.add_subplot(2,2,2)
# sns.barplot(data=df, x='sex', y='tip')

# ax3 = fig.add_subplot(2,2,4)
# sns.violinplot(data=df, x='sex', y='tip')

# ax4 = fig.add_subplot(2,2,3)
# sns.violinplot(data=df, x='day', y='tip', palette="ch:.25")

# sns.catplot(x="day", y="tip", jitter=False, data=tips)

# # Q. 시간대(time)에 따른 tips의 그래프를 catplot으로 표현해보세요!
# sns.catplot(x="time", y="tip", jitter=False, data=tips)

# plt.show()

#  -------------------------------------------------------------------------------

# 산점도

sns.scatterplot(data=df, x='total_bill', y='tip', palette="ch:r=-.2,d=.3_r")
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day')

# 선 그래프

# np.random.randn 함수는 표준 정규분포에서 난수를 생성하는 함수입니다.
# cumsum()은 누적합을 구하는 함수입니다.
plt.plot(np.random.randn(50).cumsum())

#  plt.plot() 함수의 예제로 설명했던 그래프도 선 그래프
x = np.linspace(0, 10, 100) 
plt.plot(x, np.sin(x), 'o')
plt.plot(x, np.cos(x)) 

# Seaborn을 활용
sns.lineplot(x=x, y=np.sin(x))
sns.lineplot(x=x, y=np.cos(x))

# 히스토그램

#그래프 데이터
mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

# 축 그리기
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# 그래프 그리기
patches = ax1.hist(x1, bins=50, density=False)  # bins는 x값을 총 50개 구간으로 나눈다는 뜻입니다.
patches = ax1.hist(x2, bins=50, density=False, alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')  # x축의 눈금을 아래 표시 
ax1.yaxis.set_ticks_position('left')  # y축의 눈금을 왼쪽에 표시

# 라벨, 타이틀 달기
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
ax1.set_title('Two Frequency Distributions')

plt.show()
