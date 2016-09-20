from django.conf.urls import url
from ttest.views import start_junior_test, EndJuniorTestView
urlpatterns = [
    url(r'start_junior/(?P<pk>\d+)', start_junior_test, name='start_junior_test'),
    url(r'end_junior', EndJuniorTestView.as_view(), name='end_junior_test')
]