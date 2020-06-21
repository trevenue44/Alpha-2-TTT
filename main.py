from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.player = 'X'
        self.win = False
        self.winner = None
        self.draw = False
        self.xscore = 0
        self.oscore = 0
        self.addscore = True

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 0, 541, 511))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.B1 = QtWidgets.QPushButton(self.groupBox)
        self.B1.setGeometry(QtCore.QRect(20, 20, 161, 151))
        self.B1.setText("")
        self.B1.setObjectName("B1")
        self.B2 = QtWidgets.QPushButton(self.groupBox)
        self.B2.setGeometry(QtCore.QRect(190, 20, 161, 151))
        self.B2.setText("")
        self.B2.setObjectName("B2")
        self.B3 = QtWidgets.QPushButton(self.groupBox)
        self.B3.setGeometry(QtCore.QRect(360, 20, 161, 151))
        self.B3.setText("")
        self.B3.setObjectName("B3")
        self.B4 = QtWidgets.QPushButton(self.groupBox)
        self.B4.setGeometry(QtCore.QRect(20, 180, 161, 151))
        self.B4.setText("")
        self.B4.setObjectName("B4")
        self.B5 = QtWidgets.QPushButton(self.groupBox)
        self.B5.setGeometry(QtCore.QRect(190, 180, 161, 151))
        self.B5.setText("")
        self.B5.setObjectName("B5")
        self.B6 = QtWidgets.QPushButton(self.groupBox)
        self.B6.setGeometry(QtCore.QRect(360, 180, 161, 151))
        self.B6.setText("")
        self.B6.setObjectName("B6")
        self.B7 = QtWidgets.QPushButton(self.groupBox)
        self.B7.setGeometry(QtCore.QRect(20, 340, 161, 151))
        self.B7.setText("")
        self.B7.setObjectName("B7")
        self.B8 = QtWidgets.QPushButton(self.groupBox)
        self.B8.setGeometry(QtCore.QRect(190, 340, 161, 151))
        self.B8.setText("")
        self.B8.setObjectName("B8")
        self.B9 = QtWidgets.QPushButton(self.groupBox)
        self.B9.setGeometry(QtCore.QRect(360, 340, 161, 151))
        self.B9.setText("")
        self.B9.setObjectName("B9")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(250, 520, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # score label
        self.scorelabel = QtWidgets.QLabel(self.centralwidget)
        self.scorelabel.setGeometry(QtCore.QRect(100, 580, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        self.scorelabel.setFont(font)
        self.scorelabel.setObjectName("scorelabel")
        self.scorelabel.setText(f'Scores:\t\tX:{self.xscore}\tO:{self.oscore}')

        # restart button
        self.restart = QtWidgets.QPushButton(self.centralwidget)
        self.restart.setGeometry(QtCore.QRect(500, 580, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(10)
        self.restart.setFont(font)
        self.restart.setObjectName("restart")
        self.restart.setText('Restart')

        # setting what happens when the buttons are clicked
        self.B1.clicked.connect(lambda: self.clicked(self.B1))
        self.B2.clicked.connect(lambda: self.clicked(self.B2))
        self.B3.clicked.connect(lambda: self.clicked(self.B3))
        self.B4.clicked.connect(lambda: self.clicked(self.B4))
        self.B5.clicked.connect(lambda: self.clicked(self.B5))
        self.B6.clicked.connect(lambda: self.clicked(self.B6))
        self.B7.clicked.connect(lambda: self.clicked(self.B7))
        self.B8.clicked.connect(lambda: self.clicked(self.B8))
        self.B9.clicked.connect(lambda: self.clicked(self.B9))

        # setting what happens when restart is clicked
        self.restart.clicked.connect(self.restart_clicked)

    # fxn for what happens when a button is clicked
    def clicked(self, button):
        if not self.win:
            if self.player == 'X' and button.text() == '':
                button.setText('X')
                self.player = 'O'
                self.label1.setText("O's Turn")
                self.label1.adjustSize()
            elif self.player == 'O' and button.text() == '':
                button.setText('O')
                self.player = 'X'
                self.label1.setText("X's Turn")
                self.label1.adjustSize()
        self.check_for_draw()
        if self.draw:
            self.label1.setText('Draw. No Winner')
            self.label1.setGeometry(QtCore.QRect(180, 520, 241, 51))
            self.label1.adjustSize()
            self.draw = False
        self.check_for_winner()
        if self.win:
            self.label1.setText(f'Winner: {self.winner}')
            self.label1.setGeometry(QtCore.QRect(245, 520, 241, 51))
            self.label1.adjustSize()
            if self.addscore:
                if self.winner == 'X':
                    self.xscore += 1
                if self.winner == 'O':
                    self.oscore += 1
                self.scorelabel.setText(
                    f'Scores:\t\tX: {self.xscore}\tO: {self.oscore}')
                self.scorelabel.adjustSize()
                self.addscore = False

    def check_for_draw(self):
        if (self.B1.text() and self.B2.text() and self.B3.text() and self.B4.text() and self.B5.text() and self.B6.text() and self.B7.text() and self.B8.text() and self.B9.text()) != '':
            self.draw = True

    def check_for_winner(self):
        # checking horizontals
        if self.B1.text() == self.B2.text() == self.B3.text() != '':
            self.win = True
            self.winner = self.B1.text()
        elif self.B4.text() == self.B5.text() == self.B6.text() != '':
            self.win = True
            self.winner = self.B4.text()
        elif self.B7.text() == self.B8.text() == self.B9.text() != '':
            self.win = True
            self.winner = self.B7.text()
        # checking verticals
        elif self.B1.text() == self.B4.text() == self.B7.text() != '':
            self.win = True
            self.winner = self.B1.text()
        elif self.B2.text() == self.B5.text() == self.B8.text() != '':
            self.win = True
            self.winner = self.B2.text()
        elif self.B3.text() == self.B6.text() == self.B9.text() != '':
            self.win = True
            self.winner = self.B3.text()
        # checking diagonals
        elif self.B1.text() == self.B5.text() == self.B9.text() != '':
            self.win = True
            self.winner = self.B1.text()
        elif self.B3.text() == self.B5.text() == self.B7.text() != '':
            self.win = True
            self.winner = self.B5.text()
        else:
            self.win = False
            self.winner = None

    # when restart is clicked
    def restart_clicked(self):
        self.B1.setText('')
        self.B2.setText('')
        self.B3.setText('')
        self.B4.setText('')
        self.B5.setText('')
        self.B6.setText('')
        self.B7.setText('')
        self.B8.setText('')
        self.B9.setText('')
        self.addscore = True
        self.player = 'X'
        self.win = False
        self.label1.setText("X's Turn")
        self.label1.setGeometry(QtCore.QRect(250, 520, 241, 51))
        self.label1.adjustSize()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Tic Tac Toe", "Tic Tac Toe"))
        self.label1.setText(_translate("MainWindow", "X\'s Turn"))


# if __name__ == "__main__":
def mywin():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


mywin()
