from django.urls import path
from accounts import views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView


app_name = "accounts"

urlpatterns = [

    path('', views.home, name="home" ),
    path('register/', views.register, name="register"),
    path('clientcreation/', views.clientcreation, name="clientcreation"),
    path('sellerlisting/', views.sellerlisting, name="sellerlisting"),
    path('buying/', views.buying, name="buying"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#IMAGESTUFF - line above
