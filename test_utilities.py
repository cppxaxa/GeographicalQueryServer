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




# from lib.models.GeneralParameters import *
# from lib.DistanceToRoad import *

# p = [22.090570, 84.038002]
# param = GeneralParameters(LatLon=p)
# res = DistanceToRoad(param)

# print(res.distanceInKms)
# print(res.resultCoordinates)




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




# def hello(a):
#   print("Hello", a)

# from math import *
# import concurrent.futures as futures

# gE = futures.ThreadPoolExecutor(max_workers=1)

# workA = gE.submit(hello, 40)

#gE.shutdown()

#print(workA.result())


from lib.models.Place import *
from lib.AddPlace import *
import datetime
import time

from lib.DistanceToPlaceByPersonalParameters import *
from lib.models.PersonalParameters import *

lockMap = {}

AddPlace(lockMap, Place("cppxaxa", [1,2], "MyBase", "RelaxingPlace", True, False, "8:00", "20:00"))
AddPlace(lockMap, Place("cppxaxa", [5,9], "MyBase 2", "RelaxingPlace", True, False, "8:00", "20:00"))
AddPlace(lockMap, Place("cppxaxa", [10, 15], "MyBase 2", "RelaxingPlace", True, False, "8:00", "20:00"))

res = DistanceToPlaceByPersonalParameters("RelaxingPlace", PersonalParameters("cppxaxa", [6,8]))

print(res.queryCoordinates)
print(res.resultCoordinates)
