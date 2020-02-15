# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openweather.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../OneDrive/Зображення/5dcc613f1f00009304dee539.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 470, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 470, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, -10, 691, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 100, 361, 281))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuLanguage = QtWidgets.QMenu(self.menubar)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuUnits_temperature = QtWidgets.QMenu(self.menubar)
        self.menuUnits_temperature.setObjectName("menuUnits_temperature")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFahrenheit = QtWidgets.QAction(MainWindow)
        self.actionFahrenheit.setObjectName("actionFahrenheit")
        self.actionCelsius = QtWidgets.QAction(MainWindow)
        self.actionCelsius.setObjectName("actionCelsius")
        self.actionKelvin = QtWidgets.QAction(MainWindow)
        self.actionKelvin.setObjectName("actionKelvin")
        self.actionAfrikaans = QtWidgets.QAction(MainWindow)
        self.actionAfrikaans.setObjectName("actionAfrikaans")
        self.actionGerman = QtWidgets.QAction(MainWindow)
        self.actionGerman.setObjectName("actionGerman")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionFrench = QtWidgets.QAction(MainWindow)
        self.actionFrench.setObjectName("actionFrench")
        self.actionItalian = QtWidgets.QAction(MainWindow)
        self.actionItalian.setObjectName("actionItalian")
        self.actionJapanese = QtWidgets.QAction(MainWindow)
        self.actionJapanese.setObjectName("actionJapanese")
        self.actionKorean = QtWidgets.QAction(MainWindow)
        self.actionKorean.setObjectName("actionKorean")
        self.actionPolish = QtWidgets.QAction(MainWindow)
        self.actionPolish.setObjectName("actionPolish")
        self.actionRussian = QtWidgets.QAction(MainWindow)
        self.actionRussian.setObjectName("actionRussian")
        self.actionSwedish = QtWidgets.QAction(MainWindow)
        self.actionSwedish.setObjectName("actionSwedish")
        self.actionSpanish = QtWidgets.QAction(MainWindow)
        self.actionSpanish.setObjectName("actionSpanish")
        self.actionUkrainian = QtWidgets.QAction(MainWindow)
        self.actionUkrainian.setObjectName("actionUkrainian")
        self.actionChinese_Simplified = QtWidgets.QAction(MainWindow)
        self.actionChinese_Simplified.setObjectName("actionChinese_Simplified")
        self.actionChinese_Traditional = QtWidgets.QAction(MainWindow)
        self.actionChinese_Traditional.setObjectName("actionChinese_Traditional")
        self.menuLanguage.addAction(self.actionAfrikaans)
        self.menuLanguage.addAction(self.actionGerman)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionFrench)
        self.menuLanguage.addAction(self.actionItalian)
        self.menuLanguage.addAction(self.actionJapanese)
        self.menuLanguage.addAction(self.actionKorean)
        self.menuLanguage.addAction(self.actionPolish)
        self.menuLanguage.addAction(self.actionRussian)
        self.menuLanguage.addAction(self.actionSwedish)
        self.menuLanguage.addAction(self.actionSpanish)
        self.menuLanguage.addAction(self.actionUkrainian)
        self.menuLanguage.addAction(self.actionChinese_Simplified)
        self.menuLanguage.addAction(self.actionChinese_Traditional)
        self.menuUnits_temperature.addAction(self.actionFahrenheit)
        self.menuUnits_temperature.addAction(self.actionCelsius)
        self.menuUnits_temperature.addAction(self.actionKelvin)
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menuUnits_temperature.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenWeather"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kiev</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Current temperature in {city} is {data[\'main\'][\'temp\']} °C"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Description:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">- легка злива</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">- легкий снігопад</span></p></body></html>"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuUnits_temperature.setTitle(_translate("MainWindow", "Units temperature"))
        self.actionFahrenheit.setText(_translate("MainWindow", "Fahrenheit"))
        self.actionCelsius.setText(_translate("MainWindow", "Celsius"))
        self.actionKelvin.setText(_translate("MainWindow", "Kelvin"))
        self.actionAfrikaans.setText(_translate("MainWindow", "Afrikaans"))
        self.actionGerman.setText(_translate("MainWindow", "German"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionFrench.setText(_translate("MainWindow", "French"))
        self.actionItalian.setText(_translate("MainWindow", "Italian"))
        self.actionJapanese.setText(_translate("MainWindow", "Japanese"))
        self.actionKorean.setText(_translate("MainWindow", "Korean"))
        self.actionPolish.setText(_translate("MainWindow", "Polish"))
        self.actionRussian.setText(_translate("MainWindow", "Russian"))
        self.actionSwedish.setText(_translate("MainWindow", "Swedish"))
        self.actionSpanish.setText(_translate("MainWindow", "Spanish"))
        self.actionUkrainian.setText(_translate("MainWindow", "Ukrainian"))
        self.actionChinese_Simplified.setText(_translate("MainWindow", "Chinese Simplified"))
        self.actionChinese_Traditional.setText(_translate("MainWindow", "Chinese Traditional"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
