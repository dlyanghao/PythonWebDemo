from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
def hello(request,name):
   template = loader.get_template('moduledao/index.html')
   context = {name:'name'}
   return HttpResponse(template.render(context,request))
