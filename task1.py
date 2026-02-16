import matplotlib.pyplot as plt


ages = [12, 15, 17, 18, 20, 22, 25, 27, 30, 35, 40, 45, 50, 55, 60]


plt.hist(ages, bins=5)


plt.title("Age Distribution Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")


plt.show()
