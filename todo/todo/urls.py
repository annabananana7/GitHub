from django.conf.urls.defaults import patterns, url

from todo import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^about/$', views.AboutView.as_view(), name='about'),

    url(r'^create/$', views.CreateView.as_view(), name='create'),

    url(r'^load/$', views.LoadView.as_view(), name='load'),

    url(r'^links/$', views.LinksView.as_view(), name='links'),
)
