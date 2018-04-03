class Drone:
    '''This is the base class for all drones'''

    def __init__(self, IDNumber, Model, Length, WingSpan, Height, WingArea,
                 AspectRatio, EmptyWeight, MaxTakeOffWeight,
                 MaxSpeed, CruiseSpeed, StallSpeed,
                 OpRange, Endurance, Ceiling, FuelCapacity,
                 HardPoint1, HardPoint2, HardPoint3, HardPoint4, HardPoint5, HardPoint6,
                 Speed, Altitude, FuelRemaining, isAirborne, isLanded, Location, OpStatus, FlightPath, Mission):
        #  Drone Specification Data Fields
        self.__IDNumber = IDNumber
        self.__Model = Model
        self.__Length = Length
        self.__WingSpan = WingSpan
        self.__Height = Height
        self.__WingArea = WingArea
        self.__AspectRation = AspectRatio
        self.__EmptyWeight = EmptyWeight
        self.__MaxTakeoffWeight = MaxTakeOffWeight
        self.__MaxSpeed = MaxSpeed
        self.__CruiseSpeed = CruiseSpeed
        self.__StallSpeed = StallSpeed
        self.__OpRange = OpRange
        self.__Endurance = Endurance
        self.__Ceiling = Ceiling
        self.__FuelCapacity = FuelCapacity
        self.__HardPoint1 = HardPoint1
        self.__HardPoint2 = HardPoint2
        self.__HardPoint3 = HardPoint3
        self.__HardPoint4 = HardPoint4
        self.__HardPoint5 = HardPoint5
        self.__HardPoint6 = HardPoint6

        # Drone Operation Data Fields
        self.__Speed = Speed
        self.__Altitude = Altitude
        self.__FuelRemaining = FuelRemaining
        self.__isAirborne = isAirborne
        self.__isLanded = isLanded
        self.__Location = Location
        self.__OpStatus = OpStatus
        self.__FlightPath = FlightPath
        self.__Mission = Mission

    # GETTERS

    def getIDNumber(self):
        return self.__IDNumber

    def getModel(self):
        return self.__Model

    def getLength(self):
        return self.__Length

    def getWingSpan(self):
        return self.__WingSpan

    def getHeight(self):
        return self.__Height

    def getWingArea(self):
        return self.__WingArea

    def getAspectRatio(self):
        return self.__AspectRation

    def getEmptyWeight(self):
        return self.__EmptyWeight

    def getMaxTakeOffWeight(self):
        return self.__MaxTakeOffWeight

    def getMaxSpeed(self):
        return self.__MaxSpeed

    def getCruiseSpeed(self):
        return self.__CruiseSpeed

    def getStallSpeed(self):
        return self.__StallSpeed

    def getOpRange(self):
        return self.__OpRange

    def getEndurance(self):
        return self.__Endurance

    def getCeiling(self):
        return self.__Ceiling

    def getFuelCapacity(self):
        return self.__FuelCapacity

    def getHardPoint1(self):
        return self.__HardPoint1

    def getHardPoint2(self):
        return self.__HardPoint2

    def getHardPoint3(self):
        return self.__HardPoint3

    def getHardPoint4(self):
        return self.__HardPoint4

    def getHardPoint5(self):
        return self.__HardPoint5

    def getHardPoint6(self):
        return self.__HardPoint6

    def getAltitude(self):
        return self.__Altitude

    def getFuelRemaining(self):
        return self.__FuelRemaining

    def getisAirborne(self):
        return self.__isAirborne

    def getisLanded(self):
        return self.__isLanded

    def getLocation(self):
        return self.__Location

    def getOpStatus(self):
        return self.__OpStatus

    def getFlightPath(self):
        return self.__FlightPath

    def getMission(self):
        return self.__Mission

    # SETTERS

    def setIDNumber(self, v):
        self.__IDNumber = v

    def setModel(self, v):
        self.__Model = v

    def setLength(self, v):
        self.__Length = v

    def setWingSpan(self, v):
        self.__WingSpan = v

    def setHeight(self, v):
        self.__Height = v

    def setWingArea(self, v):
        self.__WingArea = v

    def setAspectRatio(self, v):
        self.__AspectRation = v

    def setEmptyWeight(self, v):
        self.__EmptyWeight = v

    def setMaxTakeOffWeight(self, v):
        self.__MaxTakeOffWeight = v

    def setMaxSpeed(self, v):
        self.__MaxSpeed = v

    def setCruiseSpeed(self, v):
        self.__CruiseSpeed = v

    def setStallSpeed(self, v):
        self.__StallSpeed = v

    def setOpRange(self, v):
        self.__OpRange = v

    def setEndurance(self, v):
        self.__Endurance = v

    def setCeiling(self, v):
        self.__Ceiling = v

    def setFuelCapacity(self, v):
        self.__FuelCapacity = v

    def setHardPoint_1(self, v):
        self.__HardPoint_1 = v

    def setHardPoint_2(self, v):
        self.__HardPoint_2 = v

    def setHardPoint_3(self, v):
        self.__HardPoint_3 = v

    def setHardPoint_4(self, v):
        self.__HardPoint_4 = v

    def setHardPoint_5(self, v):
        self.__HardPoint_5 = v

    def setHardPoint_6(self, v):
        self.__HardPoint_6 = v

    def setAltitude(self, v):
        self.__Altitude = v

    def setFuelRemaining(self, v):
        self.__FuelRemaining = v

    def setisAirborne(self, v):
        self.__isAirborne = v

    def setisLanded(self, v):
        self.__isLanded = v

    def setLocation(self, v):
        self.__Location = v

    def setOpStatus(self, v):
        self.__OpStatus = v

    def setFlightPath(self, v):
        self.__FlightPath = v

    def setMission(self, v):
        self.__Mission = v

    # Drone Operations

    def takeOff(self):
        self.Altitude = 1000
        self.isAirborne = True

    def land(self):
        self.Altitude = 0
        self.isLanded = True

    def moveTo(self, pos):
        pass

    def loiter(self, t):
        pass

    def attack(self, tgt):
        pass

    def surveil(self, tgt):
        pass

    def refuel(self):
        pass
