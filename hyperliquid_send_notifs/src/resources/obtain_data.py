from hyperliquid.info import Info
from hyperliquid.utils import constants
import pandas as pd
from datetime import timedelta, timezone
import datetime
import time


class ObtainPrevDayHigh:

    def __init__(self, ticker):
        self.info = Info(constants.MAINNET_API_URL, skip_ws=True)
        self.ticker = ticker

    def extract_price(self):
        """Extract price on every 5minutes candlestick close
        """
        info = self.info
        ticker = self.ticker

        # Get current datetime
        startTimeUTC = datetime.datetime.now()
        endTimeUTC = datetime.datetime.now() + timedelta(minutes=5)

        # Round down to the nearest 5min
        startTimeUTC_rounded = startTimeUTC - timedelta(minutes=startTimeUTC.minute % 5,
                                                seconds=startTimeUTC.second,
                                                microseconds=startTimeUTC.microsecond)
        endTimeUTC_rounded = endTimeUTC - timedelta(minutes=startTimeUTC.minute % 5,
                                                seconds=startTimeUTC.second,
                                                microseconds=startTimeUTC.microsecond)
        endTimeUTC_rounded = endTimeUTC_rounded.replace(second=0, microsecond=0)        # Set seconds & microseconds to 0

        # Convert into Unix timestamp in milliseconds
        startTime = int(time.mktime(startTimeUTC_rounded.timetuple()) * 1000 )
        endTime = int(time.mktime(endTimeUTC_rounded.timetuple()) * 1000)

        snapshot_data = info.candles_snapshot(ticker, "5m", startTime=startTime, endTime=endTime)   # Save 5m candle data
        # print(startTimeUTC_rounded, endTimeUTC_rounded)
        return snapshot_data

    def get_values(self, keys):
        """Filter for Timestamp, High & Low values only
        """
        snapshot_data = self.extract_price()
        filter_func = lambda d: all(k in d for k in keys)
        filtered_list = filter(filter_func, snapshot_data)
        result = [{k: d[k] for k in keys} for d in filtered_list]

        return result

    def add_to_dataframe(self):
        """Append data to daraframe
        """

        df = pd.DataFrame(columns=["t", "h", "l"])

        while True:
            result = self.get_values(keys=["t", "h", "l"])
        # if 'result' is not empty
        # if df is empty (new), append first data snapshot to df
        # if df isn't empty (alr has existing data) & timestamp isn't a duplicate, append n data snapshot to df
        # otherwise, pause loop for 5mins & wait for next 5m candlestick to close
            if result:      # check if 'result' is not empty, and run following code if it isn't
                t_value = result[0]["t"]        # retrieve "t" (Unix timestamp in milliseconds)
                if df.empty:
                    df = pd.concat([df, pd.DataFrame(result)], ignore_index=True)
                elif not df['t'].isin([t_value]).any():
                    df = pd.concat([df, pd.DataFrame(result)], ignore_index=True)
                else:
                    print("Duplicate timestamp found, program will temporarily pause to wait for next 5 minute candle close")

            # print(df)
            time.sleep(300)

        return df



Extract = ObtainPrevDayHigh(ticker="HYPE")
Extract.extract_price()
# Extract.get_values(keys=["t", "h", "l"])
Extract.add_to_dataframe()


'''
startTime = int(
    time.mktime(datetime.datetime(2024, 12, 28, 11, 10, 0).timetuple()) * 1000
)  # "2024-12-28T07:00:00Z"
endTime = int(
    time.mktime(datetime.datetime(2024, 12, 28, 11, 15, 0).timetuple()) * 1000
)  # "2024-12-28T07:10:00Z"
'''