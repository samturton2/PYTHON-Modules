# let's have a look at some built in function in Python

# Import is the key word we use to call modules from Python Library

import random
import math
print(random.random())
# We have random method in python library which we use by importing

print(random.random())
# generates a float between 0-1

num_float = 23.44
print("floor method rounds the figure to the lower end")
print(math.floor(num_float))

print("ceil method rounds the figure to the higher end")
print(math.ceil(num_float))



# Task
# Get user input of a float number
# check if the number is lower than .50 then round the figure to the lower end
# check if the number is greater than .51 then round the figure to higher end
# example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end
# tips - get help online - python library

# float_number = float(input("input a float: "))
# if float_number - math.floor(float_number) <= 0.5:
#     float_number = math.floor(float_number)
# else:
#     float_number = math.ceil(float_number
# print(float_number))

import os
# to find out system configuration or system related information
# based on the information provided we can handle the user request
import math, datetime, sys # can import more than one in one line

working_dir = os.getcwd() #gets current directory

print(working_dir)

# lets find out the name of our os
# only available on linux
#print(os.uname())

# Let's count the number of CPUs
print(os.cpu_count())
# os.cpu_count() gives us the total number of CPUs in our system/os

print(datetime.datetime.today())
# datetime module gives us the ability to find the current date and time etc.

# To find the out system path
# When and why should we do it
def current_system_path():
    print("this is your current directory")
    return sys.path

print(current_system_path())