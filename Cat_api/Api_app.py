# Import all relevant libraries

import requests
import json
import sys

# Assign variables to the search api items, such as the url, api_key, etc.
url = "https://api.thecatapi.com/v1/breeds/search?q=beng"
api_key = "35dba75e-8d9e-4bc1-8500-0a2ac39a56d8"
headers = {'Accept': 'application/json'}
# use the requests. get function to extract data
response = requests.get(url, api_key, headers=headers)
# extract data in json(The api data is already in json data form)
# assign variable to extracted data
cat_data = response.json()
# print(response.status_code)
# to print data in json format

# change the json data to string...
newcat_data = json.dumps(cat_data)
# now convert json object to dictionary...
json_to_dict = json.loads(newcat_data)
# to check if json data is in the right format print.
print(json_to_dict)

# now create a javascript file using python...
sys.stdout = open('cat_api.js', 'w')
print('var cat_data2 = {}'.format(json_to_dict))
