from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name="home" ),
    path('about', AboutView.as_view(), name="about"),
    path('news', NewsView.as_view(), name="news"),
    path('contact', ContactView.as_view(), name="contact"),
    path('change_lang',change_lang, name="change_lang" ),
]


