import hashlib


from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect

from Store.models import *

def loginValid(fun):
    def inner(request,*args,**kwargs):
        c_user = request.COOKIES.get("username")
        s_user = request.session.get("username")
        if c_user and s_user and c_user == s_user:
            user = Seller.objects.filter(username=c_user).first()
            if user:
                return fun(request,*args,**kwargs)
        return HttpResponseRedirect("/Store/login/")
    return inner

def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def register(request):
    """
    register注册
    返回注册页面
    进行注册数据保存
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            seller = Seller()
            seller.username = username
            seller.password = set_password(password)
            seller.nickname = username
            seller.save()
            return HttpResponseRedirect("/Store/login/")
    return render(request,"store/register.html")

def login(request):
    """
    登陆功能，如果登陆成功，跳转到首页
    如果失败，跳转到登陆页
    """
    response = render(request,"store/login.html")
    response.set_cookie("login_from","login_page")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = Seller.objects.filter(username = username).first()
            if user:
                web_password = set_password(password)
                cookies = request.COOKIES.get("login_from")
                if user.password == web_password and cookies == "login_page":
                    response = HttpResponseRedirect("/Store/index/")
                    response.set_cookie("username",username)
                    response.set_cookie("user.id", user.id) #cookie提供用户id方便其他功能查询
                    request.session["username"] = username
                    return response
    return response

@loginValid
def index(request):
    """
    添加检查账号是否有店铺的逻辑
    """
    #查询当前用户是谁
    user_id = request.COOKIES.get("user_id")
    if user_id:
        user_id = int(user_id)
    else:
        user_id = 0
    #通过用户查询店铺是否存在(店铺和用户通过用户的id进行关联)
    store = Store.objects.filter(user_id=user_id).first()
    if store:
        is_store = 1
    else:
        is_store = 0
    return render(request,"store/index.html",{"is_store": is_store})

def register_store(request):
    type_list = StoreType.objects.all()
    if request.method == "POST":
        post_data = request.POST #接收post数据
        store_name = post_data.get("store_name")
        store_descripton = post_data.get("store_descripton")
        store_phone = post_data.get("store_phone")
        store_money = post_data.get("store_money")
        store_address = post_data.get("store_address")

        user_id =int(request.COOKIES.get("user.id")) #通过cookie来得到user_id
        type_lists = post_data.get("type") #通过request.post得到类型，但是是一个列表

        store_logo = request.FILES.get("store_logo") #通过request.FILES得到

        #保存非多对多数据
        store = Store()
        store.store_name = store_name
        store.store_descripton = store_descripton
        store.store_phone = store_phone
        store.store_money = store_money
        store.store_address = store_address
        store.user_id = user_id
        store.store_logo = store_logo #django1.8之后图片可以直接保存
        store.save() #保存，生成了数据库当中的一条数据
        #在生成的数据当中添加多对多字段。
        for i in type_lists: #循环type列表，得到类型id
            store_type = StoreType.objects.get(id = i) #查询类型数据
            store.type.add(store_type) #添加到类型字段，多对多的映射表
        store.save() #保存数据

    return render(request,"store/register_store.html",locals())

def base(request):
    return render(request,"store/base.html")

def add_goods(request):
    """
    负责添加商品
    """
    if request.method == "POST":
        #获取post请求
        goods_name = request.POST.get("goods_name")
        goods_price = request.POST.get("goods_price")
        goods_number = request.POST.get("goods_number")
        goods_description = request.POST.get("goods_description")
        goods_date = request.POST.get("goods_date")
        goods_safeDate = request.POST.get("goods_safeDate")
        goods_store = request.POST.get("goods_store")
        goods_image = request.FILES.get("goods_image")
        #开始保存数据
        goods = Goods()
        goods.goods_name = goods_name
        goods.goods_price = goods_price
        goods.goods_number = goods_number
        goods.goods_description = goods_description
        goods.goods_date = goods_date
        goods.goods_safeDate = goods_safeDate
        goods.goods_image = goods_image
        goods.save()
        #保存多对多数据
        goods.store_id.add(
            Store.objects.get(id = int(goods_store))
        )
        goods.save()
    return render(request,"store/add_goods.html")


def list_goods(request):
    keywords = request.GET.get('keywords','')
    page_num = request.GET.get('page_num',1)
    if keywords:
        goods_list = Goods.objects.filter(goods_name__contains=keywords)
    else:
        goods_list = Goods.objects.all()
    paginator = Paginator(goods_list,3)
    page = paginator.page(int(page_num))
    page_range = paginator.page_range

    return render(request,'store/goods_list.html',{'page':page,'page_range':page_range,'keywords':keywords})

# Create your views here.















