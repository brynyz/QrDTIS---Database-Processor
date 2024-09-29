from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from MainAppWindow import MainAppWindow

app = QApplication(sys.argv)

window = MainAppWindow()

window.show()
app.exec_()