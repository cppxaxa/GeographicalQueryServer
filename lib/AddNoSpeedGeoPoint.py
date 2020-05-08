

from lib.AddPlace import *
from lib.models.Place import *

def AddNoSpeedGeoPoint(lockMap, UserToken, LatLon):
    AddPlace(lockMap, Place(UserToken, LatLon, "NoSpeedGeoPoint", "NoSpeedGeoPoint"))

