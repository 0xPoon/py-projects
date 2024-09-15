import tweepy

class XAuthentication:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def auth_object(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return auth

    def api_object(self):
        auth = self.auth_object()
        # Create API object
        api = tweepy.API(auth)
        return api

class XTweets:
    # def __init__(self, api):
    #     self.api = api

    def extract_tweets(self, api):
        # api = self.api
        # Define search query and number of tweets
        query = 'python'
        num_tweets = 10

        # Extract tweets
        tweets = tweepy.Cursor(api.search_tweets, q=query).items(num_tweets)

        # Print tweets
        for tweet in tweets:
            print(tweet.text)

# Create an instance of XAuthentication
auth_instance = XAuthentication('Zhqw1T9FH7CHCG8nGUeTwKrbd', '5ui7OC3YNv0kmH7nreax1les3e9n8Qs9I76O26q5ah7WCJfPvg', '1383804256063344645-dLhdk4lO34wNaYHf1npsLk0fV7ZaP7', 'ic3zWI8a8UemErDnGyAB3jKmB4xudZaiv5sIpa6KhTurm')
# Return Twitter API object
tweet_api_instance = auth_instance.api_object()

tweets_instance = XTweets()
# Call the extract_tweets method on the instance
tweets = tweets_instance.extract_tweets(tweet_api_instance)
print(tweets)