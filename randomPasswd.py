
import random


#All chars separated
chars1 = "abcdefgijklmnopqrstuvwxyz"
chars2 = "1234567890"
chars3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars4 = "!@#$%^&*()_+-/{}[].,"

#merged chars
simple = chars1 + chars3
medium = chars1 + chars2 + chars3
strong = chars1 + chars2 + chars3 + chars4

#explanation of whats what
print("Simple - Upper cases + lower cases")
print("Medium - Upper cases + lower cases + digits")
print("Strong - Upper cases + lower cases + digits + symbols")

#variables:
#Passwd strength
x = input("Simple type - 1 ; Medium type - 2 ; Strong type - 3 : ")

#Passwd length
passwd_length = input("Password length: ")
passwd_length = int(passwd_length)

#if statement depending on choosing password strength
#Simple
if int(x) == 1 :
    password = []
    for x in range(passwd_length):
        password.append(random.choice(simple))
    print(''.join(password))

#Medium
if int(x) == 2 :
    password = []
    for x in range(passwd_length):
        password.append(random.choice(medium))
    print(''.join(password))

#Strong
if int(x) == 3 :
    password = []
    for x in range(passwd_length):
        password.append(random.choice(strong))
    print(''.join(password))



