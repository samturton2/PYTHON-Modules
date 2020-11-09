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
