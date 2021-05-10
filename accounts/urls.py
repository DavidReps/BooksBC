from django.urls import path, re_path
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
    path('profile/<str:user>', views.profile, name="profile"),
    path('buying/', views.buying, name="buying"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('chat/', views.chat, name="chat"),
    path('chat/<str:room_name>/<str:bookId>/', views.room, name='room'),
    path('soldbook/<str:bookId>/', views.sold_book, name='sold'),
    # path('chat/<str:room_name>/', views.room, name='room'),

    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('adminpage/<str:bookId>/', views.adminpage, name="adminpage1"),
    path('adminpage/<str:userId>/', views.adminpage, name="adminpage2"),
    path('reportlisting/', views.reportlisting, name="reportlisting"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#IMAGESTUFF - line above
