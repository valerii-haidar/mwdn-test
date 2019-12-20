from django.conf.urls import url, include
from crawler.api import views

urlpatterns = [
    url(r'^documents/$', views.DocumentListView.as_view(), name='document_list'),
    url(
        r'^documents/(?P<pk>\d+)/$',
        views.DocumentSingleView.as_view(), name='document_single'),
    url(
        r'^documents/upload/$',
        views.DocumentCreateView.as_view(), name='document_upload'),
    url(r'^urls/$', views.UrlsList.as_view(), name='url_list'),
]

