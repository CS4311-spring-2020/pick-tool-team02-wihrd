

class EventConfiguration:
    __instance = None
    def __init__(self, startDate, endDate, rootDirectory, eventName, eventDescription):
        super().__init__()
        self.__startDate = startDate
        self.__endDate = endDate
        self.__rootDirecotry = rootDirectory
        self.__eventName = eventName
        self.__eventDescription = eventDescription
        __instance = self

    def instance(self):
        if(self == None):
            return None
        else:
            return self.__instance
        
    
    
        