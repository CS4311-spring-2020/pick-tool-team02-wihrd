from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel
import sys
import os
sys.path.insert(1,os.path.dirname(__file__)+"/..")
print(sys.path)
from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
from QGraphViz.DotParser import Graph, GraphType
from QGraphViz.Engines import Dot

if __name__ == "__main__":
    # Create QT application
    app = QApplication(sys.argv)

    # Event Node Selected
    def node_selected(node):
        if(qgv.manipulation_mode==QGraphVizManipulationMode.Node_remove_Mode):
            print("Node {} removed".format(node))
        else:
            print("Node selected {}".format(node))

    # Event Edge Selected
    def edge_selected(edge):
        if(qgv.manipulation_mode==QGraphVizManipulationMode.Edge_remove_Mode):
            print("Edge {} removed".format(edge))
        else:
            print("Edge selected {}".format(edge))

    # Node & Edge Invoked and Removed
    def node_invoked(node):
        print("Node double clicked")
    def edge_invoked(node):
        print("Edge double clicked")
    def node_removed(node):
        print("Node removed")
    def edge_removed(node):
        print("Edge removed")
        
    # Create QGraphViz widget
    qgv = QGraphViz(
        auto_freeze= True,
        node_selected_callback=node_selected,
        edge_selected_callback=edge_selected,
        node_invoked_callback=node_invoked,
        edge_invoked_callback=edge_invoked,
        node_removed_callback=node_removed,
        edge_removed_callback=edge_removed,

        hilight_Nodes=True,
        hilight_Edges=True
        )
    qgv.setStyleSheet("background-color:gray;")
    # Create A new Graph using Dot layout engine
    qgv.new(Dot(Graph("Main_Graph")))

    # Build the graph
    qgv.build()
    # Create Main window
    main = QMainWindow()
    main.setWindowTitle('Graph View')
    # Create a central widget to handle the QGraphViz object
    wi=QWidget()
    wi.setLayout(QHBoxLayout())
    main.setCentralWidget(wi)
    # Add the QGraphViz object to the layout
    wi.layout().addWidget(qgv)
    # Add a layout for buttons
    vLayout=QVBoxLayout()
    wi.layout().addLayout(vLayout)

    # Manipulate Button functionality
    def manipulate():
        qgv.manipulation_mode=QGraphVizManipulationMode.Nodes_Move_Mode

    # Export Button functionality
    def export():
        fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.json")
        if(fname[0]!=""):
            qgv.saveAsJson(fname[0])

    # Add Node Button functionality
    def add_node():
        dlg = QDialog()
        dlg.ok=False
        dlg.node_name=""
        dlg.node_label=""
        dlg.node_color = "None"
        dlg.node_icon = ""

        # Layouts
        main_layout = QVBoxLayout()
        l = QFormLayout()
        buttons_layout = QHBoxLayout()

        main_layout.addLayout(l)
        main_layout.addLayout(buttons_layout)
        dlg.setLayout(main_layout)

        leNodeName = QLineEdit()
        leNodeLabel = QLineEdit()
        cbxNodeColor = QComboBox()

        #OK & Cancel Button
        pbOK = QPushButton()
        pbCancel = QPushButton()

        cbxNodeColor.addItems(["white.png","red.png","blue.png"])
        pbOK.setText("&OK")
        pbCancel.setText("&Cancel")

        l.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
        l.setWidget(0, QFormLayout.FieldRole, leNodeName)
        l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
        l.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
        l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Icon"))
        l.setWidget(2, QFormLayout.FieldRole, cbxNodeColor)

        def ok():
            dlg.OK=True
            dlg.node_name = leNodeName.text()
            dlg.node_label = leNodeLabel.text()
            dlg.node_color = cbxNodeColor.currentText()
            dlg.close()

        def cancel():
            dlg.OK=False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        # Choosing between Icons
        if dlg.OK and dlg.node_name != '' and dlg.node_color == 'white.png':
            dlg.node_icon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\white.png"
            qgv.addNode(qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_icon)
            qgv.build()
        elif dlg.OK and dlg.node_name != '' and dlg.node_color == 'red.png':
            dlg.node_icon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\red.png"
            qgv.addNode(qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_icon)
            qgv.build()
        elif dlg.OK and dlg.node_name != '' and dlg.node_color == 'blue.png':
            dlg.node_icon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\blue.png"
            qgv.addNode(qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_icon)
            qgv.build()

    # Remove Node Button functionality
    def remove_node():
        qgv.manipulation_mode=QGraphVizManipulationMode.Node_remove_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnRemNode.setChecked(True)

    # Remove Edge Button functionality
    def remove_edge():
        qgv.manipulation_mode=QGraphVizManipulationMode.Edge_remove_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnRemEdge.setChecked(True)

    # Add Edge Button functionality
    def add_edge():
        qgv.manipulation_mode=QGraphVizManipulationMode.Edges_Connect_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnAddEdge.setChecked(True)

    # Button Layout
    # Export Button
    btnSave = QPushButton("Export")
    btnSave.clicked.connect(export)
    vLayout.addWidget(btnSave)

    # Manipulate Button
    buttons_list=[]
    btnManip = QPushButton("Manipulate")    
    btnManip.setCheckable(True)
    btnManip.setChecked(True)
    btnManip.clicked.connect(manipulate)
    vLayout.addWidget(btnManip)
    buttons_list.append(btnManip)

    # Add Node Button
    btnAddNode = QPushButton("Add Node")    
    btnAddNode.clicked.connect(add_node)
    vLayout.addWidget(btnAddNode)
    buttons_list.append(btnManip)

    #Remove Node Button
    btnRemNode = QPushButton("Remove Node")
    btnRemNode.setCheckable(True)
    btnRemNode.clicked.connect(remove_node)
    vLayout.addWidget(btnRemNode)
    buttons_list.append(btnRemNode)

    # Add Edge Button
    btnAddEdge = QPushButton("Add Edge")    
    btnAddEdge.setCheckable(True)
    btnAddEdge.clicked.connect(add_edge)
    vLayout.addWidget(btnAddEdge)
    buttons_list.append(btnAddEdge)

    # Remove Edge Button
    btnRemEdge = QPushButton("Remove Edge")
    btnRemEdge.setCheckable(True)
    btnRemEdge.clicked.connect(remove_edge)
    vLayout.addWidget(btnRemEdge)
    buttons_list.append(btnRemEdge)

    main.showMaximized()
    
    sys.exit(app.exec_())