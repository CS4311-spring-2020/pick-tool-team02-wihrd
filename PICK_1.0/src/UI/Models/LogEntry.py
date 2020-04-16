class logEntry():
    print("Test")

    def __init__(self, description, timestamp, name, path):
        self.__description = description
        self.__timestamp = timestamp
        self.__name = name
        self.__path = path

    #Get Description method
    def get_description(self):
      return self.__description

    #Set Description method
    def set_description(self, description):
      self.__description = description

    #Get Timestamp method
    def get_timestamp(self):
      return self.__timestamp

    #Set Timestamp method
    def set_timestamp(self, timestamp):
      self.__timestamp = timestamp

    #Get Name method
    def get_name(self):
      return self.__name

    #Set Name method
    def set_name(self, name):
      self.__name = name

    #Get Path method
    def get_path(self):
      return self.__path

    #Set Path method
    def set_path(self, path):
      self.__path = path