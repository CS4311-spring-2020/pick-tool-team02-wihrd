class EAR():
    def __init__(self, name, time, desc, team, error):
        self.__name = name
        self.__time = time
        self.__desc = desc
        self.__team = team
        self.__error = error

    def getName(self):
        return self.__name

    def getTime(self):
        return self.__time

    def getDesc(self):
        return self.__desc

    def getTeam(self):
        return self.__team

    def getError(self):
        return self.__error

    def setName(self, name):
        self.__name = name

    def setTime(self, time):
        self.__time = time

    def setDesc(self, desc):
        self.__desc = desc

    def setTeam(self, team):
        self.__team = team

    def setError(self, error):
        self.__error = error