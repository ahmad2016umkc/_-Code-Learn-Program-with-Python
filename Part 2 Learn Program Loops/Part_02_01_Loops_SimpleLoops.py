# Every program has the ability to perform actions on a list of
# values. The for loop can be used to do this.
 
# Each time we go through the loop variable i's value will be
# assigned the next value in our list
 
for i in [2,4,6,8,10]:
    print "i = ", i
 
# We can also have range define our list for us. range(10) will
# create a list starting at 0 and go up to but not include
# the value passed to it.
 
for i in range(10):
    print "i = ", i
 
# We can define the starting and ending value for range
for i in range(2, 10):
    print "i = ", i
 
# You can use modulus to see if a number is odd or even
# If we divide an even by 2 there will be no remainder
# so if i % 2 == 0 we know it is true
i = 2
print((i % 2) == 0)