from PyQt5 import QtCore, QtGui, QtWidgets
import problemGen

class Prob1Pane(QtWidgets.QWidget):
    def __init__(self, Parent):
        QtWidgets.QWidget.__init__(self)
        self.MainWin = Parent

        PrbHdrFont = QtGui.QFont()
        PrbHdrFont.setFamily("Bradley Hand")
        PrbHdrFont.setPointSize(32)
        PrbHdrFont.setBold(True)

        #Generated Problem
        self.currentStep = 0
        self.steps = 4
        self.LowerBead = problemGen.lowerBead(self.steps)
        
        self.problemCycle = QtWidgets.QStackedLayout()

        self.setupProblem()
        
        self.setLayout(self.problemCycle)

    def setupProblem(self): 
        for i in range(0, self.steps):

            self.tempWidget = QtWidgets.QWidget()
        
            #Template Widget
            #Label for step
            self.label = QtWidgets.QLabel(self.tempWidget)
            self.label.setGeometry(QtCore.QRect(250, 210, 301, 131))
            self.label.setAlignment(QtCore.Qt.AlignCenter)

            if(i == 0):
                self.label.setText(str(self.LowerBead.problemSteps[i]))
            else:
                self.label.setText(str(self.LowerBead.problemSteps[i*2]))

            #Next button
            self.pushButton = QtWidgets.QPushButton(self.tempWidget)
            self.pushButton.setGeometry(QtCore.QRect(320, 360, 161, 51))

            if(i != self.steps):
                self.pushButton.setText("Next Step!")
                self.problemCycle.addWidget(self.tempWidget)
                self.pushButton.clicked.connect(self.toNextStep)
            else:
                pass
        
        #Final Template Widgit
        self.pushButton.setText("Check Answer")
        self.lineEdit = QtWidgets.QLineEdit(self.tempWidget)
        self.lineEdit.setGeometry(QtCore.QRect(325, 340, 151, 21))

        self.pushButton_2 = QtWidgets.QPushButton(self.tempWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 480, 161, 51))
        self.pushButton_2.setText("Start From Beginning")
        self.pushButton_3 = QtWidgets.QPushButton(self.tempWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 530, 161, 51))
        self.pushButton_3.setText("Main Menu")

        self.problemCycle.addWidget(self.tempWidget)

        self.pushButton.clicked.connect(self.checkAnswer)
        self.pushButton_2.clicked.connect(self.restartProblem)
        self.pushButton_3.clicked.connect(self.SetToMainPane)

    def checkAnswer(self):
        try:
            finalAns = self.lineEdit.text()
            if (int(finalAns) == sum(self.LowerBead.finalAnswer)):
                QtWidgets.QMessageBox.question(self, 'Answer', "Correct!", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.question(self, 'Answer', "Try Again!", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        except ValueError:
            QtWidgets.QMessageBox.question(self, 'Error', "The answer needs to be a number!", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        
    def toNextStep(self):
        self.currentStep += 1
        print("Step: ", self.currentStep)
        self.problemCycle.setCurrentIndex(self.currentStep)
    
    def restartProblem(self):
        self.currentStep = 0
        self.problemCycle.setCurrentIndex(0)

    def SetToMainPane(self):
        self.MainWin.SetThePane(2)

class MainPane(QtWidgets.QWidget):
    def __init__(self, Parent):
        QtWidgets.QWidget.__init__(self)
        self.MainWin = Parent

        MnMnuFont = QtGui.QFont()
        MnMnuFont.setFamily("Bradley Hand")
        MnMnuFont.setPointSize(64)
        MnMnuFont.setBold(True)
#        MnMnuFont.setWeight(75)

        #Main Menu label
        self.lblHeader = QtWidgets.QLabel("Main Menu")
        self.lblHeader.setFont(MnMnuFont)

        HBox1 = QtWidgets.QHBoxLayout()
        HBox1.addStretch(1)
        HBox1.addWidget(self.lblHeader)
        HBox1.addStretch(1)

        ColHdrFont = QtGui.QFont()
        ColHdrFont.setFamily("Bradley Hand")
        ColHdrFont.setPointSize(12)
        ColHdrFont.setBold(True)

        #Create Label for first column
        self.lblColHdr = QtWidgets.QLabel("Technique")
        self.lblColHdr.setFont(ColHdrFont)

        HBox2 = QtWidgets.QHBoxLayout()
        HBox2.addWidget(self.lblColHdr)
        HBox2.addStretch(1)

        #Adding a list to 1st column 2nd row
        self.lswTechs = QtWidgets.QListWidget()
        self.lswTechs.addItem("Lower Beads")
        self.lswTechs.addItem("Mixed Beads")
        self.lswTechs.addItem("+5 Combinations")

        #Adding Button in 2nd column to start program
        self.btnStart = QtWidgets.QPushButton("Start!")
        self.btnStart.clicked.connect(self.SetToProbPane)

        HBox3 = QtWidgets.QHBoxLayout()
        HBox3.addStretch(1)
        HBox3.addWidget(self.btnStart)

        VBox = QtWidgets.QVBoxLayout()
        VBox.addLayout(HBox1)
        VBox.addLayout(HBox2)
        VBox.addWidget(self.lswTechs)
        VBox.addLayout(HBox3)

        self.setLayout(VBox)

    def SetToProbPane(self):
        if(self.lswTechs.currentRow() == 0):
            self.MainWin.SetToProblem()

class WelcomePane(QtWidgets.QWidget):
    def __init__(self, Parent):
        QtWidgets.QWidget.__init__(self)
        self.MainWin = Parent

        #Having welcome text
        self.lblWelcomeText = QtWidgets.QLabel('Welcome To Online Anzan!')

        #Button for entering portal
        self.btnEnter = QtWidgets.QPushButton("Let's do some math!")
        self.btnEnter.clicked.connect(self.SetToMainPane)
        
        HBox = QtWidgets.QHBoxLayout()
        HBox.addWidget(self.lblWelcomeText)
        HBox.addStretch(1)

        VBox = QtWidgets.QVBoxLayout()
        VBox.addLayout(HBox)
        VBox.addWidget(self.btnEnter)
        VBox.addStretch(1)
        
        #Adding Picture
        self.logo = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('LavaLrnPNG.png')
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)
        self.logo.setGeometry(QtCore.QRect(300,325,200,200))

        self.setLayout(VBox)


    def SetToMainPane(self):
        self.MainWin.SetThePane(2)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        #Left=200; 
        #Top=200; 
        Width=800 
        Hight=650
        self.resize(Width, Hight)

        self.NextStkId = 3
        self.StakPanes = {}
        self.StakPanes[1] = WelcomePane(self)
        self.StakPanes[2] = MainPane(self)

        self.CenterPane = self.StakPanes[1]
        self.setCentralWidget(self.CenterPane)

    def SetThePane(self, Id):
        print('Stack Id :',Id)
        if(Id == 2):
            self.CenterPane = MainPane(self)
        else:
            self.CenterPane = self.StakPanes[Id]
        self.setCentralWidget(self.CenterPane)

    
    def SetToProblem(self):
        print('Next Stack Id :',self.NextStkId)
        self.StakPanes[self.NextStkId] = Prob1Pane(self)
        self.SetThePane(self.NextStkId)
        self.NextStkId += 1
        
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    App = MainWindow()
    App.show()
    
    sys.exit(app.exec_())

       
    

