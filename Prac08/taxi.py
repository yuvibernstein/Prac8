"""
CP1404/CP5632 Practical
Car class
modified by Yuvi
"""

import random
class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    price_per_km = 1.2
    fanciness = 1

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), Taxi.price_per_km,
                                                             self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        return Taxi.price_per_km * self.current_fare_distance * self.fanciness

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

class UnreliableCar(Car):
    def __init__(self, fuel):
        super().__init__(self, fuel)
        self.reliability = 70

    def drive(self, distance):
        random_num = random.randrange (0,100,1)
        if random_num >= self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven

class SilverServiceTaxi(Taxi):
    fanciness = 2
    price_per_km = 1.2 * fanciness
    flagfall = 4.50
    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def get_fare(self):
        Taxi.get_fare(self)

    def start_fare(self):
        Taxi.start_fare(self)

    def drive(self, distance):
        Taxi.drive(self,distance)
