from django.shortcuts import render, HttpResponse
import json
from django.views.generic import DetailView
from django.views.generic import TemplateView
from .models import Section
from django.utils.safestring import mark_safe
# '<a href="{% url \'aircraft_info\' %}">&1</a>',
def handle_text(text):
    links=[
    '<a href="/aircraft/">&1</a>',
    '<a href="/">&2</a>',
    '<a href="{% url \'home\' %}">&3</a>'
    ]
    data_h=[]
    data_w=[]

    text2=text.split(' ')
    for word in text2:
        if word[0]=='&':
            link_number=word[0]+word[1]
            for link in links:
                if link_number in link:
                    l=link.split(link_number)
                    hyperlink=l[0]+word[2:]+l[1]
                    data_h.append(hyperlink)
                    data_w.append(word)
    new_text=text
    for i in range(len(data_h)):
        new_text=new_text.replace(data_w[i], data_h[i])
    print(new_text)    
    return new_text
class Home(TemplateView):
    template_name = 'sections/home.html'

def get_data(request):
    with open('C:/Users/555/Desktop/zadanie/data_files/sections/large_text.json') as file:
        text_linlks = json.load(file)
    text=text_linlks[0]["text"]
    texthyperlink=handle_text(text)
    work_text=mark_safe(texthyperlink)
    # work_text=(texthyperlink)
    print('GET_DATA')
    context={
        "text":work_text
    }
    return render(request, 'sections/special_cases.html', context)


def aircraft(request):
    with open('C:/Users/555/Desktop/zadanie/data_files/sections/aircraft.json') as file:
        just_text = json.load(file)
    text=just_text[0]["text"]
    # print(text)
    texthyperlink=handle_text(text)
    work_text=mark_safe(texthyperlink)
    
    context={
        "text":work_text
    }
    return render(request, 'sections/aircraft.html', context)
def page1(request):
    return HttpResponse("page one two")
    