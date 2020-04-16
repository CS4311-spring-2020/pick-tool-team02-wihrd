

class LogFile():

    def __init__(self, filename, timestamp, path, team):
        super().__init__()
        self.__name = filename
        self.__timestamp = timestamp
        self.__path = path
        self.__team = team
        self.__progress = "procesing"
        self.__status = "imported"

    
    def getfilename(self):
        return self.__name
    
    def setfilename(self, filename):
        self.__name = filename

    def getTimeStamp(self):
        return self.__timestamp

    def setTimeStamp(self, timestamp):
        self.__timestamp = timestamp

    def getPath(self):
        return self.__path

    def setPath(self, path):
        self.__path = path

    def getTeam(self):
        return self.__team

    def setTeam(self, team):
        self.__team = team

    def getProgress(self):
        return self.__progress

    def setProgress(self, progress):
        self.__progress = progress

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status
        
