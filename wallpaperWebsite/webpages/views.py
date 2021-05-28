from django.shortcuts import render
from .models import Design
from django.views.generic import ListView
# Create your views here.

class WebpageListView(ListView):
    model = Design
    template_name = "webpages/home.html"
    # def get_context_data():

