from binance_historical_data import BinanceDataDumper


data_dumper = BinanceDataDumper(
    path_dir_where_to_dump="C:\\Users\\Google Computers\\backtesting.py\\data",
    data_type="klines",  
    data_frequency="15ms"
    # data_frequency="4h"
)

data_dumper.dump_data(
    tickers=["BTCUSDT"],
    date_start=None,
    date_end=None,
    is_to_update_existing=False
)
data_dumper.delete_outdated_daily_results()