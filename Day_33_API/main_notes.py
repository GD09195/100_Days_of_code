import requests
#requests documentation = requests.readthedocs.io/en/master

#Getting the data from the endpoint. Endpoint goes in url= argument
response = requests.get(url='http://api.open-notify.org/iss-now.json')
#response = <Response [200]>

#Raise an exception if the Status is not successful
response.raise_for_status()

#Response status code
print(response.status_code)
"""
HTTP status codes.  
#httpstatuses.com

1XX: Hold on
2XX: Here you go. Successfully
3XX: Go Away. Don't have the permission.
4XX: you Screwed up. Client side Error.
5XX: I Screwed up. Service side error.
"""

#Accessing the response Json content
print(type(response.json()))