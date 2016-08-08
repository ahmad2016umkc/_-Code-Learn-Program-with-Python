# ---------- MAKE A isfloat FUNCTION ----------
# There is no way to check if a string contains a float
# so let's make one by defining our own function
# Functions allow use to avoid repeating code
# They can receive values (attributes / parameters)
# They can return values
# You define your function name and the names for the values
# it receives like this
 
from __future__ import print_function

def isfloat(str_val):
    try:
 
        # If the string isn't a float float() will throw a
        # ValueError
        float(str_val)
 
        # If there is a value you want to return use return
        return True
    except ValueError:
        return False
 
pi = "3.14"
 
# We call our functions by name and pass in a value between
# the parentheses
print("Is Pi a Float :", isfloat(pi))