from app1.models import Test
from django.http import HttpResponse

#数据库操作
def testdb(requests):
    test1=Test(name='alan2',age=3)
    test1.save()
    return HttpResponse("数据添加成功")