from django.conf.urls import url
from ttest.views import start_junior_test, EndJuniorTestView, start_senior_test, EndSeniorTestView, start_profi_test, EndProfiTestView, ProfiFormView, JuniorTemplateView, SeniorTemplateView, TestMainView
urlpatterns = [
    url(r'start_junior/(?P<pk>\d+)', start_junior_test, name='start_junior_test'),
    url(r'end_junior', EndJuniorTestView.as_view(), name='end_junior_test'),
    url(r'start_senior/(?P<pk>\d+)', start_senior_test, name='start_senior_test'),
    url(r'end_senior', EndSeniorTestView.as_view(), name='end_senior_test'),
    url(r'start_profi/(?P<pk>\d+)', start_profi_test, name='start_profi_test'),
    url(r'end_profi', EndProfiTestView.as_view(), name='end_profi_test'),
    url(r'profi_form/(?P<pk>\d+)', ProfiFormView.as_view(), name='profi_form'),
    url(r'junior_form/(?P<pk>\d+)', JuniorTemplateView.as_view(), name='junior_form'),
    url(r'senior_form/(?P<pk>\d+)', SeniorTemplateView.as_view(), name='senior_form'),
    url(r'^$', TestMainView.as_view(), name='test_index')
]