from backtesting import Backtest , Strategy
import pandas as pd


# df=pd.read_csv("C:\\Users\\Google Computers\\backtesting.py\\data\\df15m.csv")  
df=pd.read_csv("C:\\Users\\Google Computers\\backtesting.py\\data\\df4h.csv")  

class Signal(Strategy):
    
    def next(self):
        current_signal = self.data.Position[-1]

        if current_signal == 1:
            if not self.position:
                self.buy()
            elif current_signal == 1:
                if self.position:
                    self.position.close()

bt = Backtest(df, Signal, cash= 100000000)

stats = bt.run()
print (stats)
bt.plot()
