#/usr/bin/env python
import sys

from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
dlg = QDialog()

label = QLabel("Enter name:")
le = QLineEdit()
hl = QHBoxLayout()
hl.addWidget(label)
hl.addWidget(le)

bb = QDialogButtonBox(dlg)
bb.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)


def accepted():
	if le.text():
		print("LineEdit: OK")
		dlg.accept()
	else:
		print("LineEdit: Not OK")


bb.accepted.connect(accepted)
bb.rejected.connect(dlg.reject)

vl = QVBoxLayout(dlg)
vl.addLayout(hl)
vl.addWidget(bb)

retval = dlg.exec_()
name = le.text()

print("Dialog retval=%s, name entered=\"%s\"" % (retval, name))
