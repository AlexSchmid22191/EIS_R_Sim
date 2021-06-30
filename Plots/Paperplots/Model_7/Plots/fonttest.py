import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
print(mpl.font_manager.get_cachedir())

df = pd.DataFrame({'perc': pd.Series([45, 35, 10, 5, 3, 2], index=['A', 'B', 'C','D','E','F'])})

# specify the custom font to use
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'LibertinusSans'

fig, ax = plt.subplots(figsize=(7,4))
df.iloc[::-1].plot(kind='barh', legend = False, ax=ax)
ax.set_xlabel('Percentage',fontsize=15)
ax.set_ylabel('Type',fontsize=15)


plt.show()