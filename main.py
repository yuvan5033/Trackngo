
import time
import random
from IOT.gps import GPSReader
from IOT.iot import Transmitter

BUS_ID = "BUS_101"
TABLE_NAME = "Data"

if __name__ == "__main__":
    gps_reader = GPSReader()
    transmitter = Transmitter()

    try:
        while True:
            gps_coords = gps_reader.read_gps_data()
            lat = gps_reader.read_gps_data()["latitude"]
            lon = gps_reader.read_gps_data()["longitude"]
            headcount = random.randint(0, 40)  # Placeholder for ML occupancy detection
            success = transmitter.send_data(TABLE_NAME, BUS_ID, lat, lon , headcount)
            if success:
                print(f"Sent data: GPS={gps_coords}, Headcount={headcount}")
            time.sleep(5)  # Read and transmit data every 5 seconds

    except KeyboardInterrupt:
        print("Stopping the data transmission...")