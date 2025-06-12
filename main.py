import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the data
df = pd.read_csv("Unemployment in India.csv")

#Show basic info
print(df.info())
print(df.head())

# Check null values
print(df.isnull().sum())

# Drop rows with null values
df.dropna(inplace=True)
print(df.shape)    #after cleaning to check the number of rows and columns in the dataframe.
print(df.columns)
df.columns = df.columns.str.strip() #spaces are removed.
print(df.columns)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce') #converting string date into pandas datetime object.
df = df.dropna(subset=['Date'])
print(df.Date)

#unemployement rate over the date in all regions.
plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title("Unemployment Rate Over Time by Region")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#average unemployment rate over the region.
avg_unemp = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_unemp.plot(kind='barh', color='skyblue')
plt.title("Average Unemployment Rate by Region")
plt.xlabel("Unemployment Rate (%)")
plt.show()

#heatmap of unemployment rate by region and date
pivot = df.pivot_table(values='Estimated Unemployment Rate (%)', index='Region', columns='Date')
plt.figure(figsize=(16, 8))
sns.heatmap(pivot, cmap='YlGnBu')
plt.title("Heatmap of Unemployment Rate by Region and Date")
plt.show()







