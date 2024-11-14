import pandas as pd
import seaborn as sns

titanic_data = pd.read_csv("../data/titanic.csv")

# 메서드 TOP 10

# 1.	.describe()	DataFrame 또는 Series 객체에 대한 요약 통계를 제공합니다. 이 메소드는 데이터의 중심 경향, 분포 및 형태 등을 빠르게 이해하는 데 도움이 됩니다.
# 2.	.apply()	함수를 데이터프레임의 열 또는 행에 적용 합니다.<예시> 데이터 프레임의 모든 수치 데이터에 2를 곱합니다.
# 3.	.sort_values()	DataFrame 또는 Series 내의 값에 따라 데이터를 정렬하는 데 사용됩니다. 데이터를 오름차순 또는 내림차순으로 정렬할 수 있으며, 복수의 열을 기준으로 정렬하는 것도 가능합니다.
# 4.	.tail()	DataFrame 또는 Series 객체의 끝에서부터 지정된 수의 행을 반환합니다. 최신 데이터셋을 확인할 때 유용한데 데이터 크기가 큰 경우에 전체 데이터를 로드하지 않고도 빠른 데이터 검토를 할 수 있도록 도와줍니다.
# 5.	.replace()	특정 값을 다른 값으로 대체 <예시> 데이터 프레임의 'A' 열에서 'apple'을 'orange'로 바꿉니다.
# 6.	pd.to_numeric()	문자열이나 다른 타입의 데이터를 숫자형(정수형 또는 부동소수점형)으로 변환하는 데 사용됩니다.
# 7.	.get_dummies()	주어진 범주형 열의 각 고유 범주를 대표하는 새로운 이진(0 또는 1) 열을 생성합니다.
# 8.	Aggregation	여러 데이터 포인트를 요약하고, 그룹화하여 새로운 통계 또는 정보를 추출하는 과정입니다. groupby(), 집계 함수, std(), agg()등
# 9.	.merge()	두 개 이상의 데이터 프레임을 특정 공통 열 또는 인덱스를 기준으로 병합하는 데 사용됩니다. SQL의 JOIN과 유사한 기능을 제공합니다.
# 10.	.value_counts()	범주형 데이터를 요약하는 데이터 분석 작업에 자주 사용됩니다.

df = pd.DataFrame(titanic_data)

dt_data = df.drop(['Name','Ticket', 'ticket_date'], axis=1)

# 불필요한 컬럼 삭제 및 누락된 결측치 처리

# print(dt_data)
# print(dt_data.tail(1))

# dt_data = data.copy()
# dt_data.drop(['Name', 'Ticket', 'ticket_date'], axis=1, inplace=True)
# dt_data

# # 방법 1
# data.loc[884]
# # 방법 2
# data.iloc[884]
# # 방법 3
# data.iloc[-1]

# 'Embarked'의 결측치 출력
# data[data['Embarked'].isna()]

# -------------------------------------------------------------------------------

# 이상치 탐지 및 처리


# df.boxplot(column="SibSp")
# sns.boxplot(df['SibSp'])

# df['Age'] = df['Age'].apply(lambda x: 70 if x > 70 else x)
# df = df.sort_values(by='Age', ascending=False)

# print(df)

# -------------------------------------------------------------------------------

# 중복 데이터 처리 및 데이터 형태 변환처리

# apply, replace, map, rename

# df['Gendr'] = df['Gendr'].replace({'male': 0, 'female': 1})
# replace_data = df.rename({'Gendr': 'Gender'}, axis=1)
# print(replace_data)

# -------------------------------------------------------------------------------

#  텍스트 처리

# Ticket 열을 문자열로 변환한 후 숫자만 추출
df['new_ticket'] = df['Ticket'].astype(str).str.split().apply(lambda x: int(x[-1]) if x[-1].isdigit() else None)

# df['new_ticket'] = df['Ticket'].str.split().apply(lambda x: x[-1])
# df['new_ticket'] = df['new_ticket'].replace({'LINE': '999999'})
# df['new_ticket'] = df['new_ticket'].astype('int')
print(df)

# -------------------------------------------------------------------------------

# 날짜 및 시간 데이터 처리

# 메소드와 dt 메소드 2개의 주요 차이점

# str 메소드: 문자열 데이터를 다룹니다. Series 또는 DataFrame에 문자열이 포함된 경우 .str accessor를 사용하여 각 요소의 문자열 메소드에 접근할 수 있습니다.
# dt 메소드: 날짜/시간 데이터를 다룹니다. datetime64 또는 Timedelta 유형의 데이터에 대해 .dt accessor를 사용하여 날짜와 시간 관련 정보를 추출하거나 변환할 수 있습니다.

from datetime import datetime

date1 = datetime.strptime('2022-11-24', '%Y-%m-%d')
date2 = datetime.strptime('2023-3-15', '%Y-%m-%d')

result = date2 - date1
print(result)

date1 = datetime.strptime('1912-04-15', '%Y-%m-%d')
date2 = pd.to_datetime(df['ticket_date'])

df['buy_ticket'] = date2.apply(lambda x: (date1 - x).days)
print(df)