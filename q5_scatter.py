import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("revenue.csv")

#Trading duration vs. Revenue
plt.figure(figsize=(12, 6))
plt.scatter(df["TradingDurationDays"], df["TotalRevenue"], color='Green')
plt.xlabel("Trading Duration (Days)")
plt.ylabel("Total Revenue")
plt.title("Relationship Between Store Trading Duration and Revenue")
plt.show()

# Correlation calculation
correlation = df["TradingDurationDays"].corr(df["TotalRevenue"])
correlation