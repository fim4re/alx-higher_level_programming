#!/usr/bin/python3
"""rectangle class."""
from models.base import Base


class Rectangle(Base):
    """a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """new Rectangle."""
        super().__init__(id)
        self.width = width
        self.x = x
        self.height = height
        self.y = y

    @property
    def width(self):
        """Set and get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set and get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set and get the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set and get the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the `#` character."""
        ds = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(ds, end='')

    def _update_(self, id=None, width=None, height=None, x=None, y=None):
        """fisrt update internal"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Return the dictionary of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the info of the Rectangle."""
        return "[{}] ({}) {}/{} - {}/{}"
    .format(type(self).__name__, self.id, self.x, self.y,
            self.width, self.height)
