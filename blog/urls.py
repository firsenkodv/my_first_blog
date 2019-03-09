from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [path('', views.post_list, name='post_list'),
path('main', views.main, name='main'),
url(r'^send/', views.send),
path('news', views.news, name='news'),
]
