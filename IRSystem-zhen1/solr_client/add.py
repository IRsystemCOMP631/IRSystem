from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import *
import pysolr
from . import utils


# 表单
def add_form(request):
    return render(request, 'add_form.html')


# 接收请求数据
def add(request):
    request.encoding = 'utf-8'
    message = ''
    if 'id' in request.GET and request.GET['id'] and 'author_id' in request.GET and request.GET['author_id'] and 'text' in request.GET and request.GET['text']:
        message += 'id is ' + request.GET['id'] + '\n'
        message += 'author_id is ' + request.GET['author_id'] + '\n'
        message += 'text is' + request.GET['text'] + '\n'
        add_solr(request.GET['id'], request.GET['author_id'], request.GET['text'])
    else:
        message = 'info wrong'
        #return HttpResponse(message)
    context = {}
    context['message'] = message
    return render(request, 'add.html', context)

def add_solr(id, author_id, text):
    solr = pysolr.Solr('http://127.0.0.1:8983/solr/movie_search', always_commit=True)
    res = solr.add([
        {
            "id": id,
            "author_id": author_id,
            "text": text,
        }
    ])
    print(id, author_id, text)
