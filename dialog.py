from PyQt4 import QtCore,QtGui
import data

class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        v_layout = QtGui.QVBoxLayout(self)
        h_layout = QtGui.QHBoxLayout()
        self.exe_all = QtGui.QPushButton("Start Signin")
        self.add = QtGui.QPushButton("Add")
        h_layout.addWidget(self.exe_all)
        h_layout.addWidget(self.add)
        self.l_view = QtGui.QListWidget()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.l_view)