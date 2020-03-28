
from Models.LogEntry import logEntry;
from Models.Graph import graph;

class vector():
    
    def __init__(self, daterange, creator, description, name):
        self.__daterange = daterange;
        self.__creator = creator;
        self.__description = description;
        self.__name = name;
        self.__logentrys = [];
        self.__graph = graph(self)


