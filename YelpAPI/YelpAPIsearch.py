#Client ID :ej-MTJB4iqecM0Kxpc4ggA
#API Key : 1LqpJ4tRJ__j7bh1p7A8YT8K-YjWlKJSt6KExuLd1wvRk9u1i4r7s76GfoMkIn6gOv3TUudS6_-kgO92MpCcosmPRK3PwS4fv1PDRD6KXwd-LaaeHi0GcuJR1kkXX3Yx

#import modules 
import requests 

#Define a buisness ID 
business_id = "WavvLdfdP6g8aZTtbBQHTw"

#Define the API key, Define the endpoint, Define the header 
API_KEY = "1LqpJ4tRJ__j7bh1p7A8YT8K-YjWlKJSt6KExuLd1wvRk9u1i4r7s76GfoMkIn6gOv3TUudS6_-kgO92MpCcosmPRK3PwS4fv1PDRD6KXwd-LaaeHi0GcuJR1kkXX3Yx"
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Define the parameters 
PARAMETERS = {'term':"coffee",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
              'limit' : 50,
              'radius' : 10000,
              'offset' : 50,
              'location' : 'San Diego'}

#Make a request to the yelp API 
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

#convert the JSON string to a Dictonary 
business_data = response.json()

print(business_data)

for biz in business_data['businesses']:
    print(biz['name'])

