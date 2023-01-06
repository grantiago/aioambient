#!/usr/bin/env python3
from ambient_api.ambientapi import AmbientAPI
import time
import os, sys
import json
"""Run an example script to quickly test."""
import asyncio
import logging

from aiohttp import ClientSession

from aioambient import API
from aioambient.errors import AmbientError
import argparse
from argparse import RawTextHelpFormatter


dsc = ' v. 0.1.1 2022-09-17\n changelog:\n  0.1.2 loop and write json files for both stations.  \n  0.1.0 initial build.\n  try > except\n  argsparse:\n   -p path\n   -f file name\n retrieve the hill road  weather json from the ambient weather api.\n write result as json\n '
parser = argparse.ArgumentParser(description= dsc, formatter_class=RawTextHelpFormatter)

parser.add_argument("-p", "--path", nargs='?', type=str, default='/www/rivers/dev/weather/json/', help="-p save dir. default:/www/rivers/dev/weather/json/")

parser.add_argument("-f", "--fname", nargs='?', type=str, default='ambient_weather.json', help="-f file name with ext. default: ambient_weather.json")

args = parser.parse_args()
# ---- set some vars ----
path = args.path
fname = args.fname

_LOGGER = logging.getLogger()

API_KEY = ""
APP_KEY = ""
path = './'
#fname = 'result.json'
pathandfname = os.path.join(path, fname)
async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.INFO)
    async with ClientSession() as session:
        try:
            api = API(APP_KEY, API_KEY, session=session)

            devices = await api.get_devices()
            # _LOGGER.info("Devices: %s", devices)
            for obj in devices:
                try:
                    if obj["macAddress"] == "98:CD:AC:22:78:CE":
                        fname = 'hillr_info'
                        json_data = json.dumps(obj, indent=4)
                        f = open("{}{}".format(path, fname + '.json'), 'w')
                    else: 
                        fname = 'barra_info'
                        json_data = json.dumps(obj, indent=4)
                        f = open("{}{}".format(path, fname + '.json'), 'w')

                except Exception as e:
                    print('A problem has occurred: ', e)
                    sys.exit()

                with f:
                    f.write(json_data)
                    print('\nFile Saved Successfully!')
                    print("{}{}\n".format(path, fname + ".json"))

            for device in devices:
                details = await api.get_device_details(device["macAddress"])
                jsonString = json.dumps(details, indent=4) # print('\n')
                # _LOGGER.info("Device Details (%s): %s", device["macAddress"], details)
                # print(name)
                try:
                    if device["macAddress"] == "98:CD:AC:22:78:CE":
                        fname = 'hillr'
                    else: fname = 'barra'
                    f = open("{}{}".format(path, fname + '.json'), 'w')
                    # f = open("{}{}".format(path, fname, encoding='utf-8'), 'w') # encoding='utf-8'

                except Exception as e:
                    print('A problem has occurred: ', e)
                    sys.exit()

                with f:
                    # f.write(device["macAddress"])
                    f.write(jsonString)
                    print('\nFile Saved Successfully!')
                    print("{}{}\n".format(path, fname + ".json"))

        except AmbientError as err:
            _LOGGER.error("There was an error: %s", err)
        


asyncio.run(main())