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



