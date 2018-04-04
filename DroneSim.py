from GeoSpatial.Location import Location
from GeoSpatial.WayPoint import WayPoint


def main():
    L1 = Location(10, 10)
    print(L1.getX())
    print(L1.getY())
    L2 = Location(15, 15)
    print(L2.getX())
    print(L2.getY())
    L3 = Location(15, 15)
    print(L3.getX())
    print(L3.getY())
    D = Location.euclideanDistance(L1, L2)
    print(D)
    W1 = WayPoint(10, 20, 2000)
    print(W1.getAltitude())


if __name__ == '__main__':
    main()
