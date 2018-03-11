import pandas as pd
import matplotlib.pyplot as plt


X = []
df = pd.read_csv('weather_data.csv')
X.append(df['temperature'])
X.append(df['windspeed'])
y = df['event']

plt.figure(1,(6,8))
plt.clf()
plt.scatter(X[0],X[1])


plt.hist(X, 50, normed=1, facecolor='green', alpha=0.75)
plt.show()
