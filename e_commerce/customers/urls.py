from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.user_account, name='account'),
    path('logout/', views.sigh_out, name='logout'),
]