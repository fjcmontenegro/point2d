# point2d

The `point2d` module contains only on class: `Point2D`.

This class describes Cartesian and polar coordinates for 2D points. It simultaneously represents the behavior of points (vectors) in a 2D space with Cartesian and polar coordinates, so that those can be used interchangeably. Changing one coordinate will change the value of the other, i.e., when changing a Cartesian coordinate, the polar coordinates will be recalculated, and vice-versa.

No methods need to be called to recalculate any of the coordinates, this is done automatically, e.g., if you set a new `x`, `r` and `a` will be updated.

## Instalation

From this folder run `python setup.py install`.

## Usage

You can `import point2d` and use the class via `point2d.Point2D` or `from point2d import Point2D` and use `Point2D` directly from your code.

### Attributes

The `Point2D` class has Cartesian coordinates represented by `x` and `y`, and polar coordinates (radius and angle) represented by (`r` and `a`). If you change the value of `x` or `y`, `r` and `a` will be updated automatically, and vice-versa.

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

The method `cartesian` can set Cartesian coordinates or return them. You can set them with `x` and `y` as separate arguments, with a tuple containing `x`and `y`, or use this method to get a tuple containing `x` and `y`.
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

#### Polar Coordinates

The method `polar` does the same thing for polar coordinates. You can set them with `r` and `a` as separate arguments, with a tuple containing `r`and `a`, or use this method to get a tuple containing `r` and `a`.
```python
>>> p = Point2D()
>>> p.polar(1.0, 0.0)
>>> p
Point2D(0.0, 0.0)(0.0, 0.0)
>>> p.polar((-1.0, 0.0))
>>> p
Point2D(-1.0, 0.0)(1.0, 3.141592653589793)
>>> p.polar()
(-1.0, 0.0)
```




URL: https://github.com/SplinterDev/point2d/

Created By: Fabrício J.C. Montenegro (2018)