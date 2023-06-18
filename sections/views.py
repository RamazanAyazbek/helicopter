from django.shortcuts import render, HttpResponse
import json
from django.views.generic import DetailView
from django.views.generic import TemplateView
# from .models import Section
from django.utils.safestring import mark_safe
from root.hyperlinkConv import handle_text, handle_text_urlJson



def helicopter_cabin(request):
    with open('C:/Users/555/Desktop/zadanie/data_files/sections/large_text.json') as file:
        text_linlks = json.load(file)
    text=text_linlks[0]["text"]
    url=text_linlks[0]["url"]
    texthyperlink=handle_text_urlJson(text, url) # здесь мы используем метод, которой работает когда url в jsone и вместе с текстом.
    work_text=mark_safe(texthyperlink)

    context={
        "text":work_text
    }
    return render(request, 'sections/helicopter_cabin.html', context)


def page1(request):
    return HttpResponse("page for cargo part | gruz otdel ")
    