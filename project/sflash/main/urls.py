from django.conf.urls import url
from main.views import main_view, change_image_host

urlpatterns = [
    url(r'^$',main_view,name='index'),
    url(r'^fix$', change_image_host, name='fix')
]