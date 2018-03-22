import sys
#from PyQt5.QtWidgets import *
import PyQt5.QtWidgets

app = PyQt5.QtWidgets.QApplication(sys.argv)
print(sys.argv)
#label = PyQt5.QtWidgets.QLabel("Hello PyQt")
label = PyQt5.QtWidgets.QPushButton("Quit")
label.show()
app.exec_()