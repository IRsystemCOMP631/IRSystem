from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import *
import pysolr


# 表单
def delete_form(request):
    return render(request, 'delete_form.html')


# 接收请求数据
def delete(request):
    request.encoding = 'utf-8'
    if 'id' in request.GET and request.GET['id']:
        message = 'you want delete id ' + request.GET['id']
        delete_solr(request.GET['id'])
    else:
        message = 'wrong info'
        #return HttpResponse(message)
    context = {}
    context['message'] = message
    return render(request, 'delete.html',context)

def delete_solr(id):
    solr = pysolr.Solr('http://localhost:8983/solr/test2')
    print(type(id))
    res = solr.delete(id=id)
    print(res)