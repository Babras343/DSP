import asyncio
import websockets
import socket
from base64 import b64decode
import wave
import json 
import csv

global_data = {}

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


hostname = socket.gethostname()
IPAddr = get_ip()
print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)
print(
    "* Enter {0}:5000 in the app.\n* Press the 'Set IP Address' button.\n* Select the sensors to stream.\n* Update the 'update interval' by entering a value in ms.".format(IPAddr))

async def save_global_data(global_data):
    f = open("sensors.csv", "a")
    f.write(global_data+ "\n")

async def echo(websocket, path):
    global global_data

    async for message in websocket:
        if path == '/accelerometer'or path == '/gyroscope':
            data = await websocket.recv()
            f = open("acceleration.csv", "a")
            f.write(data+"\n")

            global_data = data  # Assign data to global variable
            print(f"Global data updated: {global_data}")

            # Parse the received data
            parsed_data = json.loads(data)

            # Format the data for CSV
            formatted_data = {
                "SensorName": parsed_data.get("SensorName", ""),
                "Timestamp": parsed_data.get("Timestamp", 0),
                "x": parsed_data.get("x", 0.0),
                "y": parsed_data.get("y", 0.0),
                "z": parsed_data.get("z", 0.0),
            }
            #print(formatted_data)
            await save_global_data(global_data)  # Save data to global.csv asynchronously





# Contribution by Evan Johnston
async def run_SSS():
    async with websockets.serve(echo, '0.0.0.0', 5000, max_size=1_000_000_000):
        await asyncio.Future()
    



asyncio.run(run_SSS())
asyncio.run(save_global_data(global_data))

