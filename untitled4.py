import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Data.csv')


plt.bar(df['Product ID'],df['Profit'],color = '#2a2438')
plt.savefig('plot1.png', dpi=600, bbox_inches='tight')
plt.show()


