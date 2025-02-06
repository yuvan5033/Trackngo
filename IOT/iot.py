import time

class transmission:
    def __init__(self, GPS, Headcount, Bus_id):
        self.GPS = GPS
        self.Headcount = Headcount
        self.Bus_id = Bus_id
        print("Gps: ", self.GPS)
        print("Headcount: ", self.Headcount)
        print("Bus_id: ", self.Bus_id)
    
    def __init__(self, supabase_URL, supabase_KEY):
        self.supabase_URL = supabase_URL
        self.supabase_KEY = supabase_KEY

    def __init__(self):
        time.sleep(3)
        print("transmission successful")
