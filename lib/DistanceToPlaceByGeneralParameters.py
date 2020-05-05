import json
import os

from lib.utilities.CoordinateToNearestCoordinateInGeoFile import *
from lib.utilities.GetCompleteGeoTypeFilepath import *


def DistanceToPlaceByGeneralParameters(typeId, generalParam):
    completeTypeFilepath = GetCompleteGeoTypeFilepath(typeId)

    startPoint = generalParam.LatLon
    result = CoordinateToNearestCoordinateInGeoFile(startPoint, completeTypeFilepath)

    return result

