import math


class Circle(object):
    # more info about property - http://pythonz.net/references/named/property/
    def __init__(self, r=1):
        self._r = r
        self.recalc_radius()

    def recalc_radius(self):
        self._d = 2 * self._r
        self._s = math.pi * self._r * self._r

    def recalc_diameter(self):
        self._r = 1. / 2 * self._d
        self._s = math.pi * self._r * self._r

    def __repr__(self):
        return "Circle({r})".format(r=self._r)

    def set_r(self, r):
        if r < 0:
            raise ValueError("Radius cannot be negative")
        self._r = r
        self.recalc_radius()

    def get_r(self):
        return self._r

    def set_d(self, d):
        if d < 0:
            raise ValueError("Diameter cannot be negative")
        self._d = d
        self.recalc_diameter()

    def get_d(self):
        return self._d

    def get_s(self):
        return self._s

    def set_s(self, s):
        raise AttributeError()

    radius = property(get_r, set_r, None, "This is r property")
    diameter = property(get_d, set_d, None, "This is d property")
    area = property(get_s, set_s, None, "This is area property")

