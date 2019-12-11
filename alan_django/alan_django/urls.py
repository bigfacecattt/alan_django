"""alan_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#导入include
from django.urls import include

from django.conf.urls import url
from app1 import views
from . import testdb


urlpatterns = [
    path('admin/', admin.site.urls),
    #分层路由
    path('app1/',include('app1.urls')),
    # url(r'^demo/page=(\d+)$/',views.index_page_num),
    url('^testdb/',testdb.testdb)
]
