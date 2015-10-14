from PyQt4 import QtCore,QtGui
import data
import re
import urllib

class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        h_layout = QtGui.QHBoxLayout()
        self.l_edit = QtGui.QLineEdit()
        self.l_edit.setPlaceholderText('Paste Url here')
        self.add = QtGui.QPushButton("Add")
        h_layout.addWidget(self.l_edit)
        h_layout.addWidget(self.add)

        h_layout1 = QtGui.QHBoxLayout()
        self.l_edit1 = QtGui.QLineEdit()
        self.l_edit1.setPlaceholderText('Username(email)')
        self.l_edit2 = QtGui.QLineEdit()
        self.l_edit2.setPlaceholderText('Password')
        self.add1 = QtGui.QPushButton("Add")
        h_layout1.addWidget(self.l_edit1)
        h_layout1.addWidget(self.l_edit2)
        h_layout1.addWidget(self.add1)

        v_layout = QtGui.QVBoxLayout(self)
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout1)

        self.setconnect()

    def setconnect(self):
        self.add.clicked.connect(self.add_task)
        self.add1.clicked.connect(self.add_account)

    def add_task(self):
        url = self.l_edit.text()
        temp = re.search('kw=.+?&fr',url)
        if temp:
            key_word = temp.group()[3:-3]
            key_word = urllib.unquote(str(key_word))
            key_word = key_word.decode('gb2312')
            d = data.database()
            d._add('Task','baidutieba',key_word)
            d._done()
        self.close()

    def add_account(self):
        Username = self.l_edit1.text()
        Password = self.l_edit2.text()
        if Username and Password:
            d = data.database()
            d._add('Account','baidutieba',str(Username),str(Password))
            d._done()
        self.close()
