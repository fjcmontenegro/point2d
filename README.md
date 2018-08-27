# point2d

The `point2d` module contains only on class: `Point2D`.

This class describes Cartesian and polar coordinates for 2D points. It simultaneously represents the behavior of points (vectors) in a 2D space with Cartesian and polar coordinates, so that those can be used interchangeably. Changing one coordinate will change the value of the other, i.e., when changing a Cartesian coordinate, the polar coordinates will be recalculated, and vice-versa.

No methods need to be called to recalculate any of the coordinates, this is done automatically, e.g., if you set a new `x`, `r` and `a` will be updated.

## Instalation

From this folder run `python setup.py install`.

## Usage

You can `import point2d` and use the class via `point2d.Point2D` or `from point2d import Point2D` and use `Point2D` directly from your code.

### Attributes

The `Point2D` class has Cartesian coordinates represented by `x` and `y`, and polar coordinates (radius and angle) represented by `r` and `a`. If you change the value of `x` or `y`, `r` and `a` will be updated automatically, and vice-versa.

### Creating a Point2D

There are five ways of creating a Point2D:

1. Without any arguments. This will initialize it as the point (0, 0).
```python
>>> Point2D()
Point2D(0.0, 0.0)(0.0, 0.0)
```
2. With `x` and `y` as separate arguments.
```python
>>> Point2D(-1.0, 0.0)
Point2D(-1.0, 0.0)(1.0, 3.141592653589793)
```
3. With `x` and `y` as a single tuple.
```python
>>> Point2D((-1.0, 0.0))
Point2D(-1.0, 0.0)(1.0, 3.141592653589793)
```
4. With `r` and `a` as separate arguments.
```python
>>> Point2D(r=1.0, a=math.pi)
Point2D(-1.0, 1.2246467991473532e-16)(1.0, 3.141592653589793)
```
5. Copying another Point2D:
```python
>>> Point2D(Point2D(-1.0, 0.0))
Point2D(-1.0, 0.0)(1.0, 3.141592653589793)
```

### Functionalities

As said earlier, the class automatically keeps track of cartesian and polar coordinates.

```python
>>> p = Point2D()
>>> print(p) 
Point2D(0.0, 0.0)(0.0, 0.0)
>>> p.x = -1.0
>>> print(p)
Point2D(-1.0, 0.0)(1.0, 3.141592653589793)
>>> p.r = 5.0
>>> print(p)
Point2D(-5.0, 6.123233995736766e-16)(5.0, 3.141592653589793)
```

The class also implements operation between points (they return a new Point2D).
```python
>>> p1 = Point2D(10.0, 0.0)
>>> p2 = Point2D(0.0, 10.0)
>>> p1 + p2
Point2D(10.0, 10.0)(14.142135623730951, 0.7853981633974483)
>>> p1 - p2
Point2D(10.0, -10.0)(14.142135623730951, -0.7853981633974483)
```
You can update a point through a sum or subtraction between points if you do it like this:
```python
>>> p1 += p2
>>> p1
Point2D(10.0, 10.0)(14.142135623730951, 0.7853981633974483)
>>> p1 -= p2
>>> p1
Point2D(10.0, 0.0)(10.0, 0.0)
```
The class also implements operation between points and scalars.
```python
>>> Point2D(1.0, 0.0) * 10
Point2D(10.0, 0.0)(10.0, 0.0)
```

### Getting and setting

You can get and set values to the coordinates directly through their names (`x`, `y`, `r`, `a`), but there are some useful methods to help you on the way.

#### Cartesian Coordinates

The `cartesian()` method can set Cartesian coordinates or return them. You can set them with `x` and `y` as separate arguments, with a tuple containing `x`and `y`, or use this method to get a tuple containing `x` and `y`.
```python
>>> p = Point2D()
>>> p.cartesian(1.0, 0.0)
>>> p
Point2D(0.0, 0.0)(0.0, 0.0)
>>> p.cartesian((-1.0, 0.0))
>>> p
Point2D(-1.0, 0.0)(1.0, 3.141592653589793)
>>> p.cartesian()
(-1.0, 0.0)
```
You can also use the method `ints()` to get a tuple of ints with the cartesian coordinates. This is especially useful if you're working with Pygame.

#### Polar Coordinates

The `polar()` method does the same thing for polar coordinates. You can set them with `r` and `a` as separate arguments, with a tuple containing `r`and `a`, or use this method to get a tuple containing `r` and `a`.
```python
>>> p = Point2D()
>>> p.polar(1.0, 0.0)
>>> p
Point2D(1.0, 0.0)(1.0, 0.0)
>>> p.polar((1.0, math.pi))
>>> p
Point2D(-1.0, 1.2246467991473532e-16)(1.0, 3.141592653589793)
>>> p.polar()
(1.0, 3.141592653589793)
```
### Useful Tricks

You can work solely with Cartesian coordinates with this class and it's still useful. Here are some nice "tricks".

#### Length of a vector

Remember that the radius of a point, in polar coordinates, is its distance to the origin, which is the same as the length of a vector located at the origin.

Use `mypoint.r` to find out its length.
```python
>>> p = Point2D(3, 4)
>>> p.r
5.0
```

#### Distance between points

Subtracting two points will give you a third point. The length of this third point is the distance between the two first points. Use its radius to get the length.
```python
>>> p1 = Point2D(10, 0)
>>> p2 = Point2D(10, 10)
>>> (p2 - p1).r
10.0
```

#### Angle between vectors

Again, subtracting two vectors will give you a third. The angle of this third vector is the angle between the two first vectors. Be careful, though, `p1 - p2` is not the same as `p2 - p1`. Although they will yield supplementary angles (their sum is 180°).
```python
>>> p1 = Point2D(10, 0)
>>> p2 = Point2D(10, 10)
>>> math.degrees((p2 - p1).a)
90.0
>>> math.degrees((p1 - p2).a)
-90.0
```

#### Scaling vectors

There are two ways to do this. One of them is to multiply the vector by the number that describes its scaling factor. The other way is multiplying its radius by the number.
```python
>>> p = Point2D(1,0)
>>> p *= 3
>>> p
Point2D(3.0, 0.0)(3.0, 0.0)
>>> p = Point2D(1,0)
>>> p.r *= 3
>>> p
Point2D(3.0, 0.0)(3.0, 0.0)
```

#### Unit vector

The unit vector is a vector of magnitude 1. To find the unit vector of a vector, you need to multiply the vector by its length, which can be kind of annoying. Well, it's easy now. Just set its radius to 1 and it's done. You're welcome.

```python
>>> p = Point2D(12.34, 56.78)
>>> p.r = 1
>>> p
Point2D(0.21237248410903914, 0.9771887883072318)(1.0, 1.3567941381565736)
```

## Links


Code: [https://github.com/SplinterDev/point2d/](https://github.com/SplinterDev/point2d/)

License: [GNU General Public License v3.0](https://github.com/SplinterDev/point2d/blob/master/LICENSE)

Created By: [Fabrício J.C. Montenegro](https://github.com/SplinterDev) (2018)