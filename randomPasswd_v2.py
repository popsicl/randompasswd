import random

# Chars for specific passwords
chars1 = "abcdefgijklmnopqrstuvwxyz"
chars2 = "1234567890"
chars3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars4 = "!@#$%^&*()_+-/{}[].,"
adsymbols = "!@#$^&*"

# merged chars
simple = chars1 + chars3
medium = chars1 + chars2 + chars3
strong = chars1 + chars2 + chars3 + chars4
adpass = chars1 + chars2 + chars3 + adsymbols


# Full password gen
def password_checker():
    # Choices
    print("Simple - Upper cases + lower cases")
    print("Medium - Upper cases + lower cases + digits")
    print("Strong - Upper cases + lower cases + digits + symbols")
    print("Active Directory - Upper cases + lower cases + digits + symbols")
    # Loop password gen until it gets false output
    while True:
        # choice of password
        x = input("Simple type - 1 ; Medium type - 2 ; Strong type - 3 ; Active Directory - 4 : ")
        # Simple pass
        if int(x) == 1:
            passwd_length = input("Password length: ")
            passwd_length = int(passwd_length)
            password = []
            for x in range(passwd_length):
                password.append(random.choice(simple))
            print(''.join(password))
            # Choice for another password generation
            print("Need another? If yes press Y/y, if no press any key:")
            answer = input("Input: ")
            if answer == "Y":
                print("Choose another")
            elif answer == "y":
                print("Choose another")
            else:
                print("Thank you for using :)")
                break

        # Medium pass
        elif int(x) == 2:
            passwd_length = input("Password length: ")
            passwd_length = int(passwd_length)
            password = []
            for x in range(passwd_length):
                password.append(random.choice(medium))
            print(''.join(password))
            # Choice for another password generation
            print("Need another? If yes press Y/y, if no press any key:")
            answer = input("Input: ")
            if answer == "Y":
                print("Choose another")
            elif answer == "y":
                print("Choose another")
            else:
                print("Thank you for using :)")
                break

        # Strong pass
        elif int(x) == 3:
            passwd_length = input("Password length: ")
            passwd_length = int(passwd_length)
            password = []
            for x in range(passwd_length):
                password.append(random.choice(strong))
            print(''.join(password))
            # Choice for another password generation
            print("Need another? If yes press Y/y, if no press any key:")
            answer = input("Input: ")
            if answer == "Y":
                print("Choose another")
            elif answer == "y":
                print("Choose another")
            else:
                print("Thank you for using :)")
                break

        # AD pass
        elif int(x) == 4:
            passwd_length = input("Password length: ")
            passwd_length = int(passwd_length)
            password = []
            for x in range(passwd_length):
                password.append(random.choice(adpass))
            print(''.join(password))
            # Choice for another password generation
            print("Need another? If yes press Y/y, if no press any key:")
            answer = input("Input: ")
            if answer == "Y":
                print("Choose another")
            elif answer == "y":
                print("Choose another")
            else:
                print("Thank you for using :)")
                break
        # If x input is not recognized brings back to first choice.
        else:
            print("Invalid input, choose again.")


password_checker()
