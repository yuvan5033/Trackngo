import random

class GPSReader:
    def __init__(self):
        print("GPS Reader initialized with placeholder data.")

    def read_gps_data(self):
        # Generating random lat/long placeholders
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        return {"latitude": latitude, "longitude": longitude}
