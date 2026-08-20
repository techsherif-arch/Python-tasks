class InvalidPin(Exception):
    pass

pin = int(input("enter pin: "))

try:
    if pin == 5555:
        print("login successful")
    else:
        raise InvalidPin("wrong pin")

except InvalidPin as ex:
    print(ex)

print("thank u")
