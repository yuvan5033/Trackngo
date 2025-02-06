import IOT
import random

Transmission = IOT.transmission()

Transmission.GPS="1.1.1.1"
Transmission.Bus_id="VJA4045"
Transmission.Headcount= random.randint(1,100)
Transmission.supabase_KEY="hxapasboisefbasrgsg"
Transmission.supabase_URL="dasdgkasgb.supabase.co"

print(Transmission.supabase_KEY)
print(Transmission.supabase_URL)
print(Transmission.GPS + Transmission.Bus_id + str(Transmission.Headcount))