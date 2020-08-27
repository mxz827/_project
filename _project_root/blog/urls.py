from django.conf.urls import url
from django.urls import include,path
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns =[
    #url(r'^blog/',admin.site.urls),

    #both two ways below can call html correctly
    #path('',views.blog_list,name ='blog_list' ),
    url(r'^$',views.blog_list,name ='list'),
    url(r'^create/$',views.blog_create, name = 'create'),
    url(r'^(?P<slug>[\w-]+)/$',views.blog_detail,name='detail'),
    
    
    ]
