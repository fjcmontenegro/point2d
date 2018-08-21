import math

class Point2D:
    def __init__(self, x=None, y=None, r=None, a=None):
        if not x and not r:
            self._x = 0.0
            self._y = 0.0
            self._r = 0.0
            self._a = 0.0
        elif type(x) == Point2D:
            # copying another point
            self._x = x.x
            self._y = x.y
            self._r = x.r
            self._a = x.a
        elif type(x) == tuple:
            # creating from x and y as tuple
            self._x = x[0]
            self._y = x[1]
            self._r = math.sqrt(x[0]**2 + x[1]**2)
            self._a = math.atan2(x[1], x[0])
        elif x and y:
            # creating from x and y
            self._x = x
            self._y = y
            self._r = math.sqrt(x**2 + y**2)
            self._a = math.atan2(y, x)
        elif r and a:
            # creating from r and a
            self._r = r
            self._a = a
            self._x = r * math.cos(a)
            self._y = r * math.sin(a)

    def _calc_cartesian(self):
        self._x = self._r * math.cos(self._a)
        self._y = self._r * math.sin(self._a)

    def _calc_polar(self):
        self._r = math.sqrt(self._x**2 + self._y**2)
        self._a = math.atan2(self._y, self._x)

    def cartesian(self, x=None, y=None):
        if not x:
            # act as getter
            return (self._x, self._y)
        elif type(x) == tuple:
            self._x = float(x[0])
            self._y = float(x[1])
            self._calc_polar()
        elif x and y:
            self._x = float(x)
            self._y = float(y)
            self._calc_polar()


    def ints(self):
        return (int(self._x), int(self._y))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        print("Setting x as {}".format(val))
        self._x = float(val)
        self._calc_polar()
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        print("Setting y as {}".format(val))
        self._y = float(val)
        self._calc_polar()
    
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, val):
        print("Setting r as {}".format(val))
        self._r = float(val)
        self._calc_cartesian()
    
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, val):
        print("Setting a as {}".format(val))
        self._a = float(val)
        self._calc_cartesian()

    def __repr__(self):
        return "Point2D({}, {})({}, {})".format(self._x,self._y,self._r,self._a)

if __name__ == '__main__':
    p  = Point2D()
    print(p)
    p.x = 5
    print(p)
    p.y = 5
    print(p)
    p.r = 5
    print(p)
    p.a = math.pi
    print(p)
    p.x, p.y = 1.0, 0.0
    print(p.cartesian())
    print(p.ints())
    p.cartesian((2,2))
    print(p)
    p.cartesian(5,2)
    print(p)


