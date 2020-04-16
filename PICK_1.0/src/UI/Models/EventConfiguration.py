import sys

class EventConfiguration:
                
    instance = None
    __startDate = ""
    __endDate = ""
    __rootDirectory = ""
    __eventName = ""
    __eventDescription = ""

    def __init__(self):
        if(EventConfiguration.instance == None):
            EventConfiguration.instance = self
        else:
            raise Exception("Attempted to create a second Instance for singleton class, please use getInstance() instead")
    
    def getinstance():
        if not EventConfiguration.instance:
            EventConfiguration()
            return EventConfiguration.createConfig("","","","","")
        else:
            return EventConfiguration.instance
    
    def createConfig(startDate, endDate, rootDirectory, eventName, eventDescription):
        EventConfiguration.instance.__startDate = startDate
        EventConfiguration.instance.__endDate = endDate
        EventConfiguration.instance.__rootDirecotry = rootDirectory
        EventConfiguration.instance.__eventName = eventName
        EventConfiguration.instance.__eventDescription = eventDescription
        return EventConfiguration.instance

    def getName(self):
        return EventConfiguration.instance.__eventName

    def setName(self, eventName):
        EventConfiguration.instance.__eventName = eventName
    
    def getDescription(self):
        return EventConfiguration.instance.__eventDescription

    def setDescription(self, eventDescription):
        EventConfiguration.instance.__eventDescription = eventDescription

    def getStartDate(self):
        return EventConfiguration.instance.__startDate

    def setStartDate(self, startDate):
        EventConfiguration.instance.__startDate = startDate

    def getEndDate(self):
        return EventConfiguration.instance.__endDate

    def setEndDate(self, endDate):
        EventConfiguration.instance.__endDate = endDate

    def getRootDirectory(self):
        return EventConfiguration.instance.__rootDirecotry

    def setRootDirectory(self, rootDirectory):
        EventConfiguration.instance.__rootDirecotry = rootDirectory

    
    
        