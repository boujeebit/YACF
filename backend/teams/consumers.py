from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TeamConsumer(AsyncJsonWebsocketConsumer):
    ##### WebSocket event handlers

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        # Are they logged in?
        # if self.scope["user"].is_anonymous:
        #     # Reject the connection
        #     await self.close()
        # else:
        #     # Accept the connection
        await self.accept()
        print("Accepting connections")
        # Store which rooms the user has joined on this connection
        self.scoreboard = set()

    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        # Messages will have a "command" key we can switch on
        command = content.get("command", None)
        print(command)
        print(content)
        # try:
        if command == "join":
            # Make them join the room
            await self.join_room(content["room"])
        #     elif command == "leave":
        #         # Leave the room
        #         await self.leave_room(content["room"])
        #     elif command == "send":
        #         await self.send_room(content["room"], content["message"])
        # except ClientError as e:
        #     # Catch any errors and send it back
        #     await self.send_json({"error": e.code})

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        # Leave all the rooms we are still in
        print("Disconnecting")
        # for room_id in list(self.rooms):
        #     try:
        #         print("Leave room")
        #         # await self.leave_room(room_id)
        #     except ClientError:
        #         pass

    #### Command helper methods called by receive_json

    async def join_room(self, id):
        """
        Called by receive_json when someone sent a join command.
        """
        self.scoreboard.add(id)
        print(self.scope["user"])
        # Add them to the group so they get room messages
        await self.channel_layer.group_add(
            # str(self.scope["user"]),
            "scoreboard",
            self.channel_name
        )
        # Instruct their client to finish opening the room
        await self.send_json({
            "join": "true",
            "channel": "scoreboard",
            "user": str(self.scope["user"])
        })

    async def scoreboard_update(self, event):
        """
        Called when someone has messaged our chat.
        """
        print("I am here!?! :)")
        # Send a message down to the client
        await self.send_json(
            {
                "type"   : 1,
                "team"   : event["team"],
                "points" : event["points"],
                "added"  : event["added"],
                "time"   : event["time"]
            },
        )