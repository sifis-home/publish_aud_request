# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:56:22 2022

@author: wisam
"""

import websocket
import time
import json
import os
import subprocess
import _thread
import rel

import argparse
parser = argparse.ArgumentParser(description='')
parser.add_argument('--Request', help='Request Type', required=True, type=str)

args = parser.parse_args()
Request = args.Request
print("Value = ", Request)
print(type(Request))

# Put in Input JSON File

# Request = "start"

def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")


def on_open(ws):
    print("### Connection established ###")

def publish(Request = None):
    ws = websocket.WebSocketApp("ws://localhost:3000/ws",
                                on_open=on_open,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    
    
    ws_req = {
            "RequestPostTopicUUID": {
                "topic_name": "SIFIS:AUD_Manager_Request",
                "topic_uuid": "FirstRequest",
                "value": {
                    "Dev_uuid": "FirstDev",
                    "description": "First Request",
                    "Request": Request
                }
            }
        }
    ws.send(json.dumps(ws_req))

publish(Request)