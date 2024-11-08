from PyQt6 import QtWidgets, uic, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow


class Ui_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(330, 460, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 761, 431))
        self.graphicsView.setObjectName("graphicsView")
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Кружок"))


