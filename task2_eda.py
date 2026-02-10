import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Dataset load karna (Seaborn mein inbuilt hota hai)
df = sns.load_dataset('titanic')

# 2. Data ki pehli jhalak dekhna
print("--- Data ki shuruati 5 rows ---")
print(df.head())

# 3. Data ki basic jaankari (Kitne columns hain, kitni values miss hain)
print("\n--- Data Information ---")
print(df.info())

# 4. Statistical Summary (Mean, Median, etc.)
print("\n--- Summary Statistics ---")
print(df.describe())

# 5. Ek simple graph banana (Kitne log bache vs kitne nahi)
sns.countplot(x='survived', data=df)
plt.title('Survived (1) vs Not Survived (0)')
plt.show()

