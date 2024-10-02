# (3) Construct statement logic
#     then post tweet on Twitter account using tweepy python package (free tier). Timing of post should be dependent on timing when figures get released, utilise time python package for this.

import pandas as pd
import tweepy
from extract_int_rate_data import ExtractDataFromHTML
from transform_int_rate_data import TransformData
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Set global options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width',-1)

class PostTweets:

    def __init__(self, df):
        self.df = df

    def construct_statement_logic(self):
        df = self.df
        diff = None

        if (df["Event"] == "Fed Interest Rate Decision").any():     # checks if "Fed Interest Rate Decision" exists in any of hte rows for df["Event"]
            try:
                # Obtain 'Actual' & 'Previous' Interest Rate values, convert to float, calculate diff in and bps
                actual = str(df['Actual'].iloc[0])
                actual_flt = float(actual[:4])
                previous = str(df['Previous'].iloc[0])
                previous_flt = float(previous[:4])
                diff = previous_flt - actual_flt
                bips_diff = int(diff) * 100

                # if difference between Actual & Previous = 0.25, then "Expected Rate cut, observe trend closely"
                # if difference between Actual & Previous >= 0.50, then "Bigger than expected Rate cut, possible short play"
                if diff <= 0.25:
                    print(f"Interest Rate remained the same, observe trend closely")
                if diff == 0.25:
                    print(f"Expected Rate cut of {diff*100:.0f}, observe trend closely")
                if diff >= 0.50:
                    print(f"Bigger than expected Rate cut of {diff*100:.0f}bps, possible short play")
                # return diff
            except ValueError:
                print("'Actual' value missing, therefore cannot convert empty string to float")

        else:
            print("Fed Interest Rate Decision is not present this week. Please wait for the next one")
        return diff

    def post_to_twitter(self, consumer_key, consumer_secret, access_token, access_token_secret):
        diff = self.construct_statement_logic()
        tweet_text = ""
        client = tweepy.Client(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)

        if diff is not None:
            if diff <= 0.25:
                tweet_text = "Interest Rate remained the same, observe trend closely"
                response = client.create_tweet(text=tweet_text)
            elif diff == 0.25:
                tweet_text = f"Expected Rate cut of {diff * 100:.0f}, observe trend closely"
                response = client.create_tweet(text=tweet_text)
            elif diff >= 0.50:
                tweet_text = f"Bigger than expected Rate cut of {diff * 100:.0f} bps, possible short play"
                response = client.create_tweet(text=tweet_text)
        else:
            tweet_text = "No relevant information to tweet at this time."
            response = client.create_tweet(text=tweet_text)


# Call ExtractDataFromHTML from 'extract_cpi_data.py'
Extracted_DF = ExtractDataFromHTML("https://sslecal2.investing.com/?columns=exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&importance=3&countries=5&calType=week&timeZone=8&lang=1")
Extracted_DF.extract_data()
data = Extracted_DF.save_to_csv()       # Save original df to 'data'

# Create instance of TransformData from 'transform_int_rate_data'
Transform_Data = TransformData(data)
Transform_Data.remove_null_rows()
Transform_Data.transform_date_format()
Transform_Data.fill_down_date()
transformed_df = Transform_Data.extract_filtered_df()

# Create instance of PostTweets
Post_Tweets = PostTweets(transformed_df)
Post_Tweets.construct_statement_logic()
Post_Tweets.post_to_twitter(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)