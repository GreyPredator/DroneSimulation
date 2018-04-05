from Targeting import Target
import random


def targetFactory(count, designator, dominantType, sector):
    i = 0
    while(i < count):
        # IDNumber, Type, Location, Priority, isMobile, Size, Status, Value, Age, Description
        # Target Types:
            # Troop Concentration, Armored Vehicle, Unarmored Vehicle, Weapon Emplacement, Bunker, or Structure
        # Target Location
            # Targets are randomly  located in a sector defined by boundaries
        # Target Priorities:
            # Flash Urgent Immediate Routine
        # Target Size:
            # Small Large
        # Target Age:
            # New Recent Old
        ID = random.randint(1, 1001)
        TT = random.randint(1, 101)
        PR = random.randint(1, 5)
        SZ = random.randint(1, 3)
        A = random.randint(1, 4)

        X = sector.getUpperLeft().getX()
        Y = sector.getUpperRight()

        IDN = designator + "-" + str(ID)
        STAT = 'Active'

        if SZ == 2:
            TS = 'Large'
        else:
            TS = 'Small'

        if A == 3:
            TGTA = 'New'
        elif A == 2:
            TGTA =  'Recent'
        else:
            TGTA = 'Old'


        if dominantType != None:
            if TT > 25 < 95:
                TYP = dominantType
            elif TT < 26 and TT > 20:
                TYP = 'Troop Concentration'
                MBL = True
                TGTVAL = 2
            elif TT < 20 and TT > 15:
                TYP = 'Armored Vehicle'
                MBL = True
                TGTVAL = 5
            elif TT < 15 and TT > 10:
                TYP = 'Unarmored Vehicle'
                MBL = True
                TGTVAL = 3
            elif TT < 10 and TT > 5:
                TYP = 'Weapon Emplacement'
                TGTVAL = 1
            elif TT < 5 and TT > 1:
                TYP = 'Bunker'
                TGTVAL = 3.2
            else:
                TYP = 'Structure'
                TGTVAL = 3.5

        if dominantType == None:
            if TT >= 1 and TT < 25:
                TYP = 'Structure'
                TGTVAL = 3.5
            elif TT >= 25 and TT < 35:
                TYP = 'Armored Vehicle'
                MBL = True
                TGTVAL = 5
            elif TT >= 35 and TT < 45:
                TYP = 'Unarmored Vehicle'
                MBL = True
                TGTVAL = 3
            elif TT >= 45 and TT < 55:
                TYP = 'Weapon Emplacement'
                TGTVAL = 1
            elif TT >= 55 and TT < 65:
                TYP = 'Bunker'
                TGTVAL = 3.2
            else:
                TYP = 'Troop Concentration'
                MBL = True
                TGTVAL = 2

        if PR == 1:
            PRTY = 'Flash'
            TGTVAL = TGTVAL * 4 * SZ * A
        if PR == 2:
            PRTY = 'Urgent'
            TGTVAL = TGTVAL * 3 * SZ * A
        if PR == 3:
            PRTY = 'Immediate'
            TGTVAL = TGTVAL * 2 * SZ * A
        if PR == 4:
            PRTY = 'Routine'
            TGTVAL = TGTVAL * 1 * SZ * A

        TGTDESC = str(STAT, M, TS, TYP)
        t1 = Target(IDN, TYP, PRTY, MBL, TS, STAT, TGTA,


