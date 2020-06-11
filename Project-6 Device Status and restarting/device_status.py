from boltiot import Bolt
bolt = open(r'C:\Users\haneef\Documents\Cerdentials\bolt_iot.txt').read()
device_id, api_key = bolt.split()

mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print(response)
