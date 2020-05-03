import json
import os
from lib.utilities.GetSoftwareConfiguration import *

def GetCompleteTypeFilepath(typeId):
    swConfig = GetSoftwareConfiguration()
    
    compiledGeographyConfig = swConfig["CompiledGeography"]
    compiledGeographyPath = compiledGeographyConfig["path"]
    compiledGeographyMetadataFilename = compiledGeographyConfig["geographyMetadata"]

    completeMetadataFilename = os.path.join(compiledGeographyPath, compiledGeographyMetadataFilename)
    geographyMetadata = None
    with open(completeMetadataFilename) as f:
        geographyMetadata = json.load(f)
    
    typeFilename = geographyMetadata['Mapping'][typeId]
    completeTypeFilepath = os.path.join(compiledGeographyPath, typeFilename)

    return completeTypeFilepath




