"""This module contains only one class: Point2D"""
import math

class Point2D:
    """Describes cartesian and polar coordinates for 2D points.

    Point2D is a class used to simutaneously describe the behaviour of points 
    (vectors) in a 2D space with cartesian and polar coordinates. Changing one
    coordinate will change the value of the others, i.e., when changing a
    cartesian coordinate, the polar coordinates will be recalculated, and
    vice-versa.
    No methods need to be called to recalculate any of the coordinates, this is
    done automatically, e.g., if you set a new `x`, `r` and `a` will be
    updated.
    """
    def __init__(self, x=None, y=None, r=None, a=None):
        """Create Point2D from cartesian or polar (cartesian is default).

        All arguments are optional keyword arguments, but there are some rules.
        There are five ways to create a Point2D:
        1. Don't provide any args: will create the point (0, 0)
        2. Provide x and y: will create the cartesian point (x, y). If x is a
        number, y must be provided.
        3. Provide a tuple containing x and y: will create the cartesian point
        (x, y).
        4. Provide r and a: will create the polar point (r, a). If r is
        provided, a must be too.
        5. Provide another Point2D: Creates a copy of the point provided.

        Args:
            x (float or tuple or Point2D, optional): When `x` is a float,
                cartesian behavior is assumed and `y` should be supplied. If
                `x` is a tuple, the tuple must contain x and y. If `x` is a
                Point2D, a copy of that Point2D will be created.
            y (float, optional): y coordinate of cartesian pair.
            r (float, optional): radius of polar coordinates.
            a (float, optional): angle of polar coordinates (in radians).

        Examples:
            >>> Point2D()
            Point2D(0.0, 0.0)(0.0, 0.0)

            >>> Point2D(-1, 0)
            Point2D(-1, 0)(1.0, 3.141592653589793)

            >>> Point2D((-1.0, 0.0))
            Point2D(-1.0, 0.0)(1.0, 3.141592653589793)

            >>> Point2D(r=1.0, a=math.pi)
            Point2D(-1.0, 1.2246467991473532e-16)(1.0, 3.141592653589793)

            >>> Point2D(Point2D(10,10))
            Point2D(10, 10)(14.142135623730951, 0.7853981633974483)
        """
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
        elif type(x) == tuple:
            # creating from x and y as tuple
            self._x = x[0]
            self._y = x[1]
            self._r = math.sqrt(x[0]**2 + x[1]**2)
            self._a = math.atan2(x[1], x[0])
        elif not x == None and not y == None:
            # creating from x and y
            self._x = x
            self._y = y
            self._r = math.sqrt(x**2 + y**2)
            self._a = math.atan2(y, x)
        elif not r == None and not a == None:
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
        """Return or set cartesian coordinates.

        If no argument is provided, this method will return a tuple with
        (x, y).
        If `x` is a number, `y` must be provided. The cartesian coordinates
        will be set to `x` and `y` and the polar coordinates recalculated 
        accordingly.
        If `x` is a tuple it must contain the new values of x and y.
        """
        if not x:
            # act as getter
            return (self._x, self._y)
        elif type(x) == tuple:
            self._x = float(x[0])
            self._y = float(x[1])
            self._calc_polar()
        elif not x == None and not y == None:
            self._x = float(x)
            self._y = float(y)
            self._calc_polar()

    def polar(self, r=None, a=None):
        """Return or set polar coordinates.

        If no argument is provided, this method will return a tuple with
        (r, a).
        If `r` is a number, `a` must be provided. The polar coordinates will be
        set to `r` and `a` and the cartesian coordinates recalculated
        accordingly.
        If `r` is a tuple it must contain the new values of r and a.
        """
        if not r:
            # act as getter
            return (self._r, self._a)
        elif type(r) == tuple:
            self._r = float(r[0])
            self._a = float(r[1])
            self._calc_cartesian()
        elif not r == None and not a == None:
            self._r = float(r)
            self._a = float(a)
            self._calc_cartesian()

    def ints(self):
        """Return the cartesian coordinates as a tuple of ints."""
        return (int(self._x), int(self._y))

    @property
    def x(self):
        """x coordinate of cartesian pair."""
        return self._x

    @x.setter
    def x(self, val):
        self._x = float(val)
        self._calc_polar()
    
    @property
    def y(self):
        """y coordinate of cartesian pair."""
        return self._y

    @y.setter
    def y(self, val):
        self._y = float(val)
        self._calc_polar()
    
    @property
    def r(self):
        """Radius value of polar coordinates."""
        return self._r

    @r.setter
    def r(self, val):
        self._r = float(val)
        self._calc_cartesian()
    
    @property
    def a(self):
        """Angle value of polar coordinates."""
        return self._a

    @a.setter
    def a(self, val):
        self._a = float(val)
        self._calc_cartesian()

    def __repr__(self):
        """Return a string with the format 'Point2D(x, y)(r, a)'"""
        return "Point2D({}, {})({}, {})".format(self._x,self._y,self._r,self._a)

    def __add__(self, other):
        """Vector addition."""
        return Point2D(self._x + other.x, self._y + other.y)

    def __iadd__(self, other):
        """Vector addition."""
        self._x += other.x
        self._y += other.y
        self._calc_polar()
        return self

    def __sub__(self, other):
        """Vector subtraction."""
        return Point2D(self._x - other.x, self._y - other.y)

    def __isub__(self, other):
        """Vector subtraction."""
        self._x -= other.x
        self._y -= other.y
        self._calc_polar()
        return self

    def __mul__(self, val):
        """Scalar multiplication."""
        return Point2D(r=self.r*val, a=self.a)

    def __rmul__(self, val):
        """Scalar multiplication."""
        return Point2D(r=self.r*val, a=self.a)

    def __imul__(self, val):
        """Scalar multiplication."""
        self.r *= val
        return self


