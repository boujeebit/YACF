from django.urls import path

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from teams.consumers import TeamConsumer


application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("team/stream/", TeamConsumer),
        ]),
    ),

})