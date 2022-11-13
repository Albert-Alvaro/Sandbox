MINIMUM_LENGTH = 3

password = input("Password: ")
password_output = len(password)
while password_output < MINIMUM_LENGTH:
    print("Password length too short")
    password = input("Password: ")
    password_output = len(password)
print("*"*password_output)