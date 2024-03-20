# depict the unemployment rate over time
import matplotlib.pyplot as plt

year = [1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020]
uRate = [10.0,7.2,9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3,14.7]

plt.plot(year, uRate, color='green', marker='*')
plt.title("Unemployment Rate Over Time", fontsize=16)
plt.xlabel("Year", fontsize=16)
plt.ylabel("Unemployment Rate", fontsize=16)
plt.grid(True)
plt.show()
