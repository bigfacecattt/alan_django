# -*-coding:utf-8 -*-
# coding=utf8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,Http404
#数据库存放密码用密文
from django.contrib.auth.hashers import make_password,check_password
from app1.models import Test
from app1.models import User


def index_hello(requests):
    return HttpResponse("first_page")

def index_html_page(requests):
    return render(requests,'demo.html')
def index_html_page2(requests):
    return render(requests,'demo2.html')

def index_page_num(requests,num):
    try:
        num = int(num)
        return render(requests,'demo.html')
    except:
        return Http404

#测试从url中获取参数
def home(requests,year='2019',month='12'):
    return HttpResponse("获取当前页面的home时间标签为：%s年 %s月"%(year,month))

def url_test(requests,num='5'):
    return HttpResponse("is%s"%num)
#测试templates的视图
def views_template(requests):
    context={"kobe":{"name":"kobe","height":198},
    "iverson":{"name":"iverson","height":183}
    }
    return render(requests,'muban.html',context={"context":context})
#测试templates_include的视图
def temp_include(requests):
    context={}
    context['name']='alan' 
    return render(requests,'temp_include.html',context=context)

#测试 block extends 模板继承
def temp_extend(requests):
    context={"ads":['kobe','jordan']}
    return render(requests,'child.html',context=context)

#测试get请求获取表单
def get_test(requests):
    return render(requests,'get_test.html')
#get请求查询提交后的返回页面
def result_get(requests):
    if requests.method == 'GET':
        # 表单中的name=na
        # # #data = requests.GET['na']
        # data=requests.GET.get('na',None)
        # res=''
        # 如果是奇数则返回奇数，偶数则返回偶数
        # try:
        #     if int(data)%2:
        #         res='是奇数'
        #     else:
        #         res='是偶数'
        # except:
        #     res='请输入正确的数字'
        # return HttpResponse('输入的数字'+res,content_type='application/json;charset=utf-8')

        #通过姓名查询年纪
        data=requests.GET.get('na')
        res=Test.objects.filter(name='%s'%data)
        try:
            result=res[0].age
        except:
            result='没有该条数据'
        return render(requests,'get_test.html',context={"age":result})
    else:
        #不是get请求
        return render(requests,'get_test.html')

#用户注册的views
def register(requests):
    res=''
    if requests.method == "POST":
        username = requests.POST.get("username")
        pwd = requests.POST.get("password")
        email= requests.POST.get("email")
        #先检查是否存在该用户名
        user_list = User.objects.filter(username=username)
        if user_list:
            #如果数据库中有该用户名的数据
            res='%s 该用户名已被注册过了'%username
            return render(requests,'register.html',{"res":res})
        else:
            #插入数据库,推荐写法：
            user=User()
            user.username=username
            #明文
            # user.password=pwd
            #密文
            user.password=make_password(pwd)
            user.email=email
            user.save()
            #第二种写法
            # user=User(username=username,password=pwd,email=email)
            return render(requests,'login.html',{"res":res})
    else:
        return render(requests,'register.html')
            

#用户登录
def login(requests):
    if requests.method == "POST":
        username=requests.POST.get("username")
        pwd=requests.POST.get("password")
        #用户名校验
        
        #密文校验
        r = User.objects.filter(username=username).first()
        flag=check_password(pwd,r.password)
        #密码是明文校验
        # flag = User.objects.filter(username=username,password=pwd)
        if flag:
            #数据库中存在该用户，登录成功
            result='登录成功'
            return HttpResponse(result)
        else:
            #没有该用户，提示
            res='用户名或密码错误'
            return render(requests,'login.html',{"result":res})
    else:
        return render(requests,'login.html')
