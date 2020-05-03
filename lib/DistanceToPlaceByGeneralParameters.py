import json
import os

from lib.utilities.CoordinateToNearestCoordinateInGeoFile import *
from lib.utilities.GetCompleteTypeFilepath import *


def DistanceToPlaceByGeneralParameters(typeId, generalParam):
    completeTypeFilepath = GetCompleteTypeFilepath(typeId)

    startPoint = generalParam.LatLon
    result = CoordinateToNearestCoordinateInGeoFile(startPoint, completeTypeFilepath)

    return result

