

import concurrent.futures as futures
import threading

# Reference for singleton: https://gist.github.com/tkhoa2711/7ce18809febbca4828db
class GlobalExecutorSingleton(object):
    __lock = threading.Lock()
    __instance = None

    def __init__(self):
        self.__executor = futures.ThreadPoolExecutor(max_workers=1)
    
    def setMaxWorkers(self, maxWorkers):
        self.__executor._max_workers = maxWorkers
        self.__executor._adjust_thread_count()

    @classmethod
    def instance(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()
        return cls.__instance

