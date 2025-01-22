from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import sys

print("\n\n")
print(f"{sys.version =}")

data_path = Path(__file__).parent

print(data_path / "athlete_events.csv")

df = pd.read_csv(data_path / "athlete_events.csv")

print(df.head())

print(df.info())


# 按性别分组，计算平均年龄
avg_age_by_sex = df.groupby("Sex")["Age"].mean()

# 绘制柱状图
avg_age_by_sex.plot(kind="bar", color=["blue", "pink"], figsize=(8, 5), title="Avg age by sex")

plt.xlabel("SEX")
plt.ylabel("AVERAGE AGE")
plt.tight_layout()

plt.savefig(data_path / "bar_chart.png")
plt.show()

print("-------------------")
df.head().to_csv(data_path / "athlete_head.csv")


