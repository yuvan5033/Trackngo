import IOT
import ML
import random

Transmissions = IOT.Transmission()

Transmissions.GPS="1.1.1.1"
Transmissions.Bus_id="VJA4045"
Transmissions.Headcount= random.randint(1,100)
Transmissions.supabase_KEY="hxapasboisefbasrgsg"
Transmissions.supabase_URL="dasdgkasgb.supabase.co"

print(Transmissions.supabase_KEY)
print(Transmissions.supabase_URL)
print(Transmissions.GPS + Transmissions.Bus_id + str(Transmissions.Headcount))