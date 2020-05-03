# import json
# from lib.utilities.CoordinateToNearestCoordinateInGeoFile import *

# geographyFilename = 'CompiledGeography\\AllCoast.json'
# res = CoordinateToNearestCoordinateInGeoFile([12.969754, 80.249700], geographyFilename)
# print(res.distanceInKms)
# print(res.queryCoordinates)
# print(res.resultCoordinates)



# # GeoJSON format
# geojsonTemplate = 
'''
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [{}, {}], [{}, {}]
        ]
      }
    }
'''
# #print(geojsonTemplate.format(py, px, targety, targetx))






# import os
# import json
# from lib.Compiler import *

    
# c = PlaceToFileMappingCompiler("ABC.json")
# c.compile("abc", "CompiledGeography", False)





# from lib.models.GeneralParameters import *
# from lib.DistanceToSeabeach import *

# p = [12.968538, 80.245090]
# param = GeneralParameters(LatLon=p)
# res = DistanceToSeabeach(param)

# print(res.distanceInKms)
# print(res.resultCoordinates)




from lib.models.GeneralParameters import *
from lib.DistanceToRoad import *

p = [22.090570, 84.038002]
param = GeneralParameters(LatLon=p)
res = DistanceToRoad(param)

print(res.distanceInKms)
print(res.resultCoordinates)




# from lib.models.GeneralParameters import *
# from lib.DistanceToHighway import *

# p = [22.090570, 84.038002]
# param = GeneralParameters(LatLon=p)
# res = DistanceToHighway(param)

# print(res.distanceInKms)
# print(res.resultCoordinates)


# from lib.models.GeneralParameters import *
# from lib.DistanceToRiver import *

# p = [22.090570, 84.038002]
# param = GeneralParameters(LatLon=p)
# res = DistanceToRiver(param)

# print(res.distanceInKms)
# print(res.resultCoordinates)


