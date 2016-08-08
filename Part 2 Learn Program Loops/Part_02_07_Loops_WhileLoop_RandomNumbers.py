# ---------- THE WHILE LOOP ----------
# We can also continue looping as long as a condition is true
# with a while loop
 
# While loops are used when you don't know how many times
# you will have to loop
 
# We can use the random module to generate random numbers
import random
 
# Generate a random integer between 1 and 50
rand_num = random.randrange(1, 51)
 
# The value we increment in the while loop is defined before the loop
i = 1
 
# Define the condition that while true we will continue looping
while (i != rand_num):
 
    # You must increment your iterator inside the while loop
    i += 1
 
# Outside of the while loop when we stop adding whitespace
print "The random value is : ", rand_num 