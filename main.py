from PyQt5.QtWidgets import QApplication
import sys
from widgets.login import Ui_Login

app = QApplication(sys.argv)
window = Ui_Login()
window.show()
app.exec_()

