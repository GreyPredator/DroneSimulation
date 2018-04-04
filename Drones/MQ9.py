from Drones import Drone
from Weaponeering import HardPoint
from GeoSpatial import Location
from GeoSpatial import FlightPath
from Strike import Mission


class MQ9(Drone):

    def __init__(self, IDNumber):
        self.__IDNumber = IDNumber
        self.__Model = 'MQ-9 Reaper'
        self.__Length = 36
        self.__WingSpan = 65.5
        self.__Height = 12.5
        self.__WingArea = 153
        self.__AspectRatio = 19.0
        self.__EmptyWeight = 4901
        self.__MaxTakeoffWeight = 10494
        self.__MaxSpeed = 300
        self.__CruiseSpeed = 194
        self.__StallSpeed = 100
        self.__OpRange = 1151
        self.__Endurance = 14
        self.__Ceiling = 50000
        self.__FuelCapacity = 100
        self.__HardPoint1 = HardPoint(None)
        self.__HardPoint2 = HardPoint(None)
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