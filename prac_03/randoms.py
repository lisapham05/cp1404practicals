import random

print(random.randint(5,20))  # line 1
"""
Line 1:
I saw 12, 11, 7, 10,...
Smallest possible: 5
Largest possible: 20
Randint(a,b) includes both endpoints a and b
"""

print(random.randrange(3,10,2))  # line 2
"""
Line 2:
I saw 5, 3, 7, 9
Smallest possible: 3
Largest possible: 9
Line 2 could not produce a 4
randrange(3,10,2) has step = 2 from start, so it gives values 3,5,7,9
"""

print(random.uniform(2.5,5.5))  # line 3
"""
Line 3: 
I saw 4.24178837067064, 5.287014182540678, 5.20274442094182,...
Smallest possible: 2.5
Largest possible: 5.5
uniform(a,b) gives a float in [a,b] inclusive
"""

# Generate a random number between 1 and 100 inclusive
print(random.randint(1, 100))

