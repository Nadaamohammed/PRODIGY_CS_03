def checkPasswordStreght(password):
    upper = 0
    lower = 0
    digits = 0
    special_char = 0
    length = len(password)

    if (length < 6):
        print("Password must be at least 6 characters long!\n")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upper += 1
            elif (password[i].islower()):
                lower += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                special_char += 1

    if (upper != 0 and lower != 0 and digits != 0 and special_char != 0):
        if (length >= 10):
            print("The strength of password is strong.\n")
        else:
            print("The strength of password is medium.\n")
    else:
        if (upper == 0):
            print("Password must contain at least one uppercase character!\n")
        if (lower == 0):
            print("Password must contain at least one lowercase character!\n")
        if (special_char == 0):
            print("Password must contain at least one special character!\n")
        if (digits == 0):
            print("Password must contain at least one digit!\n")

print("password must be contain at leat 6 char(upper, lower), digits, special char ")
password = input("Please enter password: ")
checkPasswordStreght(password)