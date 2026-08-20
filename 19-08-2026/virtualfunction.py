class vehicle:
    def start(self):
        print("vehicle is starting")


class car(vehicle):
    def start(self):
        print("car starts with key")


class bike(vehicle):
    def start(self):
        print("bike starts with button")


v1 = car()
v2 = bike()

v1.start()
v2.start()
