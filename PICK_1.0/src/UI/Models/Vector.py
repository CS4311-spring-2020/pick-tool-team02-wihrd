
from Models.LogEntry import logEntry
from Models.Graph import graph

class vector():
    
    def __init__(self, startDate, endDate, creator, description, name):
        self.__startDate = startDate
        self.__endDate = endDate
        self.__creator = creator
        self.__description = description
        self.__name = name
        self.__logentrys = []
        self.__graph = graph(self)
    
    def get_startDate(self):
      return self.__startDate

    def set_startDate(self, startDate):
      self.__startDate = startDate

    def get_endDate(self):
      return self.__endDate

    def set_endDate(self, endDate):
      self.__endDate = endDate

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