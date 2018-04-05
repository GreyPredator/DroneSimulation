from GeoSpatial.Location import Location
from GeoSpatial.Sector import Sector


def main():
    UL = Location(0, 100, 30)
    LL = Location(0, 0, 30)
    UR = Location(100, 100, 30)
    LR = Location(100, 0, 30)
    s = Sector('Primary', UL, LL, UR, LR)
    print(s.displaySector())


if __name__ == '__main__':
    main()
