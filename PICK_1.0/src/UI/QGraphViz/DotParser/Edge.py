class Edge():
    def __init__(self, source, dest, label):
        self.source = source
        self.dest = dest
        #self.label = label
        self.kwargs={}

        source.out_edges.append(self)
        dest.in_edges.append(self)

    def toDICT(self):
        edge_dic = {}
        edge_dic["source"]=self.source.name
        edge_dic["dest"]=self.dest.name
        edge_dic["kwargs"]=self.kwargs
        return edge_dic
    
