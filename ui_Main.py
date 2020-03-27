# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steps.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import problemGen


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(320, 30, 341, 181))
        self.label.setObjectName("label")
        self.welcomeBtn = QtWidgets.QPushButton(self.home)
        self.welcomeBtn.setGeometry(QtCore.QRect(340, 310, 113, 32))
        self.welcomeBtn.setObjectName("welcomeBtn")
        self.stackedWidget.addWidget(self.home)

        self.menu = QtWidgets.QWidget()
        self.menu.setObjectName("menu")
        self.Info = QtWidgets.QLabel(self.menu)
        self.Info.setGeometry(QtCore.QRect(330, 70, 181, 16))
        self.Info.setObjectName("Info")
        self.lowerBeads = QtWidgets.QLabel(self.menu)
        self.lowerBeads.setGeometry(QtCore.QRect(110, 120, 151, 16))
        self.lowerBeads.setObjectName("lowerBeads")
        self.prob1btn = QtWidgets.QPushButton(self.menu)
        self.prob1btn.setGeometry(QtCore.QRect(130, 140, 113, 32))
        self.prob1btn.setObjectName("prob1btn")
        self.prob2btn = QtWidgets.QPushButton(self.menu)
        self.prob2btn.setGeometry(QtCore.QRect(130, 170, 113, 32))
        self.prob2btn.setObjectName("prob2btn")
        self.upperBeads = QtWidgets.QLabel(self.menu)
        self.upperBeads.setGeometry(QtCore.QRect(110, 210, 151, 16))
        self.upperBeads.setObjectName("upperBeads")
        self.mixedBeads = QtWidgets.QLabel(self.menu)
        self.mixedBeads.setGeometry(QtCore.QRect(110, 240, 151, 16))
        self.mixedBeads.setObjectName("mixedBeads")
        self.stackedWidget.addWidget(self.menu)


        self.step1_1 = QtWidgets.QWidget()
        self.step1_1.setObjectName("step1_1")
        self.int_1 = QtWidgets.QLabel(self.step1_1)
        self.int_1.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_1.setObjectName("int_1")
        self.nextbtn1_1 = QtWidgets.QPushButton(self.step1_1)
        self.nextbtn1_1.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn1_1.setObjectName("nextbtn1_1")
        self.stackedWidget.addWidget(self.step1_1)

        self.step1_2 = QtWidgets.QWidget()
        self.step1_2.setObjectName("step1_2")
        self.int_2 = QtWidgets.QLabel(self.step1_2)
        self.int_2.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_2.setObjectName("int_2")
        self.int_2.setText("int_2")
        self.nextbtn1_2 = QtWidgets.QPushButton(self.step1_2)
        self.nextbtn1_2.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn1_2.setObjectName("nextbtn1_2")
        self.nextbtn1_2.setText("Next Step")
        self.stackedWidget.addWidget(self.step1_2)

        self.step1_3 = QtWidgets.QWidget()
        self.step1_3.setObjectName("step1_3")
        self.int_3 = QtWidgets.QLabel(self.step1_3)
        self.int_3.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_3.setObjectName("int_3")
        self.int_3.setText("int_3")
        self.nextbtn1_3 = QtWidgets.QPushButton(self.step1_3)
        self.nextbtn1_3.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn1_3.setObjectName("nextbtn1_3")
        self.nextbtn1_3.setText("Next Step")
        self.stackedWidget.addWidget(self.step1_3)

        self.step1_4 = QtWidgets.QWidget()
        self.int_4 = QtWidgets.QLabel(self.step1_4)
        self.int_4.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_4.setObjectName("int_4")
        self.int_4.setText("int_4")
        self.nextbtn1_4 = QtWidgets.QPushButton(self.step1_4)
        self.nextbtn1_4.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn1_4.setObjectName("nextbtn1_4")
        self.nextbtn1_4.setText("Next Step")
        self.step1_4.setObjectName("step1_4")
        self.stackedWidget.addWidget(self.step1_4)

        self.step1_f = QtWidgets.QWidget()
        self.int_f = QtWidgets.QLabel(self.step1_f)
        self.int_f.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_f.setObjectName("int_f")
        self.int_f.setText("int_f")
        self.nextbtn1_f = QtWidgets.QPushButton(self.step1_f)
        self.nextbtn1_f.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn1_f.setObjectName("nextbtn1_f")
        self.nextbtn1_f.setText("Good work!")
        self.step1_f.setObjectName("step1_f")
        self.stackedWidget.addWidget(self.step1_f)

        self.step2_1 = QtWidgets.QWidget()
        self.int_2_1 = QtWidgets.QLabel(self.step2_1)
        self.int_2_1.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_2_1.setObjectName("int_2_1")
        self.int_2_1.setText("int_2_1")
        self.nextbtn2_1 = QtWidgets.QPushButton(self.step2_1)
        self.nextbtn2_1.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn2_1.setObjectName("nextbtn2_1")
        self.nextbtn2_1.setText("Next Step")
        self.step2_1.setObjectName("step2_1")
        self.stackedWidget.addWidget(self.step2_1)

        self.step2_2 = QtWidgets.QWidget()
        self.step2_2.setObjectName("step2_2")
        self.int_2_2 = QtWidgets.QLabel(self.step2_2)
        self.int_2_2.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_2_2.setObjectName("int_2_2")
        self.int_2_2.setText("int_2_2")
        self.nextbtn2_2 = QtWidgets.QPushButton(self.step2_2)
        self.nextbtn2_2.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn2_2.setObjectName("nextbtn2_2")
        self.nextbtn2_2.setText("Next Step")
        self.step2_2.setObjectName("step2_2")
        self.stackedWidget.addWidget(self.step2_2)

        self.step2_3 = QtWidgets.QWidget()
        self.step2_3.setObjectName("step2_3")
        self.int_2_3 = QtWidgets.QLabel(self.step2_3)
        self.int_2_3.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_2_3.setObjectName("int_2_3")
        self.int_2_3.setText("int_2_3")
        self.nextbtn2_3 = QtWidgets.QPushButton(self.step2_3)
        self.nextbtn2_3.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn2_3.setObjectName("nextbtn2_3")
        self.nextbtn2_3.setText("Next Step")
        self.step2_3.setObjectName("step2_3")
        self.stackedWidget.addWidget(self.step2_3)

        self.step2_4 = QtWidgets.QWidget()
        self.step2_4.setObjectName("step2_4")
        self.int_2_4 = QtWidgets.QLabel(self.step2_4)
        self.int_2_4.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_2_4.setObjectName("int_2_4")
        self.int_2_4.setText("int_2_4")
        self.nextbtn2_4 = QtWidgets.QPushButton(self.step2_4)
        self.nextbtn2_4.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn2_4.setObjectName("nextbtn2_4")
        self.nextbtn2_4.setText("Next Step")
        self.step2_4.setObjectName("step2_4")
        self.stackedWidget.addWidget(self.step2_4)

        self.step2_f = QtWidgets.QWidget()
        self.step2_f.setObjectName("step2_f")
        self.int_2_f = QtWidgets.QLabel(self.step2_f)
        self.int_2_f.setGeometry(QtCore.QRect(420, 120, 111, 16))
        self.int_2_f.setObjectName("int_2_f")
        self.int_2_f.setText("int_2_f")
        self.nextbtn2_f = QtWidgets.QPushButton(self.step2_f)
        self.nextbtn2_f.setGeometry(QtCore.QRect(390, 160, 113, 32))
        self.nextbtn2_f.setObjectName("nextbtn2_f")
        self.nextbtn2_f.setText("Good work!")
        self.step2_f.setObjectName("step2_f")
        self.stackedWidget.addWidget(self.step2_f)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)


        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuPrototype_ver_0_1 = QtWidgets.QMenu(self.menubar)
        self.menuPrototype_ver_0_1.setObjectName("menuPrototype_ver_0_1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPrototype_ver_0_1.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Buttons n shit
        self.welcomeBtn.clicked.connect(self.nextPage)
        self.prob1btn.clicked.connect(self.startProb1)
        self.nextbtn1_1.clicked.connect(self.step1_2btn)
        self.nextbtn1_2.clicked.connect(self.step1_3btn)
        self.nextbtn1_3.clicked.connect(self.step1_4btn)
        self.nextbtn1_4.clicked.connect(self.step1_fbtn)
        #return to home screen
        self.nextbtn1_f.clicked.connect(self.oneToHome)

        self.prob2btn.clicked.connect(self.startProb2)
        self.nextbtn2_1.clicked.connect(self.step2_2btn)
        self.nextbtn2_2.clicked.connect(self.step2_3btn)
        self.nextbtn2_3.clicked.connect(self.step2_4btn)
        self.nextbtn2_4.clicked.connect(self.step2_fbtn)
        self.nextbtn2_f.clicked.connect(self.twoToHome)

    def settingInts1(self, prob):
        temp = str(prob[0])
        self.int_1.setText(temp)
        if(prob[2] < 0):
            temp = prob[1] + str(-1 * prob[2])
        else:
            temp = prob[1] + str(prob[2])
        self.int_2.setText(temp)
        if(prob[4] < 0):
            temp = prob[3] + str(-1 * prob[4])
        else:
            temp = prob[3] + str(prob[4])
        self.int_3.setText(temp)
        if(prob[6] < 0):
            temp = prob[5] + str(-1* prob[6])
        else:
            temp = prob[5] + str(prob[6])
        self.int_4.setText(temp)
        finalAns = []
        for i in range(0,7,2):
            finalAns.append(prob[i])
        self.int_f.setText(str(sum(finalAns)))

    def settingInts2(self, prob):
        temp = str(prob[0])
        self.int_2_1.setText(temp)
        if(prob[2] < 0):
            temp = prob[1] + str(-1 * prob[2])
        else:
            temp = prob[1] + str(prob[2])
        self.int_2_2.setText(temp)
        if(prob[4] < 0):
            temp = prob[3] + str(-1 * prob[4])
        else:
            temp = prob[3] + str(prob[4])
        self.int_2_3.setText(temp)
        if(prob[6] < 0):
            temp = prob[5] + str(-1* prob[6])
        else:
            temp = prob[5] + str(prob[6])
        self.int_2_4.setText(temp)
        finalAns = []
        for i in range(0,7,2):
            finalAns.append(prob[i])
        self.int_2_f.setText(str(sum(finalAns)))

    #Functionality
        #Home to Menu
    def nextPage(self):
        self.stackedWidget.setCurrentWidget(self.menu)
        #Star problem 1
    def startProb1(self):
        self.stackedWidget.setCurrentWidget(self.step1_1)
    def step1_2btn(self):
        self.stackedWidget.setCurrentWidget(self.step1_2)
    def step1_3btn(self):
        self.stackedWidget.setCurrentWidget(self.step1_3)
    def step1_4btn(self):
        self.stackedWidget.setCurrentWidget(self.step1_4)
    def step1_fbtn(self):
        self.stackedWidget.setCurrentWidget(self.step1_f)
    def oneToHome(self):
        self.stackedWidget.setCurrentWidget(self.menu)

    def startProb2(self):
        self.stackedWidget.setCurrentWidget(self.step2_1)
    def step2_2btn(self):
        self.stackedWidget.setCurrentWidget(self.step2_2)
    def step2_3btn(self):
        self.stackedWidget.setCurrentWidget(self.step2_3)
    def step2_4btn(self):
        self.stackedWidget.setCurrentWidget(self.step2_4)
    def step2_fbtn(self):
        self.stackedWidget.setCurrentWidget(self.step2_f)
    def twoToHome(self):
        self.stackedWidget.setCurrentWidget(self.menu)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Anzan Practice Problems"))
        self.welcomeBtn.setText(_translate("MainWindow", "Continue"))
        self.Info.setText(_translate("MainWindow", "Pracitce Problems by Level"))
        self.lowerBeads.setText(_translate("MainWindow", "Chapter 1: Lower Beads"))
        self.prob1btn.setText(_translate("MainWindow", "Problem 1"))
        self.prob2btn.setText(_translate("MainWindow", "Problem 2"))
        self.upperBeads.setText(_translate("MainWindow", "Chapter 2: Upper Beads"))
        self.mixedBeads.setText(_translate("MainWindow", "Chapter 3: Mixed Beads"))
        self.int_1.setText(_translate("MainWindow", "Integer"))
        self.nextbtn1_1.setText(_translate("MainWindow", "Next Step"))
        self.menuPrototype_ver_0_1.setTitle(_translate("MainWindow", "Prototype ver. 0.1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    prob1 = problemGen.lowerBead(4)
    prob2 = problemGen.lowerBead(4)

    ui.settingInts1(prob1.problemSteps)
    ui.settingInts2(prob2.problemSteps)

    MainWindow.show()
    sys.exit(app.exec_())
