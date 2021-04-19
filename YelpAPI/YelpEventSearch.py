# API Key : 1LqpJ4tRJ__j7bh1p7A8YT8K-YjWlKJSt6KExuLd1wvRk9u1i4r7s76GfoMkIn6gOv3TUudS6_-kgO92MpCcosmPRK3PwS4fv1PDRD6KXwd-LaaeHi0GcuJR1kkXX3Yx
# Client ID : ej-MTJB4iqecM0Kxpc4ggA

#import modules 
import requests 

#Define the buisness ID
event_id = 'oakland-saucy-oakland-restaurant-pop-up'

#Define the API key, Define the endpoint, Define the header 
API_KEY = "1LqpJ4tRJ__j7bh1p7A8YT8K-YjWlKJSt6KExuLd1wvRk9u1i4r7s76GfoMkIn6gOv3TUudS6_-kgO92MpCcosmPRK3PwS4fv1PDRD6KXwd-LaaeHi0GcuJR1kkXX3Yx"
ENDPOINT = 'https://api.yelp.com/v3/events'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Define the parameters 
PARAMETERS = {'location':: 'San Diego',
                'limit : 50'}


#Make a request to the yelp API 
response = requests.get(url = ENDPOINT, param = PARAMETERS, headers = HEADERS)


#convert the JSON string to a Dictonary 
event_data = response.json()

for event in (event_data['events']
    print (event_keys())

#figuring out which ones are free 
#for event in event_data ['events']:
    #print(event("is_free"))

#if we want to print out all the keys to see the attributes amongst it:
    #print(event_data.keys())

#if we want to print item id's 
    #print(event_data.items())

#if we want to see all the values 
    #print(event_data.values())