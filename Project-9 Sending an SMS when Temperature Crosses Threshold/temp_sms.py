import conf
from boltiot import Sms, Bolt
import json
import time


minimum_limit = 30  # minimum temperature limit
maximum_limit = 39  # maximum temperature limit


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)


while True:
    print("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    sensor_value = int(data['value'])
    Temperature = (100*sensor_value)/1024
    print(f"Temperature is :  {Temperature: .2f}")
    #print("Sensor value is: " + str(data['value']))
    try:
        if Temperature > maximum_limit or Temperature < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms(
                f"The Current temperature is :{Temperature: .2f}")
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e:
        print("Error occured: Below are the details")
        print(e)
    time.sleep(10)
