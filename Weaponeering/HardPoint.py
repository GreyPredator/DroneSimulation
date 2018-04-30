
class HardPoint:

    def __init__(self, Ordnance):
        self.__Ordnance = Ordnance
        self.__isLoaded = False

    def getOrdnance(self):
        return self.__Ordnance

    def setOrdnance(self, ord):
        self.__Ordnance = ord

    def getisLoaded(self):
        if self.__isLoaded == True:
            return self.__isLoaded
        else:
            return None

    def setisLoaded(self,b):
        self.__isLoaded = b