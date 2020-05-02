import json
from lib.utilities.CoordinateToNearestCoordinateInGeoFile import *

geographyFilename = 'CompiledGeography\\AllCoast.json'
res = CoordinateToNearestCoordinateInGeoFile([12.969754, 80.249700], geographyFilename)
print(res.distanceInKms)
print(res.queryCoordinates)
print(res.resultCoordinates)



# GeoJSON format
geojsonTemplate = '''
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
#print(geojsonTemplate.format(py, px, targety, targetx))

