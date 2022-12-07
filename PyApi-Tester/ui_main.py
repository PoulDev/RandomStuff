# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setMinimumSize(QSize(700, 400))
        MainWindow.setStyleSheet(u"background: #16161a;\n"
"color: #fffffe")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.method = QComboBox(self.centralwidget)
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.setObjectName(u"method")
        self.method.setMinimumSize(QSize(100, 20))
        self.method.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.method)

        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")
        self.url.setMinimumSize(QSize(0, 20))
        self.url.setMaximumSize(QSize(16777215, 20))
        self.url.setStyleSheet(u"color: white;\n"
"background: #242629;\n"
"border: 2px solid #7f5af0;")

        self.horizontalLayout.addWidget(self.url)

        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.setMinimumSize(QSize(70, 20))
        self.send.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: #7f5af0;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.send)

        self.timeout = QSpinBox(self.centralwidget)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setMinimumSize(QSize(50, 20))
        self.timeout.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(10)
        self.timeout.setFont(font)
        self.timeout.setStyleSheet(u"color: white;\n"
"background: #242629;\n"
"border: 2px solid #7f5af0;")
        self.timeout.setValue(3)

        self.horizontalLayout.addWidget(self.timeout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.requestHeaders = QPlainTextEdit(self.centralwidget)
        self.requestHeaders.setObjectName(u"requestHeaders")
        self.requestHeaders.setFont(font)
        self.requestHeaders.setStyleSheet(u"color: white;\n"
"background: #242629;\n"
"border: 2px solid #7f5af0;")

        self.horizontalLayout_2.addWidget(self.requestHeaders)

        self.responseHeaders = QTextBrowser(self.centralwidget)
        self.responseHeaders.setObjectName(u"responseHeaders")
        self.responseHeaders.setFont(font)
        self.responseHeaders.setStyleSheet(u"color: white;\n"
"background: #242629;\n"
"border: 2px solid #7f5af0;")

        self.horizontalLayout_2.addWidget(self.responseHeaders)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.requestData = QTextEdit(self.centralwidget)
        self.requestData.setObjectName(u"requestData")
        self.requestData.setMinimumSize(QSize(0, 70))
        self.requestData.setMaximumSize(QSize(16777215, 16777215))
        self.requestData.setFont(font)
        self.requestData.setStyleSheet(u"color: white;\n"
"background: #242629;\n"
"border: 2px solid #7f5af0;")

        self.horizontalLayout_4.addWidget(self.requestData)

        self.responseData = QTextBrowser(self.centralwidget)
        self.responseData.setObjectName(u"responseData")
        self.responseData.setFont(font)
        self.responseData.setStyleSheet(u"color: white;\n"
"background: #242629;\n"
"border: 2px solid #7f5af0;")

        self.horizontalLayout_4.addWidget(self.responseData)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.export_2 = QPushButton(self.centralwidget)
        self.export_2.setObjectName(u"export_2")
        self.export_2.setMinimumSize(QSize(0, 20))
        self.export_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: #7f5af0;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.export_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.method.setItemText(0, QCoreApplication.translate("MainWindow", u"GET", None))
        self.method.setItemText(1, QCoreApplication.translate("MainWindow", u"POST", None))
        self.method.setItemText(2, QCoreApplication.translate("MainWindow", u"PUT", None))
        self.method.setItemText(3, QCoreApplication.translate("MainWindow", u"PATCH", None))
        self.method.setItemText(4, QCoreApplication.translate("MainWindow", u"DELETE", None))

        self.url.setText(QCoreApplication.translate("MainWindow", u"http://localhost:80/", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Response", None))
        self.requestHeaders.setPlainText(QCoreApplication.translate("MainWindow", u"User-Agent: PyApiTester/1.0.0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Request Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Response Data", None))
        self.requestData.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"Export Response", None))
    # retranslateUi

