# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# Initial commit

# Base Class Vehicle
class Vehicle(object):
    pass

# Child Class GroundVehicle which inherits from Vehicle class
class GroundVehicle(Vehicle):
    pass

# Child class Car which inherits from GroundVehicle class
class Car(GroundVehicle):
    pass

# class Motorcycle which inherits from GroundVehicle class
class Motorcycle(GroundVehicle):
    pass

# Child class FlightVehicle which inherits from Vehicle class
class FlightVehicle(Vehicle):
    pass

# Child class Airplane which inherits from FlightVehicle
class Airplane(FlightVehicle):
    pass

# Child class Starship which inherits from FlightVehicle
class Starship(FlightVehicle):
    pass
