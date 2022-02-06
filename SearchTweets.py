import tweepy
import json

bearer_token = ""
client = tweepy.Client(bearer_token=bearer_token)

response = client.search_recent_tweets(query = "big bang theory", max_results = 100)

print(response.meta)

tweets = response.data

with open('TheBigBangTheory.json', 'w') as outfile:
    result = []

    for tweet in tweets:
        data = {}
        # data["user"] = tweet.user.screen_name
        data["author_id"] = tweet.author_id
        data["id"] = tweet.id
        # data["text"] = tweet.text.encode('utf-8')
        data["text"] = tweet.text
        result.append(data)
        print(tweet.data)
    json.dump(result, outfile)
    print(len(result))