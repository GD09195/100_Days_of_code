from datetime import datetime

import requests
import datetime as dt

parameters_sunset = {
    'lat': 19.432057,
    'lng':-99.094975
    'formatted': 0
}

response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
response_sunset = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters_sunset)

response_iss.raise_for_status()
response_sunset.raise_for_status()

json_iss = response_iss.json()
json_sunset = response_sunset.json()


sunset = str(json_sunset['results']['sunrise'])
sunset_time = sunset.split('T')[1].split(':')
current_time = str(dt.datetime.now().time()).split(':')

print(sunset_time)
print(current_time)