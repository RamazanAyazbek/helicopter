from django.shortcuts import render, HttpResponse
import json
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe


class Home(TemplateView):
    template_name = 'sections/home.html'