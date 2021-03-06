from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFontMetrics, QFont
from QGraphViz.Engines.LayoutEngine import LayoutEngine
from QGraphViz.DotParser.Graph import Graph, GraphType
class Dot(LayoutEngine):
    def __init__(self, graph):
        self.graph = graph
        self.default_node_width=100
        self.default_node_height=100
        self.default_min_nodes_dist=self.default_node_height
        self.font = QFont("Arial", 12)
        self.fm = QFontMetrics(self.font)
        self.margins=20
        self.graph.depth_x_pos = [0]

    def process(self, n, graph, index=0, nb_brothers=0, depth=0, stage=0):
        n.processed+=1
        width = 0
        height = 0
        if("pos" in n.kwargs):
            n.pos[0]=n.kwargs["pos"][0]
            n.pos[1]=n.kwargs["pos"][1]
            n.size[0]=n.kwargs["size"][0]
            n.size[1]=n.kwargs["size"][1]

            if len(graph.depth_x_pos)>depth:
                graph.depth_x_pos[depth] += n.size[0] + self.default_min_nodes_dist
            else:
                graph.depth_x_pos.append(n.size[0] + self.default_min_nodes_dist)

            for i,oe in enumerate(n.out_edges):
                if (oe.dest.processed<20):
                    self.process(oe.dest, graph, i,len(n.out_edges), depth=depth+1)

            return

        if("label" in n.kwargs.keys()):
            if(n.kwargs["label"]!=""):
                rect = self.fm.boundingRect(n.kwargs["label"])
                width=rect.width()+self.margins
                height=rect.height()+self.margins

        if width==0 or height==0:
            width=self.default_node_width
            height=self.default_node_height

        if(type(n)==Graph and self.show_subgraphs):
            n.depth_x_pos=[0]
            for nn in n.nodes:
                self.process(nn, n, 0, len(n.nodes), depth=depth)
            _,_,w_,h_=n.getRect()
            width = w_ if w_>width else width
            height = h_ if h_>height else height
            width += 2*self.margins
            height += 2*self.margins

        n.size[0]=width
        n.size[1]=height

        if len(n.in_edges)==0:
            n.pos[0]=graph.depth_x_pos[depth]+self.margins+width/2
            n.pos[1]=self.default_node_height/2+self.margins+height/2
            if len(graph.depth_x_pos)>depth:
                graph.depth_x_pos[depth] += width/2 + self.default_min_nodes_dist
            else:
                graph.depth_x_pos.append(width/2 + self.default_min_nodes_dist)
        else:
            x=(width/2 + self.default_min_nodes_dist)*(-(nb_brothers-1)/2+index)
            y=0
            for i,oe in enumerate(n.out_edges):
                if (oe.dest.processed<20):
                    self.process(oe.dest, graph, i,len(n.out_edges),depth=depth+1)

            for edg in n.in_edges:
                if (edg.source.processed==0):
                    self.process(edg.source, graph)
                if(n.parent_graph == edg.source.parent_graph):
                    x += edg.source.pos[0]
                    if(y<edg.source.pos[1]+height/2+self.default_min_nodes_dist):
                        y = edg.source.pos[1]+height/2+self.default_min_nodes_dist
            x/=len(n.in_edges)

            n.pos[0]=x
            n.pos[1]=y

        for i,oe in enumerate(n.out_edges):
            if oe.dest.processed<20:
                self.process(oe.dest, graph, i,len(n.out_edges))

        if(type(n)==Graph and self.show_subgraphs):
            n.depth_x_pos=[0]
            for nn in n.nodes:
                self.process(nn, n, 0, len(n.nodes), depth=depth)

    # Populate Graph with Nodes
    def build_graph(self, graph):
        for n in graph.nodes:
            n.processed=0
         
        for i,n in enumerate(graph.nodes):
            if(n.processed<3):
                self.process(n, graph)

        _,_,graph.size[0], graph.size[1] = graph.getRect()
        graph.pos[0] = graph.size[0] /2
        graph.pos[1] = graph.size[1] /2

    # Build Graph
    def build(self):
        self.graph.depth_x_pos = [0]
        self.build_graph(self.graph)
