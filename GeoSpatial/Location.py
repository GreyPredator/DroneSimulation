import math


class Location:

    def __init__(self, X, Y):
        self.__X = X
        self.__Y = Y

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def setX(self, X):
        self.__X = X

    def setY(self, Y):
        self.__Y = Y

    @staticmethod
    def euclideanDistance(L1, L2):
        X = (L1.getX() - L2.getX()) ** 2
        Y = (L1.getY() - L2.getY()) ** 2
        distance = math.sqrt(X + Y)
        return distance

    @staticmethod
    def createLocation(L1, Xchange, Ychange):
        L1.setX(L1.getX() + Xchange)
        L1.setY(L1.getY() + Ychange)
        return L1
