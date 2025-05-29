import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
file_path = "births-and-deaths-projected-to-2100.csv"
data = pd.read_csv(file_path)

#select data for India and the US
india_data = data[data['Entity'] == 'India']
usa_data = data[data['Entity'] == 'United States']

births_2000_india = india_data[india_data['Year'] == 2000]['Births - Sex: all - Age: all - Variant: estimates']
births_2000_usa = usa_data[usa_data['Year'] == 2000]['Births - Sex: all - Age: all - Variant: estimates']

#combine data into a single list for comparison
combine_births = [births_2000_india.values[0], births_2000_usa.values[0]]
countries = ['India', 'United States']

#plot the bar chart for comparison
plt.figure(figsize=(10, 6))
plt.bar(countries, combine_births, color=['skyblue', 'green'], edgecolor='black')
plt.title('Comparison of Births in 2000: India vs United States', fontsize=18)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Births', fontsize=14)
plt.grid(axis='y')
plt.show()