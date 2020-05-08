
import os
import json
import shutil
import random
from lib.utilities.GetCompleteUserPointTypeFilepath import *
from lib.utilities.UpdateLockMap import *
from lib.utilities.DistanceInMetersBetweenGeographicCoordinates import *

def DeleteNearbyPlaceByCoordinates(lockMap, UserToken, Type, nearbyLatLon, maxEntriesToDelete = 1):
    swConfig = GetSoftwareConfiguration()
    userStore = swConfig["UserPointStore"]["path"]

    userId = UserToken
    userDir = os.path.join(userStore, userId)

    if not os.path.exists(userDir):
        os.mkdir(userDir)

    type = Type
    completeFileStorePath = GetCompleteUserPointTypeFilepath(userId, type)

    # Find the entries to delete
    px, py = nearbyLatLon.LatLon
    toDeleteLineNumberList = []
    with open(completeFileStorePath) as f:
        lineNumber = 0
        for line in f:
            lineNumber += 1

            unit = json.loads(line)
            lat1, lon1 = unit["LatLon"]
            dist = DistanceInMetersBetweenGeographicCoordinates([px, py], [lat1, lon1])
            if dist <= nearbyLatLon.RadiusInMeters:
                toDeleteLineNumberList.append([dist, lineNumber])
    
    toDeleteLineNumberList = sorted(toDeleteLineNumberList)
    if len(toDeleteLineNumberList) > maxEntriesToDelete:
        toDeleteLineNumberList = toDeleteLineNumberList[:maxEntriesToDelete]
    
    # Make a set for faster query
    toDeleteLineNumberSet = [el[1] for el in toDeleteLineNumberList]
    toDeleteLineNumberSet = set(toDeleteLineNumberSet)

    # Now lock the file to delete
    lockMap = UpdateLockMap(lockMap, userId, type)
    with lockMap[userId][type]:
        # Make a copy of the original file to filter
        completeTempFilename = GetCompleteUserPointTypeFilepath(userId, \
            "temp_" + str(random.randint(100, 10000)) + "_" + type)
        shutil.copyfile(completeFileStorePath, completeTempFilename)

        with open(completeTempFilename) as origFileHandle:
            with open(completeFileStorePath, 'w') as f:
                lineNumber = 0
                for line in origFileHandle:
                    lineNumber += 1
                    if lineNumber not in toDeleteLineNumberSet \
                        and line.strip() != "":
                        f.write(line.strip() + "\n")
        
        os.remove(completeTempFilename)

