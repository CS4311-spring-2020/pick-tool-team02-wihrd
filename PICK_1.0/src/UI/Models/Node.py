from Models.LogEntry import logentry;

class node():
    
    def __init__(self, id, name, timestamp, description, logentry, creator, icon, artifact):
        self.__id = id;
        self.__name = name;
        self.__timestamp = timestamp;
        self.__description = description;
        self.__logEntry = logentry;
        self.__creator = creator;
        self.__icon = icon;
        self.artifact = artifact;
        self.__isvisible = True;

