class WayPoint:

    def __init__(self, Name, Location):
        self.__Name = Name
        self.__Location = Location

    def getName(self):
        return self.__Name

    def setName(self, v):
        self.__Name = v

    def getLocation(self):
        return self.__Location

    def setLocation(self, v):
        self.__Location = v