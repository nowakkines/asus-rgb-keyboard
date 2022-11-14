
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor, QIcon, QPixmap
from PySide6.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QSlider
from PySide6.QtCore import QRect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Asus Rog")
        MainWindow.resize(505, 857)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label =QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 561, 1011))
        # self.label.setText("")
        self.label.setPixmap(QPixmap("github/asus-rgb-keyboard/asus-rgb-keyboad.jpg"))
        self.label.setObjectName("label")
        # MainWindow.setStyleSheet(u"QWidget {\n"
        #                          "                color: white;\n"
        #                          "               background-color: #121212;\n"
        #                          "                font-family: Rubik;\n"
        #                          "                font-size: 16pt;\n"
        #                          "                font-weight: 600;\n"
        #                          "                }\n"
        #                          "\n"
        #                          "                QPushButton {\n"
        #                          "                background-color: transparent;\n"
        #                          "                border: none;\n"
        #                          "                }\n"
        #                          "\n"
        #                          "                QPushButton:hover {\n"
        #                          "                background-color: #666;\n"
        #                          "                }\n"
        #                          "\n"
        #                          "                QPushButton:pressed {\n"
        #                         #  "                background-color: #888;\n"
        #                          "                }\n"
        #                          "            ")



        # self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        # self.label = QLabel(self.centralwidget)
        # self.label.setGeometry(QRect(0, 0, 561, 1011))
        # self.label.setText("")
        # self.lbl_temp = QLabel(self.centralwidget)
        # self.lbl_temp.setObjectName(u"github/asus-rgb-keyboard/asus-rgb-keyboad.jpg")


        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QRect(30, 420, 441, 51))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(20, 560, 141, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(180, 560, 141, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(340, 560, 141, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(180, 650, 141, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QRect(340, 650, 141, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QRect(20, 650, 141, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SINGLE STATIC"))
        self.pushButton_2.setText(_translate("MainWindow", "SINGLE BREATHING"))
        self.pushButton_3.setText(_translate("MainWindow", "RAINBOW"))
        self.pushButton_4.setText(_translate("MainWindow", "MUTI BREATHING"))
        self.pushButton_5.setText(_translate("MainWindow", "RAIBOW CYCLE"))
        self.pushButton_6.setText(_translate("MainWindow", "MULTI STATIC"))
