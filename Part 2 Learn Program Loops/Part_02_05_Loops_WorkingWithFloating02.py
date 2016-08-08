# ---------- WORKING WITH FLOATS ----------
# When working with floats understand that they are not precise
 
# This should print 0 but it doesn't
i = 0.1 + 0.1 + 0.1 - 0.3
print(i)
 
# Floats will print nonsense beyond 16 digits of precision
i = .11111111111111111111111111111111
j = .00000000000000010000000000000001
 
print("Answer : {:.32}".format(i + j))