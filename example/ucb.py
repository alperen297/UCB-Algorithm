"""
    Author: Alperen Aydın
    Description: UCB Algorithm (Reinforced Learning)
"""

import math
import pandas as pd

def ucb(data) -> int:
    if not type(data) == pd.DataFrame:
        raise Exception("Data type must be DataFrame")
    
    n = len(data)
    d = len(data.columns)
    ri = [0] * d
    ni = [0] * d
    tco = []
    
    for i in range(1,n):
        chosen = 0
        max_ucb = 0
        for j in range(0,d):
            if ni[j] > 0:
                average = ri[j] / ni[j]
                delta = math.sqrt(3/2 * math.log(i) / ni[j])
                ucb = delta + average
            else:
                ucb = n * 10
            
            if max_ucb < ucb:
                max_ucb = ucb
                chosen = j

        tco.append(chosen)
        ni[chosen] = ni[chosen] + 1
        ri[chosen] = ri[chosen] + data.values[i,chosen]
        ttl_rwrd = 0
        for k in range(len(ri)):
            ttl_rwrd += ri[k] 

    print(ttl_rwrd)
