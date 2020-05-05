import json
import os
from lib.utilities.GetSoftwareConfiguration import *

def GetCompleteUserPointTypeFilepath(userId, typeId):
    swConfig = GetSoftwareConfiguration()
    userStore = swConfig["UserPointStore"]["path"]

    userDir = os.path.join(userStore, userId)

    if not os.path.exists(userDir):
        os.mkdir(userDir)

    completeFileStorePath = os.path.join(userDir, typeId + ".txt")

    return completeFileStorePath




