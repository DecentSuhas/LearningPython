import json

# The process of encoding JSON is usually called "serialization". This term refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network

# Select all and press Ctrl + Alt + L in the json file to format it.

referral_token = {
    "access_token": "3E6RAHCN2LCGJML5QQL5RC6GK4",
    "expires_in": 63072000,
    "scopes": [
        "UPDATE_PROFILE"
    ]
}

ebooks_details = '''{
   "eBooks":[
      {
         "language":"Pascal",
         "edition":"third"
      },
      {
         "language":"Python",
         "edition":"four"
      },
      {
         "language":"SQL",
         "edition":"second"
      }
   ]
}
'''
def write_to_json():
    with open("sample.json", 'w') as write_file:
        json.dump(referral_token,write_file)


data = json.loads(ebooks_details)
for i in data['eBooks']:
    print(i)