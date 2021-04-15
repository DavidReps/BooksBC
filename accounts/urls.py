from django.urls import path
from accounts import views
from . import views


app_name = "accounts"

urlpatterns = [

    path('', views.home, name="home" ),
    path('register/', views.register, name="register"),
    path('clientcreation/', views.clientcreation, name="clientcreation"),
    path('sellerlisting/', views.sellerlisting, name="sellerlisting"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
]