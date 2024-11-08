import sys
import random
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow
import ui

class Yellowcir(ui.Ui_Form):
    def __init__(self):
        super().__init__()

        self.pushButton.clicked.connect(self.add_circle)

        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 800, 600)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

    def add_circle(self):
        color = ['red', 'yellow', 'blue', 'green', 'brown', 'black', 'white', 'purple', 'pink']
        diameter = random.randint(20, 100)
        x = random.randint(0, 800 - diameter)
        y = random.randint(0, 600 - diameter)

        circle = QtWidgets.QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QtGui.QBrush(QtGui.QColor(random.choice(color))))
        self.scene.addItem(circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Yellowcir()
    window.show()
    sys.exit(app.exec())
