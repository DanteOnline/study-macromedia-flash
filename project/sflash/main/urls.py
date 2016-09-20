from django.conf.urls import url
from main.views import change_image_host, MainPageView, MaterialView

urlpatterns = [
    url(r'^$',MainPageView.as_view(),name='index'),
    url(r'^fix$', change_image_host, name='fix'),
    url(r'^material', MaterialView.as_view(), name='material')
]