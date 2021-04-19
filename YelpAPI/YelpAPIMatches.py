# API Key : 1LqpJ4tRJ__j7bh1p7A8YT8K-YjWlKJSt6KExuLd1wvRk9u1i4r7s76GfoMkIn6gOv3TUudS6_-kgO92MpCcosmPRK3PwS4fv1PDRD6KXwd-LaaeHi0GcuJR1kkXX3Yx
# Client ID : ej-MTJB4iqecM0Kxpc4ggA

#import modules 
import requests 
from YELP_API import get_my_key 

#Define a buisness ID 
business_id = "WavvLdfdP6g8aZTtbBQHTw"

#Define the API key, Define the endpoint, Define the header 
API_KEY = get_my_key()
ENDPOINT = 'https://api.yelp.com/v3/businesses/matches'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Define the parameters 
PARAMETERS = {'name': 'Peets Coffee & Tea' ,
              'address1': '7845 Highland Village Pl',
              'city' : 'San Diego',
              'state' : 'CA'
              'country' : 'US' }

#Make a request to the yelp API 
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

#convert the JSON string to a Dictonary 
buisness_data = response.json()

print(buisness_data.keys())

for biz in buisness_data['buisness']:
    print biz(['name'])


