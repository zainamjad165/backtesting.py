import pandas as pd
import numpy as np


def Supertrend(df, atr_period, multiplier):
    
    high = df['high']
    low = df['low']
    close = df['close']
    
    
    price_diffs = [high - low, high - close.shift(), close.shift() - low]
    true_range = pd.concat(price_diffs, axis=1)
    true_range = true_range.abs().max(axis=1)

    atr = true_range.ewm(alpha=1/atr_period,min_periods=atr_period).mean() 
    
    hl2 = (high + low) / 2

    final_upperband = upperband = hl2 + (multiplier * atr)
    final_lowerband = lowerband = hl2 - (multiplier * atr)
    
    supertrend = [0] * len(df)
    position = [0] * len(df)

    for i in range(1, len(df.index)):
        curr, prev = i, i-1

        if close[curr] > final_upperband[prev]:
            supertrend[curr] = 1

        elif close[curr] < final_lowerband[prev]:
            supertrend[curr] = -1

        else:
            supertrend[curr] = supertrend[prev]
            
            if supertrend[curr] == 1 and final_lowerband[curr] < final_lowerband[prev]:
                final_lowerband[curr] = final_lowerband[prev]
                
            if supertrend[curr] == -1 and final_upperband[curr] > final_upperband[prev]:
                final_upperband[curr] = final_upperband[prev]

        if supertrend[curr] == supertrend[prev]:
            position[curr] = 0

        elif supertrend[curr] == 1 and  supertrend[prev] == 0 :
            position[curr]=1

        elif supertrend[curr] == 1 and  supertrend[prev] == -1 :
            position[curr]=1

        elif supertrend[curr] == -1 and  supertrend[prev] == 1 :
            position[curr]=-1

        if supertrend[curr] == 1:
            final_upperband[curr] = np.nan

        else:
            final_lowerband[curr] = np.nan
    
    return pd.DataFrame({'Supertrend': supertrend,'Position': position,'Final Lowerband': final_lowerband,'Final Upperband': final_upperband}, index=df.index)


df=pd.read_csv("C:\\Users\\Google Computers\\backtesting.py\\data\\4h timeframe.csv")  
# df=pd.read_csv("C:\\Users\\Google Computers\\backtesting.py\\data\\15m timeframe.csv")

atr_period = 10
atr_multiplier = 3.0

supertrend = Supertrend(df, atr_period, atr_multiplier)

df = df.join(supertrend)

df.to_csv("C:\\Users\\Google Computers\\backtesting.py\\data")