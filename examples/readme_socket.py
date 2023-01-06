#!/usr/bin/env python3.9

import asyncio

from aiohttp import ClientSession

from aioambient import Websocket

API_KEY = ""
APP_KEY = ""
API_KEY = ""
APP_KEY = ""

async def main() -> None:
    """Create the aiohttp session and run the example."""
    websocket = Websocket(APP_KEY, API_KEY)

    # Define a method that should be fired when the websocket client
    # connects:
    def connect_method():
        """Print a simple "hello" message."""
        print("Client has connected to the websocket")

    websocket.on_connect(connect_method)

    # Define a method that should be run upon subscribing to the Ambient
    # Weather cloud:
    def subscribed_method(data):
        """Print the data received upon subscribing."""
        print(f"Subscription data received: {data}")

    websocket.on_subscribed(subscribed_method)

    # Define a method that should be run upon receiving data:
    def data_method(data):
        """Print the data received."""
        print(f"Data received: {data}")

    websocket.on_data(data_method)

    # Define a method that should be run when the websocket client
    # disconnects:
    def disconnect_method(data):
        """Print a simple "goodbye" message."""
        print("Client has disconnected from the websocket")

    websocket.on_disconnect(disconnect_method)

    # Connect to the websocket:
    await websocket.connect()

    # At any point, disconnect from the websocket:
    await websocket.disconnect()


asyncio.run(main())
