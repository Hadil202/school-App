from PySide6.QtWidgets import QApplication
from frontPage import MysideBar
import sys

app = QApplication(sys.argv)
window = MysideBar() 
window.show()
app.exec()
