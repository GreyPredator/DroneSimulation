from GeoSpatial import FlightPath
from Targeting import Target


class Mission:

    def __init__(self, IDNumber, Type, FlightPath, Target, LaunchTime, OPStatus):
        self.__IDNumber = IDNumber
        self.__Type = Type
        self.__FlightPath = FlightPath
        self.__Target = Target
        self.__LaunchTime = LaunchTime
        self.__OPStatus = OPStatus

    def getIDNumber(self):
        return self.__IDNumber

    def getType(self):
        return self.__Type

    def getFlightPath(self):
        return self.__FlightPath

    def getTarget(self):
        return self.__Target

    def getLaunchTime(self):
        return self.__LaunchTime

    def getOPStatus(self):
        return self.__OPStatus

    def setIDNumber(self, v):
        self.__IDNumber = v

    def setType(self, v):
        self.__Type = v

    def setFlightPath(self, v):
        self.__FlightPath = v

    def setTarget(self, v):
        self.__Target = v

    def setLaunchTime(self, v):
        self.__LaunchTime = v

    def setOPStatus(self, v):
        self.__OPStatus = v