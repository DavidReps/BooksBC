from django.urls import re_path, path

from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
# ]

# websocket_urlpatterns = [
#     re_path(r'ws/chat/<room_name>/(?P<bookId>\w+)/$', consumers.ChatConsumer.as_asgi()),
# ]

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/<str:bookId>/', consumers.ChatConsumer.as_asgi()),
]