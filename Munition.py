

class Munition:

    def __init__(self, Manufacturer, Cost, Weight, Length, Diameter, WarheadWeight, WarheadType, Engine, OpRange, Speed, Guidance):
        self.__Manufacturer = Manufacturer
        self.__Cost = Cost
        self.__Weight = Weight
        self.__Length = Length
        self.__Diameter = Diameter
        self.__WarheadWeight = WarheadWeight
        self.__WarheadType = WarheadType
        self.__Engine = Engine
        self.__OpRange = OpRange
        self.__Speed = Speed
        self.__Guidance = Guidance

    def getManufacturer(self):
        return self.__Manufacturer

    def getCost(self):
        return self.__Cost

    def getWeight(self):
        return self.__Weight

    def getLength(self):
        return self.__Length

    def getDiameter(self):
        return self.__Diameter

    def getWarheadWeight(self):
        return self.__WarheadWeight

    def getWarheadType(self):
        return self.__WarheadType

    def getEngine(self):
        return self.__Engine

    def getOpRange(self):
        return self.__OpRange

    def getSpeed(self):
        return self.__Speed

    def getGuidance(self):
        return self.__Guidance
