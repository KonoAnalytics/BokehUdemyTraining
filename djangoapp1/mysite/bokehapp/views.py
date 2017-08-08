from django.shortcuts import render
from . import BasicLine

def index(request):
    context={"div":BasicLine.div,
             "js":BasicLine.js,
             "cdn_js":BasicLine.cdn_js,
             "cdn_css":BasicLine.cdn_css,
             }
    return render(request,'bokehapp/index.html', context)