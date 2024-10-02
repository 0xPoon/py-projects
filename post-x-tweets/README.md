# Post conditional tweets based on Fed Interest Rate data
### This application aims to post conditional tweets based on Fed Interest Rate data
### If Rate cut is more than expected, then it suggests Fed knows something we don't, and something could be wrong with the economy; can be perceived as a ***negative / bearish sentiment***
### If Rate cut is in line with expectations, then it suggests that market is in tune with Fed's perception of the current macro situation; can be perceived as a ***neutral / bullish sentiment***
### If Rate cut is less than expectations, then it suggests that inflation could be still prevalent in the economy; ***perceived as bearish / neutral sentiment***
## Libraries used: *selenium*, *pandas*, *tweepy*, *io*, *datetime*
## Program is split into different 3 parts: *extract_int_rate_data.py*, *transform_int_rate_data.py*, *post_tweets.py*
## Program will be refreshed as per schedule, using Airflow hosted on an EC2 instance on a Linux VM
### 1) *extract_int_rate_data.py*: extracts interest rate data using web scraping, stores as dataframe and returned
### 2) *transform_int_rate_data.py*: transforms interest rate data using pandas, returns dataframe
### 3) *post_tweets.py*: contains main logic that would post tweets based on Interest Rate cut decision
