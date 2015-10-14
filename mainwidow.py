#coding:utf8
from PyQt4 import QtCore,QtGui
import data
import dialog
import baidu
import time

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        centralWidget = QtGui.QWidget()
        h_layout = QtGui.QHBoxLayout()
        v_layout = QtGui.QVBoxLayout()
        self.exe_all = QtGui.QPushButton("Start Signin")
        self.add = QtGui.QPushButton("Add")
        h_layout.addWidget(self.exe_all)
        h_layout.addWidget(self.add)
        h_layout1 = QtGui.QHBoxLayout()
        self.l_view = QtGui.QListWidget()
        self.l_view2 = QtGui.QListWidget()
        h_layout1.addWidget(self.l_view)
        h_layout1.addWidget(self.l_view2)
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout1)
        centralWidget.setLayout(v_layout)
        self.setCentralWidget(centralWidget)

        self.setconnect()
        self.set_l_list()
    def setconnect(self):
        self.exe_all.clicked.connect(self.exe_all_func)
        self.add.clicked.connect(self.add_func)

    def set_l_list(self):
        d = data.database()
        temp = d._search('Task','taskid','baidutieba')
        self.lists = []
        for i in temp:
            self.lists.append(i[1])
        qlist = QtCore.QStringList(self.lists)
        self.l_view.insertItems(0,qlist)

    def exe_all_func(self):
        d = data.database()
        account = d._search('Account','sitename','baidutieba')[0]
        bd = baidu.Baidu(account[1],account[2])
        self.exe_all.setText('Proccessing....')
        if bd.login():
            for name in self.lists:
                self.exe_all.setText('....')
                bd.sign_in(name)
                self.l_view2.insertItem(0,QtCore.QString(name))
        self.exe_all.setText('All Done!')

    def add_func(self):
        d = dialog.Dialog(self)
        d.show()
