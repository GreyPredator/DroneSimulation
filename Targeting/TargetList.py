

class TargetList:

    def __init__(self, IDNumber, TimeDate, Targets):
        self.__IDNumber = IDNumber
        self.__TimeDate = TimeDate
        self.__Targets = Targets

    def getIDNumber(self):
        return self.__IDNumber

    def getTimeDate(self):
        return self.__TimeDate

    def getTargets(self):
        return self.__Targets

    def setIDNumber(self, v):
        self.__IDNumber = v

    def setTimeDate(self, v):
        self.__TimeDate = v

    def setTargets(self, v):
        self.__Targets = v

    def getTargetListValue(self):
        LV = 0
        for t in self.__Targets:
            LV += t.getValue()
        return LV

    def getTarget(self, ID):
        for t in self.__Targets:
            if t.IDNumber == ID:
                return t
            else:
                return None

    def addTarget(self, Tgt):
        self.__Targets.append(Tgt)

    def removeTarget(self, tgt):
        for t in self.__Targets:
            if t.IDNumber == tgt.IDNumber:
                t = None
            else:
                return None

    def displayTargets(self):
        for t in self.__Targets:
            print(t.IDNumber + " " + t.Type + " " + t.Location + " " + t.Priority + " " + t.Status)
