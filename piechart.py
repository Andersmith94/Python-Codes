import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
file_path = "births-and-deaths-projected-to-2100.csv"
data = pd.read_csv(file_path)

#filter data for the year 1950 and sum births and deaths globally
year_data = data[data["Year"] == 1950 ]

#calc global totals for births and deaths
total_birth = year_data["Births - Sex: all - Age: all - Variant: estimates"].sum()
total_deaths = year_data["Deaths - Sex: all - Age: all - Variant: estimates"].sum()

#data for the pie chart
labels = ["Births", "Deaths"]
sizes = [total_birth, total_deaths]

#plot the pie chart
plt.figure(figsize = (8,8))
plt.pie(sizes, labels = labels, autopct='%1.1f%%', startangle=90, colors = ['skyblue', 'lightcoral'])
plt.title("Global Births vs Deaths (1950)" , fontsize = 16)
plt.show()