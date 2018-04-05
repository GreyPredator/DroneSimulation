import math


class Location:

    def __init__(self, X, Y, Z):
        self.__X = X
        self.__Y = Y
        self.__Z = Z

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def setX(self, X):
        self.__X = X

    def setY(self, Y):
        self.__Y = Y

    def getZ(self):
        return self.__Z

    def setZ(self, Z):
        self.__Z = Z

    @staticmethod
    def euclideanDistance(L1, L2):
        X = (L1.getX() - L2.getX()) ** 2
        Y = (L1.getY() - L2.getY()) ** 2
        Z = (L1.getZ() - L2.getZ()) ** 2
        distance = math.sqrt(X + Y + Z)
        return distance

    @staticmethod
    def createLocation(L1, Xchange, Ychange, Zchange):
        L1.setX(L1.getX() + Xchange)
        L1.setY(L1.getY() + Ychange)
        L1.setY(L1.getZ() + Zchange)
        return L1
