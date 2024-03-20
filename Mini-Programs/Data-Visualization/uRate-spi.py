# depict relationship between unemployment rates and stock price index
import matplotlib.pyplot as plt

uRate = [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2]
spi = [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]

plt.scatter(uRate, spi, color='green')
plt.title('Unemployment Rate Vs Stock Price Index', fontsize=16)
plt.xlabel('Unemployment Rate', fontsize=16)
plt.ylabel('Stock Price Index', fontsize=16)
plt.grid(True)
plt.show()
