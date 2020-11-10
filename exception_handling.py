# we will have a look at the practical use cases and implementation of try, excuse and finally

# # we will create a variable to store a file data using open()
# # Iteration 1
# try: # lets use try block for a 1 line of code where we know this will throw an error
#     file = open("orders.text")
# except:
#     print("Panic alert !! ")

# Iteration 2
try:
    file = open("orders.text")
except FileNotFoundError as errmsg: # creating alias for file not found error
    print("please create a file first.  " + str(errmsg))
# if we still wanted them to see the actual exception
    raise # will send back the actual exception
finally: #finally will execute regardless of above conditions
    print("Hope you had a good customer experience")
