# random password generator

import random

password = ""

for i in range(3): # will run through 3x ( each = 3characters, so = 15 total )
    
    i = chr(random.randint(65, 90)) # ASCII 65-90 : A-Z
    j = chr(random.randint(65, 90)).lower() # lowercase
    k = random.randint(0, 10) # random numbers
    
    password = str(password) + i + j + str(k)
    
print(password)