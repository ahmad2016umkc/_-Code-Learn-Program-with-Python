# ---------- ACCURATE FLOATING POINT CALCULATIONS ----------
 
# The decimal module provides for more accurate floating point calculations
# With from you can reference methods without the need to reference the module
# like we had to do with math above
# We create an alias being D here to avoid conflicts with methods with
# the same name
from decimal import Decimal as D
 
sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print "Sum Using Decimal = ", sum 
print "0.1+0.1+0.1-0.3 =", 0.1+0.1+0.1-0.3