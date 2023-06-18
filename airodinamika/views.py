from django.shortcuts import render, HttpResponse
import json
from django.utils.safestring import mark_safe
from root.hyperlinkConv import handle_text, handle_text_urlJson


def new_page(request):
    return HttpResponse("hi, it's weather page !")

def special_cases(request):
    with open('C:/Users/555/Desktop/zadanie/data_files/sections/aircraft.json') as file:
        just_text = json.load(file)
    text=just_text[0]["text"]
    # print(text)
    texthyperlink=handle_text(text) #метод работает когда у нас есть отдельный json для ссылок, 
    work_text=mark_safe(texthyperlink)
    
    context={
        "text":work_text
    }
    return render(request, 'airodinamika/aircraft.html', context)