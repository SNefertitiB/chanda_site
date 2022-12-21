from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render(context,request))
