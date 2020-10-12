'''
    @python @database @model @sql @sqlite
'''

# ptqt
from PyQt5 import QtCore, QtSql, QtWidgets
from PyQt5.QtWidgets import QHeaderView

# local
import sportsconnection #  from parent node example


def initializeModel(model):
    # Using connection from:
    #   self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #   self.db.setDatabaseName('sports.db')
    model.setTable('sportsmen')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "Extra")

def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow(model):
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)


def findrow(i):
    delrow = i.row()

def deleteRow(model, row):
    model.removeRow(row)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(788, 708)

        sportsconnection.createDB()

        # Any model will use this later
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('sports.db')

        model = QtSql.QSqlTableModel()
        initializeModel(model)

        view1 = createView("Table Model (View 1)", model)
        view1.clicked.connect(findrow)

        # Header size, fill parent, stretch
        for column in range(model.columnCount()):
            view1.horizontalHeader().setSectionResizeMode(column, QHeaderView.Stretch)

        layout = QtWidgets.QGridLayout(Form)
        layout.addWidget(view1)
        self.addRowButton = QtWidgets.QPushButton("Add a row")
        self.addRowButton.clicked.connect(lambda: addrow(model))
        layout.addWidget(self.addRowButton)
        self.deleteButton = QtWidgets.QPushButton("del a row")
        self.deleteButton.clicked.connect(lambda: deleteRow(model, view1.currentIndex().row()))
        layout.addWidget(self.deleteButton)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Window"))
        self.deleteButton.setText(_translate("Form", "delete row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


