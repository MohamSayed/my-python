from PyQt5 import QtSql, QtGui, QtWidgets

def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                    "This example needs SQLite support. Please read "
                    "the Qt SQL driver documentation for information "
                    "how to build it.\n\n"
                    "Click Cancel to exit."),
                    QtGui.QMessageBox.Cancel)
        return False


    query = QtSql.QSqlQuery()

    # Initial values
    query.exec_("create table sportsmen(id int primary key, "
        "firstname varchar(20), lastname varchar(20), more varchar(50))")
    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer', 'extra 1')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo', 'extra 2)")
    db.commit()

    return True

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createDB()
