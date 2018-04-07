from Weaponeering import Munition


class GBU44(Munition):

    def __init__(self):
        super().__init__('MBDA', 15000, 42, 36, 5.5, 2.3, "HEAT", 'Free Fall', 10, 'Free Fall', 'GPS-Laser Homing')