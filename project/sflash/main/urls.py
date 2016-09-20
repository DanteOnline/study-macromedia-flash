from django.conf.urls import url
from main.views import main_view

urlpatterns = [
    url(r'^$',main_view,name='index')
]