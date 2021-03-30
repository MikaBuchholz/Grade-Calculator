
from PyQt5 import QtCore, QtGui, QtWidgets
from backend import GradeCalcultor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 457)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 351, 41))
        self.label.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 180, 71, 20))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(300, 180, 31, 21))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 180, 31, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"       border-color: rgb(255, 255, 255);\n"
"    background-color: rgb(70, 135, 255);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(67, 123, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(210, 210, 80, 200))
        self.listWidget.setStyleSheet("border: none;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 220, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 300, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 260, 201, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 390, 75, 23))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"       border-color: rgb(255, 255, 255);\n"
"    background-color: rgb(70, 135, 255);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(67, 123, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 390, 75, 23))
        self.pushButton_3.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"       border-color: rgb(255, 255, 255);\n"
"    background-color: rgb(70, 135, 255);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(67, 123, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.calculator = GradeCalcultor(self.lineEdit, self.checkBox, self.listWidget, self.label_2, self.label_3, self.label_4)

        self.pushButton.clicked.connect(self.calculator.getValues)
        self.pushButton_2.clicked.connect(self.calculator.savePoints)
        self.pushButton_3.clicked.connect(self.calculator.clear)
        self.lineEdit.setValidator(QtGui.QIntValidator())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Noten Rechner"))
        self.label.setText(_translate("MainWindow", "Notendurchschnitt Rechner"))
        self.checkBox.setText(_translate("MainWindow", "LK"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "Eingegebener Punkt:"))
        self.label_3.setText(_translate("MainWindow", "Punktedurchschnitt:"))
        self.label_4.setText(_translate("MainWindow", "Notendurchschnitt:"))
        self.pushButton_2.setText(_translate("MainWindow", "Speichern"))
        self.pushButton_3.setText(_translate("MainWindow", "Neu"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
