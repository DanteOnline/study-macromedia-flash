from django.conf.urls import url
from theory.views import TheoryDetailView

urlpatterns = [
    url(r'/(?P<pk>\d+)', TheoryDetailView.as_view(), name='theory')
]