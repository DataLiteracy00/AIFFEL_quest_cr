import pandas as pd
import os

salary1_data_path = os.getenv("HOME") + "/programming/AI/AIFFEL/AIFFEL_quest_cr/Python/data/salary_1.csv"
salary2_data_path = os.getenv("HOME") + "/programming/AI/AIFFEL/AIFFEL_quest_cr/Python/data/salary_2.csv"
cpi_path = os.getenv("HOME") + "/programming/AI/AIFFEL/AIFFEL_quest_cr/Python/data/cpi.csv"

salary1_data = pd.read_csv(salary1_data_path)
salary2_data = pd.read_csv(salary2_data_path)
cpi_data = pd.read_csv(cpi_path)

# print(salary1_data.head())
# print(salary2_data.head())

salary_df = pd.concat([salary1_data, salary2_data])
# print(salary_df.loc[0])

salary_df.reset_index(drop = True, inplace = True) # drop -> 빠져나온 인덱스 제거, inplace -> 덮어쓰기
# print(salary_df)

# cpi 적용

# print(cpi_data.head())
# print(salary_df['Country'].unique())
# print(cpi_data['Country'].unique())

cpi_data['Country'] = cpi_data['Country'].replace({'United States': 'USA', 'United Kingdom': 'UK'}) 
# print(cpi_data)

salary_df = salary_df.merge(cpi_data, on = 'Country', how = 'left')
salary_df.drop(['Reference', 'Previous', 'Units', 'Frequency'], axis = 1, inplace = True)
salary_df.rename({'Last', "CPI"}, axis = 1)
print(salary_df)