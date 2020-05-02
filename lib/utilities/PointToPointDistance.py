import math

# A = [x1, y1], B = [x2, y2]
def PointToPointDistance(A, B):
    return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
