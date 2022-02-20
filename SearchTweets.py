import tweepy
import json
import re
import os
#删除了一下电影名，因为在request的时候会出错，暂不清楚原因, 可能是名字包含and或者法语字母

bearer_token = ""
client = tweepy.Client(bearer_token=bearer_token)

def read_document(name):
    with open(name, "r") as f:
        document = f.read()
    return document

def remove_punctuation(document):
    document = re.sub(r'[^\w\s]', '', document)
    return document.strip()

def case_folding(document):
    return document.lower()

movie_list = read_document("movie_list.txt")
movie_list = remove_punctuation(movie_list)
movie_list = case_folding(movie_list)
movie_list = movie_list.split('\n')
print("query all " + str(len(movie_list)) + "movies")


count = 0
for i in range(197,237):
    title = movie_list[i]
    print(title)
    response = client.search_recent_tweets(query = title, max_results = 100, tweet_fields=["author_id" ,"text","id","lang"])

    tweets = response.data

    doc_name = "./documents/"
    file_name = doc_name + title + ".json"

    with open(file_name, 'w') as outfile:
        result = []

        for tweet in tweets:
            data = {}
            data["author_id"] = tweet.author_id
            data["id"] = tweet.id
            data["text"] = tweet.text
            if(tweet.lang == "en"):
                result.append(data)
        print(i)
        count += len(result)
        print(count)
        json.dump(result, outfile)

