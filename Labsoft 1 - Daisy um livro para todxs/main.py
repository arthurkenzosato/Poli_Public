import sys
from PyQt4 import QtGui
from tela_login import Ui_login

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Ui_login()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
