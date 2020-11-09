# importing requests to make an api to www

import requests

live_response = requests.get("https://www.bbc.co.uk/")
# it provides in integer as a response code

if live_response == 200:
    print("mission successful!!!")
print(live_response.status_code)
