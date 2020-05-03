
import threading

globalUpdateLockMapLock = threading.Lock()

def UpdateLockMap(lockMap, userId, type):
    with globalUpdateLockMapLock:
        if userId not in lockMap:
            lockMap[userId] = { type: threading.Lock() }
        elif type not in lockMap[userId]:
            lockMap[userId][type] = threading.Lock()
    return lockMap
