#from AI import *
#from DataProcessing import *
#from GUI import *
from InfluxDB_RD import *
#from InfluxDC_PD import *
from SSS import *
import subprocess

async def main():
    SSS_task = asyncio.create_task(activate_SSS())

    # Create InfluxDB JSON object:
    influx_data = [
        {
        "measurement": "measurement_name",
        "time": "timestamp",
        "fields": {
            "SensorName": ("SensorName", ""),
            "x": float(("x", 0.0)),
            "y": float(("y", 0.0)),
            "z": float(("z", 0.0)),
                    }
        }
        ]

    data = influx_data

    send_to_influxdb(data)

    await asyncio.Future()
