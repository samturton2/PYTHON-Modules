import requests
import json

# live_response = requests.get("https://api.postcodes.io/postcodes/nw21re")
#
# argument = str(input("please enter your postcode "))
#
# # convert live response into dictionary
# print(live_response.json()) # .json() used to convert a bytes object to a python dictionary
# print(json.loads(live_response.content)) # json.loads() used to convert a javascript dictionary into a python dictionary

# Create a function that returns the longitude and latitude
def long_and_lat():
    # Enter postcode into the website
    postcode = input("Whats your postcode?\n=>").lower().replace(" ", "")
    l_resp = requests.get("https://api.postcodes.io/postcodes/" + postcode)

    # check the status code, to see if webpage is found
    try:
        if l_resp.status_code == requests.codes.ok:
            result = l_resp.json()['result']  # Convert to a python dictionary and retrieve the results dictionary
            longitude = result['longitude']
            latitude = result["latitude"]
            # return the longitude and latitude from the dictionary
            return f"longitude: {longitude}, latitude: {latitude}"
        elif l_resp.status_code == requests.codes.not_found:  # This checks for if not 200-400 status code
            print("This site is unavailable until further notice.")
    except:
        print("OOPs something went wrong please try later")

print(long_and_lat())