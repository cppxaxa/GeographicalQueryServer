import math

def PointToLineCoordinates(line, point):
    x1, y1 = line[0]
    x2, y2 = line[1]
    px, py = point

    x = 0
    y = 0

    if x2 != x1 and y2 != y1:
        m1 = (y2 - y1)/(x2 - x1)
        m2 = -1/m1

        c1 = y1 - m1 * x1
        c2 = py - m2 * px

        x = (c1 - c2)/(m2 - m1)
        y = m1 * x + c1

    elif x2 == x1:
        x = x1
        y = py

    elif y2 == y1:
        y = y1
        x = px

    return [x, y]
