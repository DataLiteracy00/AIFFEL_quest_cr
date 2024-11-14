import numpy as np
import pandas as pd
import os

# ser = pd.Series(['a','b','c',3])
# print(ser.index)

# ser2 = pd.Series(['a', 'b', 'c', 3], index=['i','j','k','h'])
# print(ser2)
# ser2.index = ['Jhon', 'Steve', 'Jack', 'Bob']
# print(ser2)

csv_path = os.getenv("HOME") + "/programming/AI/AIFFEL/AIFFEL_quest_cr/Python/data/covid19_italy_region.csv"
data = pd.read_csv(csv_path)

# print(type(data))
# print(data.head(3))
# print(data.tail())

# print(data.columns)
# print(data.info())  # 각 컬럼별로 Null값과 자료형을 보여주는 메서드
# print(data.describe()) # 개수(Count), 평균(mean), 표준편차(std), 최솟값(min), 4분위수(25%, 50%, 75%), 최댓값(max)

# print(data.isnull().sum())
# print(data['RegionName'].value_counts()) # 각 범주(Case 또는Category)별로 값이 몇 개 있는지 구할 수 있음
# print(data['Country'].value_counts())
# print(data['Country'].value_counts().sum())

# print("총 감염자", data['TotalPositiveCases'].sum())
# print("전체 검사자 수", data['TestsPerformed'].sum())
# print("사망자 수", data['Deaths'].sum())
# print("회복자 수", data['Recovered'].sum())
# print(data.sum())  # 컬럼별로 합 구하기

# 상관관계 분석 (상관관계 분석은 데이터가 숫자로만 이루어져 있어야 하므로 문자열 데이터가 있는 컬럼은 제외해야 한다.)
# print(data['TestsPerformed'].corr(data['TotalPositiveCases']))
# print(data['TestsPerformed'].corr(data['Deaths']))
# print(data['TotalPositiveCases'].corr(data['Deaths']))
data.drop(['RegionName','Latitude','Longitude','Country','Date','HospitalizedPatients',  'IntensiveCarePatients', 'TotalHospitalizedPatients','HomeConfinement','RegionCode','SNo'], axis=1, inplace=True)
# print(data.corr())

# pandas 기본 통계 메서드
# count(): NA를 제외한 수를 반환합니다.
# describe(): 요약 통계를 계산합니다.
# min(), max(): 최소, 최댓값을 계산합니다.
# sum(): 합을 계산합니다.
# mean(): 평균을 계산합니다.
# median(): 중앙값을 계산합니다.
# var(): 분산을 계산합니다.
# std(): 표준편차를 계산합니다.
# argmin(), argmax(): 최소, 최댓값을 가지고 있는 값을 반환합니다.
# idxmin(), idxmax(): 최소, 최댓값을 가지고 있는 인덱스를 반환합니다.
# cumsum(): 누적 합을 계산합니다.
# pct_change(): 퍼센트 변화율을 계산합니다.

# print(data.pct_change())
