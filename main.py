#coding:utf8
import sys
from PyQt4 import QtCore,QtGui
from mainwidow import MainWindow
def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()