from boltiot import Bolt
bolt = open(r'C:\Users\haneef\Documents\Cerdentials\bolt_iot.txt').read()
device_id, api_key = bolt.split()

mybolt = Bolt(api_key, device_id)

'''
pin 0 & intensity level 10
Intensity ranges from (0,255)
analogWrite('pin numer', 'intensity value')
'''
response = mybolt.analogWrite('0', '10')
print(response)
