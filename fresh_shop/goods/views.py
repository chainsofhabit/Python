from django.shortcuts import render

from goods.models import Goods,GoodsCategory
from utils.functions import login_required


# @login_required
def index(request):
    if request.method == 'GET':
        #{category1:[Goods object1]}
        goods = Goods.objects.all()
        categorys = GoodsCategory.CATEGORY_TYPE
        goods_dict = {}
        for category in categorys:
            goods_list = []
            count = 0
            for good in goods:
                #判断商品分类和商品对象
                if count <4:
                    if category[0] == good.category_id:
                        goods_list.append(good)
                        count += 1
            goods_dict[category[1]] = goods_list


        return render(request,'index.html',{'goods_dict':goods_dict})


def detail(request,id):
    if request.method == 'GET':
        goods = Goods.objects.filter(pk=id).first()
        return render(request,'detail.html',{'goods':goods})





