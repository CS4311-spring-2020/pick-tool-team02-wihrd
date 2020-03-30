from Models.Vector import vector
class graph():
    def __init__(self, vector):
        self.__vector = vector
        self.__nodes = []
        self.__associations = []
        
    #Get Vector method
    def get_vector(self):
      return self.__vector

    #Set Vector method
    def set_vector(self, vector):
        self.__vector = vector

    #Get Nodes method
    def get_nodes(self):
      return self.__nodes

    #Set Nodes method
    def set_nodes(self, nodes):
        self.__nodes = nodes

    #Get Associations method
    def get_associations(self):
      return self.__associations

    #Set Associations method
    def set_associations(self, associations):
        self.__associations = associations