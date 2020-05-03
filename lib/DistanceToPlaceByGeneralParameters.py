import json
import os

from lib.utilities.CoordinateToNearestCoordinateInGeoFile import *

def DistanceToPlaceByGeneralParameters(typeId, generalParam):
    swConfig = None
    with open("Configuration.json") as f:
        swConfig = json.load(f)
    
    compiledGeographyConfig = swConfig["CompiledGeography"]
    compiledGeographyPath = compiledGeographyConfig["path"]
    compiledGeographyMetadataFilename = compiledGeographyConfig["geographyMetadata"]

    completeMetadataFilename = os.path.join(compiledGeographyPath, compiledGeographyMetadataFilename)
    geographyMetadata = None
    with open(completeMetadataFilename) as f:
        geographyMetadata = json.load(f)
    
    typeFilename = geographyMetadata['Mapping'][typeId]
    completeTypeFilepath = os.path.join(compiledGeographyPath, typeFilename)

    startPoint = generalParam.LatLon
    result = CoordinateToNearestCoordinateInGeoFile(startPoint, completeTypeFilepath)

    return result

