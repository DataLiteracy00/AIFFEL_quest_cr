import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('taxis')

# # data.info()로 확인해보면 RangeIndex 값보다 Non-null Count가 작으면 해당 컬럼에 null 값, 즉 결측치가 있는 것
# print(data.info()) # 결측치 유무 확인

# isna_sum = data.isna().sum() # 결측치 개수 확인
# print(isna_sum)

# isna_percent = isna_sum / len(data) * 100
# print(isna_percent) # 결측치 비율

# print(data[data['pickup_zone'].isnull()]) # 결측치가 있는 행 print

# data.dropna(inplace = True) # 결측치 있는 행 삭제
# print(data.info())

# ------------------------------------------------------------

# passengers 컬럼의 displot을 그려보기
sns.displot(data['passengers'])

# distance 컬럼의 scatterplot을 그려보기
sns.scatterplot(data['distance'])

distance , fare , tip , total 컬럼의 히스토그램 그려보기

fig, ax = plt.subplots(2,2)
# figure 전체 크기 8인치로 설정
fig.set_size_inches(8,8)
column_list = ['distance','fare','tip','total']

for i in range(4):
  row = i // 2
  col = i % 2
  cur_ax = ax[row, col]
  sns.histplot(data=data, x=column_list[i], ax=cur_ax)
  cur_ax.set_title(f"Histogram of {column_list[i]}")

plt.tight_layout() # 서브플롯 간의 간격
plt.show()

Q1 = data['tip'].quantile(0.25)
Q3 = data['tip'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data['tip'] < lower_bound) | (data['tip'] > upper_bound)]
print(outliers['tip'])

data_no_outliers = data.drop(outliers.index)
print(data_no_outliers['tip'])