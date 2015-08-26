#coding:utf8
from PyQt4 import QtCore,QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi()
        self.setconnect()
    def setupUi(self):
        centralWidget = QtGui.QWidget()
        h_layout = QtGui.QHBoxLayout()
        v_layout = QtGui.QVBoxLayout()
        self.exe_all = QtGui.QPushButton("Start Checkin")
        self.add = QtGui.QPushButton("Add")
        h_layout.addWidget(self.exe_all)
        h_layout.addWidget(self.add)
        self.t_view = QtGui.QTableView()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.t_view)
        centralWidget.setLayout(v_layout)
        self.setCentralWidget(centralWidget)
    def setconnect(self):
        self.exe_all.clicked.connect(self.exe_all_func)
        self.add.clicked.connect(self.add_func)
    def exe_all_func(self):
        print "exe_all_func"
    def add_func(self):
        print "add_func"