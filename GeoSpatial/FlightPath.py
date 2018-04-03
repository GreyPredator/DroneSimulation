class FlightPath:

    def __init__(self,WayPointList):
        self.__WayPointList = WayPointList

    def getWayPointList(self):
        return self.__WayPointList

    def setWaypointList(self,v):
        self.__WayPointList = v

    def getWayPointList(self, index):
        return self.__WayPointList[index]

    def AddWayPoint(self, index, wp):
        self.__WayPointList[index] = wp

    def RemoveWaypoint(self, index, wp):
        self.__WayPointList[index] = None
