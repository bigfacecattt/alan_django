# -*-coding:utf-8 -*-
from django.urls import path
from django.conf.urls import url
from app1 import views
urlpatterns = [
    path(r'index_hello/',views.index_hello),
    path(r'index_html_page/',views.index_html_page),
    url(r'^demo/?page=(\d+)$', views.index_page_num),
    path(r'home/<year>/<month>/',views.home),
    path(r'test<num>/',views.url_test),
    #正则匹配URL
    url(r'demo2/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})$',views.home),
    #url name作用，在html href中直接调用name <a href=" {% url 'name的值' %} ">
    url('^index_html_page2/',views.index_html_page2,name='page2'),
    #测试template路由
    url('^template/',views.views_template),
    #测试template——include路由
    url('include/',views.temp_include),
    #测试模板的继承
    url('^extends/',views.temp_extend),
    #get请求的url
    url(r'^get_test/',views.get_test),
    #get请求成功后的返回url
    url(r'^get_result/',views.result_get,name='get_result'),
    #post请求注册用户
    url(r'^register/',views.register),
    #用户登录
    url(r'^login/',views.login),
]
