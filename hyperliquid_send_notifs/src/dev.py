from hyperliquid.info import Info
from hyperliquid.utils import constants
import datetime
import time
from datetime import timedelta

'''
# Convert Unix timestamp back to datetime
start_ms = startTime / 1000.00
end_ms = endTime / 1000.00

# Convert to datetime objects
start_ts = datetime.datetime.fromtimestamp(start_ms, tz=timezone.utc)
end_ts = datetime.datetime.fromtimestamp(end_ms, tz=timezone.utc)

# print(startTimeUTC, endTimeUTC)
# print(start_ts, end_ts)
'''


# Get the current time and subtract 5 minutes
startTimeUTC = datetime.datetime.now() # - timedelta(minutes=5)

# Round down to the nearest 5 minutes
rounded_time = startTimeUTC - timedelta(minutes=startTimeUTC.minute % 5,
                                         seconds=startTimeUTC.second,
                                         microseconds=startTimeUTC.microsecond)

print("Original Time:", startTimeUTC)
print("Rounded Down Time:", rounded_time)