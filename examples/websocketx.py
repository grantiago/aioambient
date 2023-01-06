#!/usr/bin/env python3

"""Run an example script to quickly test."""
from __future__ import annotations

import asyncio
import logging
from typing import Any

from aioambient import Websocket
from aioambient.errors import WebsocketError

_LOGGER = logging.getLogger()
import json
import time
import threading
timeout = time.time() + 60*5   # 5 minutes from now
timeout = 30  # [seconds]

timeout_start = time.time()
# path = args.path
path = './'
# fname = args.fname
fname = 'response.json'
API_KEY = ""
APP_KEY = ""

def print_data(data: dict[str, Any]) -> None:
    """Print data as it is received.
    Args:
        data: The websocket data received.
    """
    _LOGGER.info("Data received: %s", data)

def print_goodbye() -> None:
    """Print a simple "goodbye" message."""
    _LOGGER.info("Client has disconnected from the websocket")


def print_hello() -> None:
    """Print a simple "hello" message."""
    _LOGGER.info("Client has connected to the websocket")


def print_subscribed(data: dict[str, Any]) -> None:
    """Print subscription data as it is received.
    Args:
        data: The websocket data received.
    """
    _LOGGER.info("Client has subscribed: %s", data)
    
def write_json(data: dict[str, Any]) -> None:
    """Print subscription data as it is received.
    Args:
        data: The websocket data received.
    """
    #_LOGGER.info("Client has subscribed: %s", data)
    try:
            f = open("{}{}".format(path, fname), 'w')

    except Exception as e:
        print('A problem has occurred: ', e)
        sys.exit()

    with f:
        myJson = json.dumps(data)
        f.write(myJson)
        print('\nFile Saved Successfully!')
        print("{}{}\n".format(path, fname))

async def main() -> None:
    """Run the websocket example."""
    logging.basicConfig(level=logging.INFO)
    websocket = Websocket(APP_KEY, API_KEY)
    websocket.on_connect(print_hello)
    websocket.on_data(print_data)
    websocket.on_disconnect(print_goodbye)
#    websocket.on_subscribed(print_subscribed)
    websocket.on_subscribed(write_json)


    try:
        await websocket.connect()
    except WebsocketError as err:
        _LOGGER.error("There was a websocket error: %s", err)
        return
        test -= 1
    while True:
        _LOGGER.info("Simulating some other task occurring...")
        await asyncio.sleep(5)


asyncio.run(main())
