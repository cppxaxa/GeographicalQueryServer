
import os
from lib.utilities.GetCompleteUserPointTypeFilepath import *
from lib.utilities.UpdateLockMap import *

def AddPlace(lockMap, place):
    swConfig = GetSoftwareConfiguration()
    userStore = swConfig["UserPointStore"]["path"]

    userId = place.UserToken
    userDir = os.path.join(userStore, userId)

    if not os.path.exists(userDir):
        os.mkdir(userDir)

    type = place.Type
    completeFileStorePath = GetCompleteUserPointTypeFilepath(userId, type)

    lockMap = UpdateLockMap(lockMap, userId, type)
    with lockMap[userId][type]:
        with open(completeFileStorePath, 'a') as f:
            f.write(json.dumps(place.__dict__) + "\n")



