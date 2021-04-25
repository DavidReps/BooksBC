from django.urls import path
from accounts import views
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "accounts"

urlpatterns = [

    path('', views.home, name="home" ),
    path('register/', views.register, name="register"),
    path('clientcreation/', views.clientcreation, name="clientcreation"),
    path('sellerlisting/', views.sellerlisting, name="sellerlisting"),
    path('cart/', views.cart, name="cart"),
    path('profile/', views.profile, name="profile"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#IMAGESTUFF - line above
