import math

class Point2D:
    def __init__(self, x=None, y=None, r=None, a=None):
        self._x = 0.0
        self._y = 0.0
        self._r = 0.0
        self._a = 0.0

        if type(x) == Point2D:
            # copying another point
            self._x = x.x
            self._y = x.y
            self._r = x.r
            self._a = x.a
        elif not x == None and not y == None:
            # creating from x and y
            self._x = x
            self._y = y
            self._r = math.sqrt(x**2 + y**2)
            self._a = math.atan2(y, x)
        elif type(x) == tuple:
            # creating from x and y as tuple
            self._x = x[0]
            self._y = x[1]
            self._r = math.sqrt(x[0]**2 + x[1]**2)
            self._a = math.atan2(x[1], x[0])
        elif not r == None and not a == None:
            # creating from r and a
            self._r = r
            self._a = a
            self._x = r * math.cos(a)
            self._y = r * math.sin(a)




    def __repr__(self):
        return "Point2D({}, {})({}, {})".format(self._x,self._y,self._r,self._a)

if __name__ == '__main__':
    p  = Point2D((1,0))
    p2 = Point2D(p)
    print(p)
