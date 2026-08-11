#No parameter, No return type
def check():
    n = int(input("enter a number:"))
    if n % 2 == 0:
        print("even number")
    else:
        print("odd number")
check()
#With parameter, No return type
def check(n):
    if n % 2 == 0:
        print("even number")
    else:
        print("odd number")
num = int(input("enter a number: "))
check(num)
#With parameter, With return type
def check(n):
    if n % 2 == 0:
        return "even no"
    else:
        return "odd no"
n = int(input("enter number: "))
print(check(n))
#No parameter, With return type
def check():
    n = int(input("enter number: "))
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

print(check())
