from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import *


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
        numFound, result_list = search_solr(text, author_id, id)
    context          = {}
    context['message'] = message

    context['result_list'] = result_list
    context['numFound'] = numFound
    return render(request, "search.html", context)

def search_solr(text,auhor_id="",id=""):
    url = 'http://127.0.0.1:8983/solr/test1/select?indent=true&q.op=OR&q='
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
    for document in response['response']['docs']:
        # print("  id =", document['id'])
        # print("  author_id =", document['author_id'])
        # print("  text =", document['text'])
         result_list.append(document)
    return response['response']['numFound'],result_list

def rep(s):
    li = []
    for i in s:
        li.append(i)
    for i in li:
        if i==' ':
            li[li.index(i)]='%20'
    return ''.join(li)

