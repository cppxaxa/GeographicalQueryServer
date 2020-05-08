


import os
from lib.utilities.GetCompleteUserPointTypeFilepath import *
from lib.utilities.UpdateLockMap import *

def DeleteAllCurrentDestination(UserToken):
    swConfig = GetSoftwareConfiguration()
    userStore = swConfig["UserPointStore"]["path"]

    userId = UserToken
    userDir = os.path.join(userStore, userId)

    if not os.path.exists(userDir):
        os.mkdir(userDir)

    type = "CurrentDestination"
    completeFileStorePath = GetCompleteUserPointTypeFilepath(userId, type)

    os.remove(completeFileStorePath)

    