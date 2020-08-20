from django.shortcuts import render
from app_1.models import Tag
#queryset转dict
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist  # ObjectDoesNotExist 值不存在的异常类型
import  json
# Create your views here.
def index(request):
    #插入数据
    #实例化对象
    Book_obj=Tag(id=1,title='百度百科全书',pub_date='2020-8-18',price=100,publish='百度')
    #save()之后记录才会生成 # 表里面的一条记录就是类的一个对象
    Book_obj.save()
    # 1. all() ：查询所有结果；返回值是一个QuerySet数据类型（Django自定义的数据类型），调用者是 objects
    # all_books = Tag.objects.all()
    all_books = Tag.objects.get(id=1)
    # queryset转dict
    data=model_to_dict(all_books)


    print(data)
    return render(request,template_name='app_1/index.html',context=data)