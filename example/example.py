# This is how to use UCB Algorithm
from ucb import ucb
import pandas as pd

df = pd.read_csv("Ads_CTR_Optimisation.csv") # Your data type must be pandas dataframe
# Data were generated randomly.

ucb(df)


# UCB vs Random
import random
n = 10000
d = 10 
total = 0
chosens = []
for n in range(0,n):
    ad = random.randrange(d)
    chosens.append(ad)
    reward = df.values[n,ad]
    total = total + reward
print(total)

# You can compare two results from the terminal. (First one is ucb result.)