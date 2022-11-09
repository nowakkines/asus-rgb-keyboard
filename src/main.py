import sys  # argv in QApplication
from PyQt5 import QtWidgets

import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # access to variables, methods, etc in design.py
        super().__init__()
        self.setupUi(self)  #
       #it's necessary to initialize  our design


def main():
    app = QtWidgets.QApplication(sys.argv)  # new copy of QApplication
    window = ExampleApp()  # creating a object class of ExampleApp
    window.show()  # show window
    app.exec()  # run the app


if __name__ == '__main__':
    main()
