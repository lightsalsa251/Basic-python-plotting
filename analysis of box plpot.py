import matplotlib.pyplot as plt
import numpy as np
import statistics as st


spread = np.random.rand(50) * 100
#50 random values from 0 to 1 multiplied by 100
center = np.ones(25) * 50
#25 ones multiplied by 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), axis=0)

plt.boxplot(data)

x = len(data)
for i in range(x):
    if data[i]<-40 or data[i]>130:
        np.delete(data,i,0)
plt.boxplot(data)
plt.show()

#removing outliers by visualizing


print(st.median_grouped(data))
