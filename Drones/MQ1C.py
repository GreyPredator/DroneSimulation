from Drones import Drone
from Weaponeering import HardPoint
from GeoSpatial import Location
from GeoSpatial import FlightPath
from Strike import Mission

class MQ1C(Drone):

    def __init__(self, IDNumber):
        self.__IDNumber = IDNumber
        self.__Model = 'MQ-1C Gray Eagle'
        self.__Length = 28
        self.__WingSpan = 56
        self.__Height = 7
        self.__WingArea = 123.3
        self.__AspectRatio = 19.0
        self.__EmptyWeight = 1130
        self.__MaxTakeoffWeight = 2250
        self.__MaxSpeed = 167
        self.__CruiseSpeed = 100
        self.__StallSpeed = 62
        self.__OpRange = 675
        self.__Endurance = 25
        self.__Ceiling = 29000
        self.__FuelCapacity = 100
        self.__HardPoint1 = HardPoint(None)
        self.__HardPoint2 = HardPoint(None)
        self.__HardPoint1 = HardPoint(None)
        self.__HardPoint2 = HardPoint(None)

        # Drone Operation Data Fields
        self.__Speed = 0
        self.__Altitude = 0
        self.__FuelRemaining = 100
        self.__isAirborne = False
        self.__isLanded = True
        self.__Location = Location(0,0)
        self.__OpStatus = 'Landed'
        self.__FlightPath = FlightPath(None)
        self.__Mission = Mission