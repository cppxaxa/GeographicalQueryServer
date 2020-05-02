import json
from lib.utilities.IsPointLieOnLineSegment import *
from lib.utilities.PointToLineCoordinates import *
from lib.utilities.PointToPointDistance import *
from lib.utilities.DistanceInMetersBetweenGeographicCoordinates import *

class CoordinateToNearestCoordinateInGeoFileResult:
    def __init__(self):
        self.distanceInKms = 0
        self.queryCoordinates = None
        self.resultCoordinates = None

# Sample point 12.969754, 80.249700 and file AllCoast.json
def CoordinateToNearestCoordinateInGeoFile(point, geographyFilename):
    points = None
    with open(geographyFilename) as f:
        points = json.load(f)

    INVALID_MAX = 999999999

    px, py = point
    minDistance = INVALID_MAX
    targetx, targety = 0, 0

    for unit in points:
        lat1, lon1 = unit["la"], unit["lo"]

        dist = PointToPointDistance([px, py], [lat1, lon1])
        if dist < minDistance:
            minDistance = dist
            targetx, targety = lat1, lon1

        edges = unit["e"]
        for p in edges:
            index = p["i"]
            lat2, lon2 = points[index]["la"], points[index]["lo"]

            dist = PointToPointDistance([px, py], [lat2, lon2])
            if dist < minDistance:
                minDistance = dist
                targetx, targety = lat2, lon2
            
            shadowx, shadowy = PointToLineCoordinates([[lat1, lon1], [lat2, lon2]], [px, py])

            if IsPointOnLineSegment([[lat1, lon1], [lat2, lon2]], [shadowx, shadowy]):
                dist = PointToPointDistance([px, py], [shadowx, shadowy])
                if dist < minDistance:
                    minDistance = dist
                    targetx, targety = shadowx, shadowy

    if minDistance == INVALID_MAX:
        return None

    result = CoordinateToNearestCoordinateInGeoFileResult()
    result.distanceInKms = DistanceInMetersBetweenGeographicCoordinates([px, py], [targetx, targety]) / 1000
    result.resultCoordinates = [targetx, targety]
    result.queryCoordinates = [px, py]

    return result
    