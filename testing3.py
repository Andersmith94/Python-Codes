import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
file_path = "average_prices.csv"
data = pd.read_csv(file_path)

#filter data
bread_data = data[data['item_name'].str.contains('Bread', case=False, na=False)]

#convert values to numeric
bread_data.loc[:, 'value'] = pd.to_numeric(bread_data['value'], errors='coerce')

#drop missing values
bread_data = bread_data.dropna(subset=['year', 'value'])

#group by year and average
bread_data_avg = bread_data.groupby('year')['value'].mean().reset_index()

#plot graph
plt.figure(figsize=(10, 6))
plt.plot(bread_data_avg['year'], bread_data_avg['value'], color='skyblue', label='Gas (all types)', linewidth=2)
plt.title('Average price of bread over time in USA', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Price (in Dollars)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()