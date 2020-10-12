from PyQt5 import QtWidgets, uic
import sys


# Class structure is different than normal structure
class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        super(Ui, self).__init__()

        # Must be main window type, not a dialog nor widget, since it the
        # skeleton of this application.
        uic.loadUi('mainwindow.ui', self)

        obj = self.findChild(QtWidgets.QPushButton, "pushButton")
        obj.clicked.connect(lambda: print("Obj clicked"))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
