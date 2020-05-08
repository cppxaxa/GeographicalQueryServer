

from lib.DistanceToPlaceByPersonalParameters import *
from lib.DistanceToPlaceByGeneralParameters import *
from lib.models.GeneralParameters import *

def DistanceToNearbyWaterbody(personalParams):
    res = DistanceToPlaceByPersonalParameters("Waterbody", personalParams)

    if res is not None: return res

    res = DistanceToPlaceByGeneralParameters("Waterbody", \
        GeneralParameters(personalParams.UserToken, \
            personalParams.LatLon))

    if res is not None: return res
    
    res = DistanceToPlaceByGeneralParameters("River", \
        GeneralParameters(personalParams.UserToken, \
            personalParams.LatLon))

    if res is not None: return res
    
    res = DistanceToPlaceByGeneralParameters("Coast", \
        GeneralParameters(personalParams.UserToken, \
            personalParams.LatLon))

    if res is not None: return res

    return None
    

