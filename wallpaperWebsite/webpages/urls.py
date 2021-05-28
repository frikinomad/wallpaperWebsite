from django.urls import path
from .views import WebpageListView
from django.views.generic.base import TemplateView

urlpatterns =[
    path('', WebpageListView.as_view(), name='webpage_view'),
]