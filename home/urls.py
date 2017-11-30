from django.conf.urls import url

from . import views

app_name = "home"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^submit_abstract/$', views.submit_abstract, name='submit_abstract'),
    url(r'^submission_success/$', views.submission_success, name='submission_success'),
    url(r'^submission_fail/$', views.submission_fail, name='submission_fail'),
]
