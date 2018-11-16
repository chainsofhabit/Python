from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserRegisterForm, UserAddressForm
from user.models import User, UserAddress
from django.http import HttpResponseRedirect,JsonResponse

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data)
        if form.is_valid():


            User.objects.create(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            return HttpResponseRedirect(reverse('user:login'))

        else:
            return render(request,'register.html',{'errors':form.errors})


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        # data = request.POST
        # form = UserLoginForm(data)
        # if form.is_valid():
        #     user = User.objects.filter(username=request.POST.get('username')).first()
        #     if not user:
        #         msg = '该用户还没注册'
        #         return render(request,'login.html',{'msg':msg})
        #     return HttpResponseRedirect(reverse('goods:index'))
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not all([username,password]):
            msg = '请填写完整的参数'
            return render(request,'login.html',{'msg':msg})

        user = User.objects.filter(username=username).first()
        if not user:
            msg = '该用户还没注册'
            return render(request,'login.html',{'msg':msg})

        # if check_password(password,user.password):
        #     #验证成功
        #     request.session['user_id'] = user.id
        #     return HttpResponseRedirect(reverse('goods:index'))
        # else:
        #     msg = '密码不正确'
        #     return render(request, 'login.html', {'msg': msg})

        if password != user.password:
            msg = '密码不正确'
            return render(request, 'login.html', {'msg': msg})

        request.session['user_id'] = user.id
        return HttpResponseRedirect(reverse('goods:index'))

def is_login(request):
    if request.method == 'GET':
        #清空session
        user = request.user
        return JsonResponse({'code':200,'msg':'请求成功','username':user.username})


def logout(request):
    if request.method == 'GET':
        #清空session
        request.session.flush()
        return HttpResponseRedirect(reverse('goods:index'))

def user_center_order(request):
    if request.method == 'GET':
        return render(request,'user_center_info.html')

def user_address(request):
    if request.method == 'GET':
        user = request.user
        #获取用户的收货地址
        user_addresses = UserAddress.objects.filter(user=user).order_by('-id')
        return render(request,'user_center_site.html',{'user_addresses':user_addresses})
    if request.method == 'POST':
        #使用表单验证，验证收货地址的参数是否填写完整
        form = UserAddressForm(request.POST)
        if form.is_valid():
            user = request.user
            address_info = form.cleaned_data
            #保存收货地址
            UserAddress.objects.create(**address_info,user=user)
            return HttpResponseRedirect(reverse('user:user_address'))
        else:
            user = request.user
            #获取用户的收货地址信息
            user_addresses = UserAddress.objects.filter(user=user).order_by('-id')
            return render(request,'user_center_site.html',{'form':form,'user_addresses':user_addresses})