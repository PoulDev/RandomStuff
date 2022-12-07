import os
import sys
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import *
import requests
from datetime import datetime

from ui_main import Ui_MainWindow as Ui_Main

def raw2json(raw : str) -> dict:
    output = {}
    for line in raw.splitlines():
        sepIndex = line.index(':')
        output[line[:sepIndex]] = line[sepIndex+2:]
    return output

def json2raw(jsonData : dict) -> str:
    return "\n".join(f'{name}: {value}' for name, value in jsonData.items())

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.send.clicked.connect(self.sendRequest)
        self.ui.send.setIcon(QIcon('Icons/send.png'))
        self.setWindowTitle('PyApi Tester | Developer: @PoulDev')
        self.ui.export_2.clicked.connect(self.export)

    def export(self):
        with open('exported.raw', 'wb') as f:
            f.write(self.res.content)
        os.startfile('.')

    def sendRequest(self):
        method = getattr(requests, self.ui.method.currentText().lower())
        kwargs = {
            'headers': raw2json(self.ui.requestHeaders.toPlainText()),
            'timeout': self.ui.timeout.value()
        }
        if method != requests.get:
            kwargs['data'] = self.ui.requestData.toPlainText()

        try:
            response = method(
                self.ui.url.text(),
                **kwargs
            )
            self.res = response
        except Exception as e:
            self.ui.statusBar.showMessage(f'[{datetime.now().strftime("%H:%M:%S")}] {type(e)}: {e}')
        else:
            self.ui.responseHeaders.setPlainText(json2raw(response.headers))
            self.ui.responseData.setPlainText(response.text)
            self.ui.statusBar.showMessage(f'[{datetime.now().strftime("%H:%M:%S")}] Request Sent')


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont()
    font.setFamilies([u"Poppins"])
    font.setPointSize(9)
    font.setBold(False)

    app.setFont(font)
    app.setWindowIcon(QIcon('Icons/logo.png'))
    window = MainWindow()
    window.show()
    app.exec()