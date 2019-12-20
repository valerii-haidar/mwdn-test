from django.conf.urls import url, include
from django.contrib import admin
from crawler import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('crawler.urls')),
    url(r'^$', views.UploadFileView.as_view(), name='home')
]
