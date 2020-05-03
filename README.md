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
	1. (UserToken, LatLon)
	2. (UserToken, nearbyLatLon)
	3. (UserToken, namePattern)
4. DistanceToPlace (UserToken, LatLon, Type[], isPreferredPlace, isFavourite) <- Should return LatLon also
	1. DistanceToSeabeach (GeneralParameters)
	2. DistanceToRiver (GeneralParameters)
	3. DistanceToNearbyWaterbody (PersonalParameters)
	4. DistanceToHighway (GeneralParameters)
	5. DistanceToRelaxingPlace (PersonalParameters)
	6. DistanceToAtm (PersonalParameters)
	7. DistanceToRestaurant (PersonalParameters)
	8. DistanceToBank (PersonalParameters)
	9. DistanceToWork (PersonalParameters)
	10. DistanceToBusStop (PersonalParameters)
	11. DistanceToSocialPlace (PersonalParameters)
	12. DistanceToHospital (PersonalParameters)
	13. DistanceToMedicalCounter (PersonalParameters)
5. ListNearbyPlaces (UserToken, LatLon, Type[], Radius, Limit=10)
6. SearchPlaceByName (UserToken, namePattern)

# Abbreviation

- Type = Coast, Waterbody, Highway, Restaurant, RelaxingPlace, Atm, Bank, Work, BusStop, SocialPlace, Hospital, MedicalStore
- Attributes of a place = UserToken, LatLon, Name, Type, isPreferredPlace, isFavourite, PreferredTimeStart, PreferredTimeEnd
- GeneralParameters = (UserToken, LatLon)
- PersonalParameters = (UserToken, LatLon, isPreferred, isFavourite, CurrentTime)
