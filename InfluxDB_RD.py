# Token Raw Data Base: 9Yr6JOBQLsfn5gRFmBkdG__nA-Z35Xcp5dBMnbtO4gf4yKuzFfe1j_isyCP-NWLlHErlWg_3autk65P_P_xNxg==
import os, time
from influxdb_client_3 import InfluxDBClient3, Point, WriteOptions
import pandas


token = "9Yr6JOBQLsfn5gRFmBkdG__nA-Z35Xcp5dBMnbtO4gf4yKuzFfe1j_isyCP-NWLlHErlWg_3autk65P_P_xNxg=="
org = "DSP"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(
  host=host, 
  token=token, 
  org=org,

)

database="InfluxDB_RD"

def send_to_influxdb(data):
    try:
        # Write data to InfluxDB
        client.write_points(data)
        print("Data sent to InfluxDB succesfully.")
    except Exception as e:
        print(f"Error sending data to InfluxDB: {e}")


        ### New text written 22(23.3)
### SO what if I change this one...