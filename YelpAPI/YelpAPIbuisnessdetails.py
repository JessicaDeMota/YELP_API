# API Key : 1LqpJ4tRJ__j7bh1p7A8YT8K-YjWlKJSt6KExuLd1wvRk9u1i4r7s76GfoMkIn6gOv3TUudS6_-kgO92MpCcosmPRK3PwS4fv1PDRD6KXwd-LaaeHi0GcuJR1kkXX3Yx
# Client ID : ej-MTJB4iqecM0Kxpc4ggA

#import modules 
import requests 


#Define a buisness ID 
business_id = "WavvLdfdP6g8aZTtbBQHTw"

#Define the API key, Define the endpoint, Define the header 
API_KEY ="1LqpJ4tRJ__j7bh1p7A8YT8K-YjWlKJSt6KExuLd1wvRk9u1i4r7s76GfoMkIn6gOv3TUudS6_-kgO92MpCcosmPRK3PwS4fv1PDRD6KXwd-LaaeHi0GcuJR1kkXX3Yx"
ENDPOINT = 'https://api.yelp.com/v3/businesses/{ }'.format(business_id)
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Define the parameters 
#PARAMETERS = {"phone": "+14159083801"}

#Make a request to the yelp API 
response = requests.get(url = ENDPOINT, headers = HEADERS)

#convert the JSON string to a Dictonary 
buisness_data = response.json()

print(buisness_data.keys())

#f#or biz in buisness_data['buisness']:
    #print biz(['name'])


