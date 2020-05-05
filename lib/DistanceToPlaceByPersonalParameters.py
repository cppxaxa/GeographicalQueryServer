import json
import os

from lib.utilities.CoordinateToNearestCoordinateInUserPointFile import *
from lib.utilities.GetCompleteUserPointTypeFilepath import *


def DistanceToPlaceByPersonalParameters(typeId, personalParams):
    userId = personalParams.UserToken
    completeTypeFilepath = GetCompleteUserPointTypeFilepath(userId, typeId)

    startPoint = personalParams.LatLon
    result = CoordinateToNearestCoordinateInUserPointFile(startPoint, completeTypeFilepath)

    return result

