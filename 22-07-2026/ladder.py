level = int(input("Enter water tank level"))
if level == 100:
    print("Tank is Full")
elif level >= 85 and level <= 99:
    print("Tank is Almost Full")
elif level >= 75 and level <= 84:
    print("Tank is ThreedQuarter Full")
elif level >= 50 and level <= 74:
    print("Tank is Half Full")
elif level >= 25 and level <= 49:
    print("Tank is Quarter Full")
elif level == 0:
    print("Tank is Empty")
else:
    print("Invalid Water Level")
