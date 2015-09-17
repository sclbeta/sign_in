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
        self.l_view = QtGui.QListWidget()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.l_view)
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
                if bd.sign_in(name):
                    self.exe_all.setText(name)
                    time.sleep(5)
                self.exe_all.setText('Processing....')
                time.sleep(5)

    def add_func(self):
        d = dialog.Dialog(self)
        d.show()
