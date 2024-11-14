import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_path = os.getenv("HOME") + "/programming/AI/AIFFEL/AIFFEL_quest_cr/Python/data/flights.csv"
data = pd.read_csv(csv_path)
flights = pd.DataFrame(data)
# print(flights)

# sns.barplot(data=flights, x='year', y='passengers')

# # Q. seaborn pointplot을 그려봅시다.
# sns.pointplot(data=flights, x='year', y='passengers')

# # Q. seaborn lineplot을 그려봅시다.
# sns.lineplot(data=flights, x='year', y='passengers')

# sns.lineplot(data=flights, x='year', y='passengers', hue='month', palette='ch:.50')
# plt.legend(bbox_to_anchor=(1.03, 1), loc=2) #legend 그래프 밖에 추가하기

# sns.histplot(flights['passengers'])

# --------------------------------------------------------------------------------------------------------

# Heatmap

# pivot = flights.pivot(index='year', columns='month', values='passengers')
# sns.heatmap(pivot)
# sns.heatmap(pivot, linewidths=.2, annot=True, fmt="d")

# # Q. cmap 인자를 "YlGnBu"로 지정하여 heatmap을 그려보세요!
# sns.heatmap(pivot, cmap="YlGnBu", linewidths=.2, annot=True, fmt="d")

tips = sns.load_dataset("tips")

sns.scatterplot(x="tip", y="total_bill", hue="time", data=tips)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Relationship between Total Bill and Tip by Time")

# Q. seaborn jointplot의 문서를 참고하여 아래와 같은 그래프를 그려보세요!
sns.jointplot(x="total_bill", y="tip", hue="time", data=tips)

plt.show()