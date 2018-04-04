from GeoSpatial.Location import Location


class WayPoint(Location):

    def __init__(self,X, Y, Altitude):
        super().__init__(X,Y)
        self.__Altitude = Altitude

    def getAltitude(self):
        return self.__Altitude

    def setAltitude(self,v):
        self.__Altitude = v