from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages

# Create your views here.
def user_account(request):
    form_method = request.POST
    if form_method:
        try:
            if 'login' in form_method:
                username = form_method.get('username')
                password = form_method.get('password')
                
            elif 'register' in form_method:
                username = form_method.get('username')
                email = form_method.get('email')
                password = form_method.get('password')
                address = form_method.get('address')
                phone = form_method.get('phone')
            else:
                pass

            # user accout creation

            user = User.objects.create(
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
            return redirect('index')
        except Exception as e:
            error_msg = "user already exist"
            messages.error(request, error_msg)
    return render(request, 'account.html')
