import sys

from PyQt5 import QtWidgets, QtQui, QtCore


class UI():
	def initUi(self, Form):
		self.label = QtWidgets.QLabel("label")
		layout = QtWidgets.QGridLayout(Form)
		layout.addWidget(self.label)
		

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = UI()
	ui.initUi(Form)
	Form.show()
	sys.exit(app.exec_())

