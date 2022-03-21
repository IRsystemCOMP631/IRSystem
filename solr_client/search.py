from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import *


# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    numFound = 0
    result_list = []
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
        numFound,result_list = search_solr(request.GET['q'])
    else:
        message = '你提交了空表单'
        #return HttpResponse(message)
    context          = {}
    context['message'] = message

    context['result_list'] = result_list
    context['numFound'] = numFound
    return render(request, "search.html", context)

def search_solr(q):
    url = 'http://127.0.0.1:8983/solr/test1/select?indent=true&q.op=OR&q=text%3A'
    url += q
    url += '&wt=python'
    connection = urlopen(url)
    response = eval(connection.read())
    print(response['response']['numFound'], "documents found.")

    # Print the name of each document.
    result_list = []
    for document in response['response']['docs']:
        print("  id =", document['id'])
        print("  author_id =", document['author_id'])
        print("  text =", document['text'])
        result_list.append(document)
    return response['response']['numFound'],result_list