import tweepy

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

bearer_token = "AAAAAAAAAAAAAAAAAAAAAOmBYgEAAAAAczWUgmeQGFjck9WASQUdsvHvuSQ%3DWOdf9l69eQcpYJFuPWbQ3foVkzmtn35ApMIwcb7wsi1T8wyidk"

client = tweepy.Client(bearer_token=bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("gao")
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# Each Tweet object has default id and text fields
for tweet in tweets:
    # print(tweet.id)
    # print(tweet.lang)
    print(tweet.data)

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
response = client.search_recent_tweets("Tweepy", max_results=100)