import unittest
from point2d import Point2D
import math

class TestPoint2D(unittest.TestCase):
    def setUp(self):
        self.p = Point2D()

    def test_construct_no_param(self):
        p = Point2D()
        self.assertEqual(p._x, 0.0)
        self.assertEqual(p._y, 0.0)
        self.assertEqual(p._r, 0.0)
        self.assertEqual(p._a, 0.0)

    def test_construct_x_and_y(self):
        p = Point2D(2, 0)
        self.assertEqual(p._x, 2.0)
        self.assertEqual(p._y, 0.0)
        self.assertEqual(p._r, 2.0)
        self.assertEqual(p._a, 0.0)

    def test_construct_x_and_y_tuple(self):
        p = Point2D((2, 0))
        self.assertEqual(p._x, 2.0)
        self.assertEqual(p._y, 0.0)
        self.assertEqual(p._r, 2.0)
        self.assertEqual(p._a, 0.0)

    def test_construct_r_and_a(self):
        p = Point2D(r=2, a=math.pi)
        self.assertEqual(p._x, -2.0)
        self.assertEqual(round(p._y, 5), 0.0)
        self.assertEqual(p._r, 2.0)
        self.assertEqual(p._a, math.pi)

    def test_copy_point(self):
        p1 = Point2D(2, 0)
        p2 = Point2D(p1)
        self.assertEqual(p2._x, 2.0)
        self.assertEqual(p2._y, 0.0)
        self.assertEqual(p2._r, 2.0)
        self.assertEqual(p2._a, 0.0)

    def test_get_x(self):
        self.assertEqual(self.p.x, 0.0)
    def test_get_y(self):
        self.assertEqual(self.p.y, 0.0)
    def test_get_r(self):
        self.assertEqual(self.p.r, 0.0)
    def test_get_a(self):
        self.assertEqual(self.p.a, 0.0)

    def test_get_cartesian(self):
        t = self.p.cartesian()
        self.assertEqual(t[0], self.p.x)
        self.assertEqual(t[1], self.p.y)

    def test_get_ints(self):
        t = self.p.ints()
        self.assertEqual(t[0], int(self.p.x))
        self.assertEqual(t[1], int(self.p.y))

    def test_get_polar(self):
        t = self.p.polar()
        self.assertEqual(t[0], self.p.r)
        self.assertEqual(t[1], self.p.a)

    def test_set_x(self):
        self.p.x = 1.2
        self.assertEqual(self.p.x, 1.2)
    def test_set_y(self):
        self.p.y = 1.2
        self.assertEqual(self.p.y, 1.2)
    def test_set_r(self):
        self.p.r = 1.2
        self.assertEqual(self.p.r, 1.2)
    def test_set_a(self):
        self.p.a = 1.2
        self.assertEqual(self.p.a, 1.2)

    def test_set_cartesian(self):
        self.p.cartesian(1.2, 3.4)
        self.assertEqual(self.p.x, 1.2)
        self.assertEqual(self.p.y, 3.4)

    def test_set_cartesian_tuple(self):
        self.p.cartesian((1.2, 3.4))
        self.assertEqual(self.p.x, 1.2)
        self.assertEqual(self.p.y, 3.4)

    def test_set_polar(self):
        self.p.polar(1.2, 3.4)
        self.assertEqual(self.p.r, 1.2)
        self.assertEqual(self.p.a, 3.4)

    def test_set_polar_tuple(self):
        self.p.polar((1.2, 3.4))
        self.assertEqual(self.p.r, 1.2)
        self.assertEqual(self.p.a, 3.4)

    def test_polar_from_cartesian(self):
        self.p.x = 1
        self.p.y = 0
        self.assertEqual(self.p.r, 1.0)
        self.assertEqual(self.p.a, 0.0)

    def test_cartesian_from_polar(self):
        self.p.r = 1
        self.p.a = 0
        self.assertEqual(self.p.x, 1.0)
        self.assertEqual(self.p.y, 0.0)

    def test_add(self):
        p1 = Point2D(1, 0)
        p2 = Point2D(0, 1)
        p = p1 + p2
        self.assertEqual(p.x, 1.0)
        self.assertEqual(p.y, 1.0)
        p = p2 + p1
        self.assertEqual(p.x, 1.0)
        self.assertEqual(p.y, 1.0)

    def test_iadd(self):
        p1 = Point2D(1, 0)
        p2 = Point2D(0, 1)
        p1 += p2
        self.assertEqual(p1.x, 1.0)
        self.assertEqual(p1.y, 1.0)
        p1 = Point2D(1, 0)
        p2 += p1
        self.assertEqual(p2.x, 1.0)
        self.assertEqual(p2.y, 1.0)

    def test_sub(self):
        p1 = Point2D(1, 0)
        p2 = Point2D(0, 1)
        p = p1 - p2
        self.assertEqual(p.x, 1.0)
        self.assertEqual(p.y, -1.0)
        p = p2 - p1
        self.assertEqual(p.x, -1.0)
        self.assertEqual(p.y, 1.0)

    def test_isub(self):
        p1 = Point2D(1, 0)
        p2 = Point2D(0, 1)
        p1 -= p2
        self.assertEqual(p1.x, 1.0)
        self.assertEqual(p1.y, -1.0)
        p1 = Point2D(1, 0)
        p2 -= p1
        self.assertEqual(p2.x, -1.0)
        self.assertEqual(p2.y, 1.0)

    def test_mul(self):
        self.p.x = 1
        self.assertEqual((self.p * 2).r, 2.0)
        self.assertEqual((self.p * 2).a, 0.0)

    def test_rmul(self):
        self.p.x = 1
        self.assertEqual((2 * self.p).r, 2.0)
        self.assertEqual((2 * self.p).a, 0.0)

    def test_imul(self):
        self.p.x = 1
        self.p  *= 2
        self.assertEqual(self.p.r, 2.0)
        self.assertEqual(self.p.a, 0.0)





if __name__ == '__main__':
    unittest.main()