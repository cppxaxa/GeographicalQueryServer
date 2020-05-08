

from lib.AddPlace import *
from lib.models.Place import *

def AddCurrentDestination(lockMap, UserToken, LatLon):
    AddPlace(lockMap, Place(UserToken, LatLon, "CurrentDestination", "CurrentDestination"))

