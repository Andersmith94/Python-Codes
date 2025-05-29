import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
file_path = "births-and-deaths-projected-to-2100.csv"
data = pd.read_csv(file_path)

#filter data for a specific country (Afghanistan)
afghanistan_data = data[data['Entity'] == 'Afghanistan']

#extract the years, births, and deaths
years = afghanistan_data['Year']
births = afghanistan_data['Births - Sex: all - Age: all - Variant: estimates']
deaths = afghanistan_data['Deaths - Sex: all - Age: all - Variant: estimates']

#makes the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(years, births, color='skyblue', label='Births')
plt.scatter(years, deaths, color='red', label='Deaths')
plt.title('Births and Deaths in Afghanistan over time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()