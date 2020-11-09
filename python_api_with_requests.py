# importing requests to make an api to www

import requests
from emoji import emojize

live_response = requests.get("https://www.bbc.co.uk/")
# it provides in integer as a response code

print(live_response.headers)
print(type(live_response.content))

# First iteration
# if live_response.status_code == 200:
#     print("mission successful!!!" + str(live_response.status_code))
#     print(emojize(":thumbs_up:"))
# elif live_response.status_code == 404:
#     print("This site is unavailable untill further notice.")
# else:
#     print("OOPs something went wrong please try later")

# # Second iteration
# def check_response_code():
#     if live_response.status_code == 200:
#         print("mission successful!!!" + str(live_response.status_code))
#         print(emojize(":thumbs_up:"))
#     elif live_response.status_code == 404:
#         print("This site is unavailable until further notice.")
#     else:
#         print("OOPs something went wrong please try later")
#
# check_response_code()

# Third iteration
# What does request module bring to the table

def check_response_code():
    if live_response.status_code == requests.codes.ok:  # This checks for 200-400 as that would return boolean True
        print("mission successful!!!" + str(live_response.status_code))
        print(emojize(":thumbs_up:"))
    elif live_response.status_code == requests.codes.not_found:  # This checks for if not 200-400 as would return boolean False
        print("This site is unavailable until further notice.")
    else:
        print("OOPs something went wrong please try later")

check_response_code()
