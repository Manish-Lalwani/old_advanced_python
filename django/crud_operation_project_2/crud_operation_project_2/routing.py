from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from crud_operation_app_2 import consumer


websocket_url_pattern = [
    path('ws/new_test_case',consumer.DashConsumer),
    path('ws/loader',consumer.DashConsumer),
]
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(websocket_url_pattern))
})