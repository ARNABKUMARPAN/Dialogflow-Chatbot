from django.conf.urls import url
from django.contrib import admin
from .views import chat_view, index_view, bb

urlpatterns = [
    url(r'chat/$', chat_view, name='chat'),
    url(r'^$', index_view, name='index'),
    url(r'^f/', bb, name='bb')


    #url(r'^admin/', admin.site.urls),
]
