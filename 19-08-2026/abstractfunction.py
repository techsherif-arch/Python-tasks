from abc import ABC, abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


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
