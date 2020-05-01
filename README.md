[WIP]

# Geographical Query Server

The server requirements are as follows:
1. Pure python code or cross-platform binaries
2. Entertain certain queries - possibly stateless
3. Simple to setup - or has a very easy setup
4. Honors confiugration to support lower-end servers
5. May have a report/ log to represent current state/ health and debug

# Queries to support (REST)

1. Trigger restart server/ invalidate cache
2. AddPoints (UserToken, LatLon, Name, Type)
3. DeletePoints
    i. (UserToken, LatLon)
    ii. (UserToken, nearbyLatLon)
    iii. (UserToken, namePattern)
4. DistanceToPlace (UserToken, LatLon, Type[], isPreferredPlace, isFavourite) <- Should return LatLon also
    i. 
    ii. DistanceToNearbyWaterbody <PersonalParameters>
    iii. DistanceToHighway <GeneralParameters>
    iv. DistanceToRelaxingPlace <PersonalParameters>
    v. DistanceToAtm <PersonalParameters>
    vi. DistanceToRestaurant <PersonalParameters>
    vii. DistanceToAtm <PersonalParameters>
    viii. DistanceToBank <PersonalParameters>
    ix. DistanceToWork <PersonalParameters>
    x. DistanceToBusStop <PersonalParameters>
    xi. DistanceToSocialPlace <PersonalParameters>
    xii. DistanceToHospital <PersonalParameters>
    xiii. DistanceToMedicalCounter <PersonalParameters>
5. ListNearbyPlaces (UserToken, LatLon, Type[], Radius, Limit=10)
6. SearchPlaceByName (UserToken, namePattern)

# Abbreviation

Type = SeaBeach, Waterbody, Highway, Restaurant, RelaxingPlace, Atm, Bank, Work, BusStop, SocialPlace, Hospital, MedicalStore

Attributes of a place = UserToken, LatLon, Name, Type, isPreferredPlace, isFavourite, PreferredTimeStart, PreferredTimeEnd

<GeneralParameters> = (UserToken, LatLon)
<PersonalParameters> = (UserToken, LatLon, isPreferred, isFavourite, CurrentTime)
