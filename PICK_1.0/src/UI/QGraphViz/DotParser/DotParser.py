import json

class DotParser():
    def __init__(self):
        pass

    def isParam_line(self, data):
        l=len(data)
        for (i,c) in enumerate(data):
            if c=="=":
                return True
            if c=="[":
                return False
            if i < l-1:
                if data[i:i+2]=="--":
                    return False
                if data[i:i+2]=="->":
                    return False
        return False  

    def isNode_line(self, data):
        l=len(data)
        for (i,c) in enumerate(data):
            if c=="[":
                return True
            if c=="}":
                return False
            if i < l-1:
                if data[i:i+2]=="--":
                    return False
                if data[i:i+2]=="->":
                    return False
        return True

    def isEdge_line(self, data, connection_sign="--"): 

        l=len(data)
        for (i,_) in enumerate(data):
            if i < l-1:
                if data[i:i+2]==connection_sign:
                    return True
        return False

    def has_params(self, data):
        for c in data:
            if c=="[":
                return True
            if c=="{":
                return False
        return False

    def find_params(self, data):
        try:
            start_idx=data.index("[")
            end_index=data.rindex("]")

            strparams = self.split(data[start_idx+1:end_index])#.split(",")
            params={}
            for param in strparams:
                vals = param.split("=")
                params[vals[0].strip()] = "=".join(vals[1:]).strip()
            return params, start_idx, end_index
        except:
            return None, 0, 0

    def toJSON(self, filename, graph):
        graph_dic = graph.toDICT()
        with open(filename, 'w') as fp:
            json.dump(graph_dic, fp, indent=4)