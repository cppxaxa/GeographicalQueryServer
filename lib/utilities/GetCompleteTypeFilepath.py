import json
import os

def GetCompleteTypeFilepath(typeId):
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

    return completeTypeFilepath