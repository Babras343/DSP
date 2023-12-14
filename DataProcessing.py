import json

async def echo(websocket, path):
    async for message in websocket:
        try:
            # Parse JSON data
            data = json.loads(message)

            # Display data for each axis
            print(f"Sensor Name: {data.get('SensorName', 'Unknown')}")
            print(f"Timestamp: {data.get('Timestamp', 'Unknown')}")
            print(f"X-axis: {data.get('x', 0.0)}")
            print(f"Y-axis: {data.get('y', 0.0)}")
            print(f"Z-axis: {data.get('z', 0.0)}")
            print("=" * 20)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Error processing data: {e}")
