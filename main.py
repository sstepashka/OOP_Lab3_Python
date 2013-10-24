#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Shape(x, y):

    def f(func_name, *args):
        if func_name == "getX":
            return x
        elif func_name == "setX":
            return Shape(args[0], y)
        elif func_name == "getY":
            return y
        elif func_name == "setY":
            return Shape(x, args[0])
        elif func_name == "move":
            return Shape(x + args[0], y + args[1])
        elif func_name == "print":
            print "Shape X = %i, Y = %i" % (x, y)
        else:
            return None

    return f

def Rectangle(x, y, w, h):
    parent = Shape(x, y)

    def f (func_name, *args):
        if func_name == "getW":
            return w
        elif func_name == "setW":
            return Rectangle(x, y, args[0], h)
        elif func_name == "getH":
            return h
        elif func_name == "setH":
            return Rectangle(x, y, w, args[0])
        elif func_name == "setX":
            return Rectangle(args[0], y, w, h)
        elif func_name == "setY":
            return Rectangle(x, args[0], w, h)
        elif func_name == "move":
            return Rectangle(x + args[0], y + args[1], w, h)
        elif func_name == "print":
            print "Rectangle X = %i, Y = %i, W = %i, H = %i;" % (x, y, w, h)
        else:
            return parent(func_name, *args)

    return f


def Box(x, y, s):
    parent = Rectangle(x, y, s, s)

    def f (func_name, *args):
        if func_name == "getS":
            return s
        elif func_name == "setS":
            return Box(x, y, args[0])
        elif func_name == "setH":
            return Box(x, y, args[0])
        elif func_name == "setW":
            return Box(x, y, args[0])
        elif func_name == "setX":
            return Box(args[0], y, s)
        elif func_name == "setY":
            return Box(x, args[0], s)
        elif func_name == "move":
            return Box(x + args[0], y + args[1], s)
        elif func_name == "print":
            print "Box X = %i, Y = %i, S = %i;" % (x, y, s)
        else:
            return parent(func_name, *args)

    return f;

def Cyrcle(x, y, r):
    parent = Shape(x, y)

    def f (func_name, *args):
        if func_name == "setR":
            return Cyrcle(x, y, args[0])
        elif func_name == "getR":
            return r
        elif func_name == "setX":
            return Cyrcle(args[0], y, r)
        elif func_name == "setY":
            return Cyrcle(x, args[0], r)
        elif func_name == "move":
            return Cyrcle(x + args[0], y + args[1], r)
        elif func_name == "print":
            print "Cyrcle X = %i, Y = %i, R = %i;" % (x, y, r)
        else:
            return parent(func_name, *args)

    return f


def Composite(x, y, shapes = []):
    parent = Shape(x, y)

    def f (func_name, *args):
        if func_name == "addShape":
            return Composite(x, y, shapes + [args[0]])
        elif func_name == "deleteShape":
            return Composite(x, y, filter(lambda x: x != args[0], shapes))
        elif func_name == "setX":
            return Composite(args[0], y, shapes)
        elif func_name == "setY":
            return Composite(x, args[0], shapes)
        elif func_name == "move":
            return Composite(x + args[0], y + args[1], map(lambda x: x("move", args[0], args[1]), shapes))
        elif func_name == "print":
            print "Begin Composite X = %i, Y = %i;" % (x, y)
            map(lambda x: x("print"), shapes)
            print "End Composite X = %i, Y = %i;" % (x, y)
        else:
            return parent(func_name, *args)

    return f


def main():

    rect = Rectangle(1, 2, 3, 5)
    rect2 = Rectangle(2, 3, 6, 1)
    box = Box(6, 3, 9)
    cyrcle = Cyrcle(3, 1, 5)
    cyrcle2 = Cyrcle(23, 2, 6)

    composite = Composite(3, 1, [box, cyrcle])

    composite2 = Composite(6, 9, [composite, rect2])
    composite2 = composite2("addShape", cyrcle2)

    print "Rect:"
    rect("print")
    print ""

    print "Box:"
    box("print")
    print ""

    print "Cyrcle:"
    cyrcle("print")
    print ""

    print "Composite:"
    composite("print")
    print ""

    print "Composite2:"
    composite2("print")
    print ""

    print "Composite2 move by (10, 10):"
    composite2 = composite2("move", 10, 10)
    composite2("print")
    print ""

    print "Composite2 move by (-10, -10):"
    composite2 = composite2("move", -10, -10)
    composite2("print")
    print ""

if __name__ == '__main__':
    main()
