

def IsPointOnLineSegment(line, point):
    x1, y1 = line[0]
    x2, y2 = line[1]
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    x, y = point

    if x >= minx and x <= maxx and y >= miny and y <= maxy:
        return True
    return False