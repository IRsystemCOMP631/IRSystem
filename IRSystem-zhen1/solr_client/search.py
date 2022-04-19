from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import *
import solr_client.tools.sentiment as sentiment


# 表单
def search_form(request):
    # if 'text' in request.GET and request.GET['text']:
    #     request.GET['text'] = rep(request.GET['text'])
    #
    # if 'author_id' in request.GET and request.GET['author_id']:
    #     request.GET['author_id'] = rep(request.GET['author_id'])
    # if 'id' in request.GET and request.GET['id']:
    #     request.GET['id'] = rep(request.GET['id'])
    return render(request, 'search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    numFound = 0
    result_list = []
    message =""
    text = ""
    author_id = ""
    id = ""
    sentiment_score = -1
    if 'text' in request.GET and request.GET['text']:
        text += request.GET['text']

    if 'author_id' in request.GET and request.GET['author_id']:
        author_id += request.GET['author_id']
    if 'id' in request.GET and request.GET['id']:
        id += request.GET['id']
    if text == "" and author_id == "" and id == "":
            message = 'You submitted an empty form'
            # return HttpResponse(message)
    else:

        message = 'You are searching for: ' + request.GET['text']
        numFound, result_list, sentiment_score = search_solr(text, author_id, id)
    context          = {}
    context['message'] = message
    context['sentiment'] = sentiment_score
    context['result_list'] = result_list
    context['numFound'] = numFound
    return render(request, "search.html", context)

def search_solr(text,auhor_id="",id=""):
    url = 'http://127.0.0.1:8983/solr/movie_search/select?indent=true&q.op=OR&q='
    count = 0
    if(text != ""):
        if(count == 0):
            url += "text%3A"
            count = 1
        else:
            url += "%20AND%text%3A"
        text = rep(text)
        print(text)
        url += text
    if(auhor_id != ""):
        if (count == 0):
            url += "author_id%3A"
            count = 1
        else:
            url += "%20AND%20author_id%3A"

        url += auhor_id
    if (id != ""):
        if (count == 0):
            url += "id%3A"
            count = 1
        else:
            url += "%20AND%20id%3A"

        url += id
    url += '&wt=python'
    connection = urlopen(url)
    response = eval(connection.read())
    #print(response['response']['numFound'], "documents found.")

    # Print the name of each document.
    print(url)
    result_list = []
    sentiment_score = 0.0
    s = sentiment.Sentiment()
    for document in response['response']['docs']:
        # print("  id =", document['id'])
        # print("  author_id =", document['author_id'])
        # print("  text =", document['text'])
        sentiment_result = s.get_sentiment(document['text'])[0]
        positive_score = sentiment_result.confidence_scores.positive
        neutral_score = sentiment_result.confidence_scores.neutral
        sentiment_score += positive_score + neutral_score * 0.5
        result_list.append(document)
    sentiment_score_avg = sentiment_score / len(response['response']['docs'])
    return response['response']['numFound'],result_list, sentiment_score_avg

def rep(s):
    li = []
    for i in s:
        li.append(i)
    for i in li:
        if i==' ':
            li[li.index(i)]='%20'
    return ''.join(li)

