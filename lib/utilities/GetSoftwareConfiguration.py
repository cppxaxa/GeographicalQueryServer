
import json

def GetSoftwareConfiguration():
    swConfig = None
    with open("Configuration.json") as f:
        swConfig = json.load(f)
    return swConfig

