#!/usr/bin/python3
"""base class."""


class Base:
    """base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """new"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id - Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies of list of dictionaries.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves json to file.'''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_objs = [o.to_dictionary() for o in list_objs]

    @staticmethod
    def from_json_string(json_string):
        '''return deserialization a json dicts.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Loads from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''return list of classes from file and unjsonifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        try:
            with open(file, "r") as f:
                list_d = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_d]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        filename = cls.__name__ + ".csv"
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open(filename, 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        retr = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                retr.append(cls.create(**d))
        return retr

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for u in list_rectangles + list_squares:
            trt = turtle.Turtle()
            trt.color((randrange(255), randrange(255), randrange(255)))
            trt.pensize(1)
            trt.penup()
            trt.pendown()
            trt.setpos((u.x + trt.pos()[0], u.y - trt.pos()[1]))
            trt.pensize(10)
            trt.forward(u.width)
            trt.left(90)
            trt.forward(u.height)
            trt.left(90)
            trt.forward(u.width)
            trt.left(90)
            trt.forward(u.height)
            trt.left(90)
            trt.end_fill()

        time.sleep(5)
