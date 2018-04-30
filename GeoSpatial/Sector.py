from GeoSpatial.Location import Location


class Sector:

    def __init__(self, Name, UpperLeft, LowerLeft, UpperRight, LowerRight):
        self.__Name = Name
        self.__UpperLeft = UpperLeft
        self.__LowerLeft = LowerLeft
        self.__UpperRight = UpperRight
        self.__LowerRight = LowerRight

    def getName(self):
        return self.__Name

    def getUpperLeft(self):
        return self.__UpperLeft

    def getLowerLeft(self):
        return self.__LowerLeft

    def getUpperRight(self):
        return self.__UpperRight

    def getLowerRight(self):
        return self.__LowerRight

    def setName(self, v):
        self.__Name = v

    def setUpperLeft(self, v):
        self.__UpperLeft = v

    def setLowerLeft(self, v):
        self.__LowerLeft = v

    def setUpperRight(self, v):
        self.__UpperRight = v

    def setLowerRight(self, v):
        self.__LowerRight = v

    def displaySector(self):
        print('Sector: ' + self.__Name)
        print('Upper Left: ' + str(self.__UpperLeft.getX()) + ' , ' + str(self.__UpperLeft.getY()))
        print('Lower Left: ' + str(self.__LowerLeft.getX()) + ' , ' + str(self.__LowerLeft.getY()))
        print('Upper Right: ' + str(self.__UpperRight.getX()) + ' , ' + str(self.__UpperRight.getY()))
        print('Lower Right: ' + str(self.__LowerRight.getX()) + ' , ' + str(self.__LowerRight.getY()))
        print('Sector ' + self.__Name + ' has an area of ' + str(self.getSectorArea()) + ' sq kilometers')

    def getSectorArea(self):
        UX = self.__UpperRight.getX()
        LX = self.__UpperLeft.getX()
        Length = UX - LX
        UY = self.__UpperLeft.getY()
        LY = self.__LowerLeft.getY()
        Width = UY - LY
        return Length * Width
