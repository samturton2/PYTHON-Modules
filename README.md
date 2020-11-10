# This lesson covers python modules

- Built in functions
- Python Library
- What is pip and how do we use it 
- APIs with Python

- Built in functions help us accelerate the development of our software.


- To find the out system path
- When and why should we do it
- Creating a customised method to add required information and use the functionality provided by sys module
``` 
def current_system_path():
    print("this is your current directory")
    return sys.path

print(current_system_path()) 
```

### What is pip
- package manager for python and helps us install external packages
such as requests
- syntax: pip install name_of_package


### API with requests

![](/CRUD.png)


## Json basics
- Java script object notation
- use cases - browser data
- data is in key value pairs
- Json encoding from a Dictionary
- Json decoding into a Dictionary
- handling/creating files with python
- writing to file
- reading from file


#### Exception handling
syntax 
```python
try: # If no error occurs
    raise: # can raise an error of your choice in the raise section
except: # Except when this error occurs (can specify
else: # Occurs if no errors raised
finally: # always happens no matter what
```

- **use cases**
- we use these blocks when we expect an error or an exception from python interpreter
- why - this helps us handle the `errors` or `exception` and add customised message as awell as a make a decision based on the customer needs.

- We will create a variable to store a file using ```open()```
**iteration 1**
```python
try: # lets use try block for a 1 line of code where we know this will throw an error
    file = open("orders.text")
except:
    print("Panic alert !! ")
```
**Iteration 2 using `raise` and `finally`**
```python
try:
    file = open("orders.text")
except FileNotFoundError as errmsg: # creating alias for file not found error
    print("please create a file first.  " + str(errmsg))
# if we still wanted them to see the actual exception
    raise # will send back the actual exception
finally: #finally will execute regardless of above conditions
    print("Hope you had a good customer experience")
```