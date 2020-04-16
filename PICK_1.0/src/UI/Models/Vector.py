
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
    
    def get_daterange(self):
      return self.__daterange

    def set_daterange(self, daterange):
      self.__daterange = daterange

    def get_creator(self):
      return self.__creator

    def set_creator(self, creator):
      self.__creator = creator

    def get_description(self):
      return self.__description

    def set_description(self, description):
      self.__description = description

    def get_name(self):
      return self.__name

    def set_name(self, name):
      self.__name = name

    def get_logentrys(self):
      return self.__logentrys

    def set_logentrys(self, logentrys):
      self.__logentrys = logentrys

    def get_graph(self):
      return self.__graph
    
    def set_graph(self, graph):
      self.__graph = graph