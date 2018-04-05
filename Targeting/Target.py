class Target:

    def __init__(self, IDNumber, Type, Location, Priority, isMobile, Length, Width, Status):
        self.__IDNumber = IDNumber
        self.__Type = Type
        self.__Location = Location
        self.__Priority = Priority
        self.__isMobile = isMobile
        self.__Length = Length
        self.__Width = Width
        self.__Status = Status

    def getIDNumber(self):
        return self.__IDNumber

    def getType(self):
        return self.__Type

    def getLocation(self):
        return self.__Location

    def getPriority(self):
        return self.__Priority

    def getisMobile(self):
        return self.__isMobile

    def getLength(self):
        return self.__Length

    def getWidth(self):
        return self.__Width

    def getStatus(self):
        return self.__Status

    def setIDNumber(self, v):
        self.__IDNumber = v

    def setType(self, v):
        self.__Type = v

    def setLocation(self, v):
        self.__Location = v

    def setPriority(self, v):
        self.__Priority = v

    def setisMobile(self, v):
        self.__isMobile = v

    def setLength(self, v):
        self.__Length = v

    def setWidth(self, v):
        self.__Width = v

    def getStatus(self, v):
        self.__Status = v
