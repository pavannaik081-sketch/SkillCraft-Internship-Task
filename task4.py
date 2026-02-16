import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("accident.csv")

print(data.head())

sns.barplot(x="time", y="accidents", data=data)
plt.title("Accidents by Time of Day")
plt.show()

sns.barplot(x="weather", y="accidents", data=data)
plt.title("Accidents by Weather")
plt.show()

sns.barplot(x="road_condition", y="accidents", data=data)
plt.title("Accidents by Road Condition")
plt.show()
