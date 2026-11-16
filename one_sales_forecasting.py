import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jonnawaddington/Documents/DataAnalysis/Python Data Analysis Projects Package/Project 1/sales_forecasting_data.csv', parse_dates=["date"])
df = df.sort_values("date")

# Plot sales trends
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["sales"], label="Daily Sales", color='blue', alpha=0.7)
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Daily Sales Over Time")
plt.legend()
plt.show()

### Exploratory Data Analysis (EDA)
### - Examine historical sales trends across different stores.
### - Identify outliers, missing values, and data inconsistencies.
### - Visualize patterns to detect seasonality, trends, and anomalies.