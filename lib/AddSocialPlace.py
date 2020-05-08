


from lib.AddPlace import *
from lib.models.Place import *

def AddCurrentDestination(lockMap, place):
    AddPlace(lockMap, Place(place.UserToken, place.LatLon, \
        place.Name, "SocialPlace", place.IsPreferredPlace, \
            place.IsFavourite, place.PreferredTimeStart, \
                place.PreferredTimeEnd))

