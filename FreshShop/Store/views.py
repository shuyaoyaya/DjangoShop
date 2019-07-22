
import hashlib
from Store.models import *
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


def loginValid(fun):
    def inner(request,*args,**kwargs):
        c_user = request.COOKIES.get('username')
        s_user = request.session.get('username')
        if c_user and s_user and c_user == s_user:
            user = Seller.objects.filter(username=c_user).first()
            if user:
                return fun(request,*args,**kwargs)
        return HttpResponseRedirect('/Store/login')
    return inner

def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            seller = Seller()
            seller.username = username
            seller.password = set_password(password)
            seller.nickname = username
            seller.save()
            return HttpResponseRedirect('/Store/login/')
    return render(request,'store/register.html')

def login(request):
    response = render(request,'store/login.html')
    response.set_cookie('login_form','login_page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password' )
        if username and password:
            user = Seller.objects.filter(username = username).first()
            if user:
                web_password = set_password(password)
                cookies = request.COOKIES.get('login_form')
                if user.password == web_password and cookies == 'login_page':
                    response = HttpResponseRedirect('/Store/index/')
                    response.set_cookie('username',username)
                    request.session['username'] = username
                    return response
    return response

@loginValid
def index(request):
    return render(request,'store/index.html')
    # Create your views here.
