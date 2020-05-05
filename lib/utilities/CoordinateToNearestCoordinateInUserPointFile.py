import json
from lib.utilities.IsPointLieOnLineSegment import *
from lib.utilities.PointToLineCoordinates import *
from lib.utilities.PointToPointDistance import *
from lib.utilities.DistanceInMetersBetweenGeographicCoordinates import *
from lib.models.CoordinateToNearestCoordinateInGeoFileResult import *

# Sample point 12.969754, 80.249700 and file AllCoast.json
def CoordinateToNearestCoordinateInUserPointFile(point, userPointFilepath):
    INVALID_MAX = 999999999

    px, py = point
    minDistance = INVALID_MAX
    targetx, targety = 0, 0

    with open(userPointFilepath) as f:
        for line in f:
            unit = json.loads(line)

            lat1, lon1 = unit["LatLon"]

            dist = PointToPointDistance([px, py], [lat1, lon1])
            if dist < minDistance:
                minDistance = dist
                targetx, targety = lat1, lon1


    if minDistance == INVALID_MAX:
        return None

    result = CoordinateToNearestCoordinateInGeoFileResult()
    result.distanceInKms = DistanceInMetersBetweenGeographicCoordinates([px, py], [targetx, targety]) / 1000
    result.resultCoordinates = [targetx, targety]
    result.queryCoordinates = [px, py]

    return result
    