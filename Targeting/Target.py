class Target:

    def __init__(self, IDNumber, Type, Location, Priority, isMobile, Size, Status, Value, Age, Description):
        self.__IDNumber = IDNumber
        self.__Type = Type
        self.__Location = Location
        self.__Priority = Priority
        self.__isMobile = isMobile
        self.__Size = Size
        self.__Status = Status
        self.__Value = Value
        self.__Age = Age
        self.__Description = Description

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

    def getSize(self):
        return self.__Size

    def getStatus(self):
        return self.__Status

    def getValue(self):
        return self.__Value

    def getAge(self):
        return self.__Age

    def getDescription(self):
        return self.__Description

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

    def setSize(self, v):
        self.__Size = v

    def setLength(self, v):
        self.__Length = v

    def setWidth(self, v):
        self.__Width = v

    def setStatus(self, v):
        self.__Status = v

    def setValue(self, v):
        self.__Value = v

    def setAge(self, v):
        self.__Age = v

    def setDescription(self, v):
        self.__Description = v
