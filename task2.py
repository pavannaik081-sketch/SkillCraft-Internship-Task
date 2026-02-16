import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Python/titanic.csv")

print(data.head())


plt.hist(data['Age'], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

sns.countplot(x='Sex', hue='Survived', data=data)
plt.title("Survival by Gender")
plt.show()
