from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def sigh_out(request):
    logout(request)
    return redirect('index')
def user_account(request):
    post_method = request.POST
    user_check = {}
    if post_method:
        try:
            if 'login' in post_method:
                username = post_method.get('username')
                password = post_method.get('password')
                user_check['login'] = True
                
            elif 'register' in post_method:
                username = post_method.get('username')
                email = post_method.get('email')
                password = post_method.get('password')
                address = post_method.get('address')
                phone = post_method.get('phone')
                user_check['register'] = False
            else:
                pass

            # user accout creation
            print(user_check)
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email,
            )

            # customer account creation

            customer = Customer.objects.create(
                name = username,
                user = user,
                phone = phone,
                address = address,
            )
            success_message = "registerd successfully"
            messages.success(request, success_message)
        except Exception as e:
            error_msg = "username already exist"
            messages.error(request, error_msg)
    if post_method:
        if 'login' in post_method:
            username = post_method.get('username')
            password = post_method.get('password')
            user = authenticate(username=username,
                                password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                error_msg = "invalid username or password"
                print(error_msg)
                messages.error(request, error_msg)
    return render(request, 'account.html', user_check)
