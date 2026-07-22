room = input("Is the room available? (yes/no):")
if room == "yes":
    payment = input("Is the payment completed? (yes/no):")
    if payment == "yes":
        print("Booking Confirmed")
    else:
        print("Please Complete the Payment")
else:
    print("No Rooms Available")
