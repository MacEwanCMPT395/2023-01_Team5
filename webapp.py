#import PyQt5 as qtw
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from request_rooms import *
from os import *
import settingText
import pandas as pd


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        '''making the schedule builder window'''
        self.acceptDrops()
        self.setWindowTitle("Schedule Builder")
        self.setGeometry(0, 0, 1900, 734) # x,y,w,h
        self.setFixedSize(QSize(1900, 734)) # w,h
        self.setStyleSheet("background-color: whitesmoke")

        ''' putting the pictures in place'''
        self.label = QLabel(self)
        self.pixmap = QPixmap(getcwd() + "\\macewan1.png")
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.label.move(797,0)

        self.label2 = QLabel(self)
        self.pixmap = QPixmap(getcwd() + "\\macewanlogo.png")
        self.label2.setPixmap(self.pixmap)
        self.label2.resize(self.pixmap.width(), self.pixmap.height())
        self.label2.move(10,0)

        '''putting all the labels in place'''
        self.pmLabel = QLabel("Project Management (PM):",self)
        self.pmLabel.move(7,200)
        self.pmLabel.resize(260,25)
        self.pmLabel.setFont(QFont('Arial',10))
        #self.pmLabel.setStyleSheet("border: 1px solid black")
        self.pmLabel.setAlignment(QtCore.Qt.AlignRight)

        self.baLabel = QLabel("Business Analysis (BA):",self)
        self.baLabel.move(7,250)
        self.baLabel.resize(260,25)
        self.baLabel.setFont(QFont('Arial',10))
        self.baLabel.setAlignment(QtCore.Qt.AlignRight)

        self.glmLabel = QLabel("Supply Chain Managment and",self)
        self.glmLabel.move(7,300)
        self.glmLabel.resize(260,25)
        self.glmLabel.setFont(QFont('Arial',10))
        self.glmLabel.setAlignment(QtCore.Qt.AlignRight)
        self.glmLabel2 = QLabel("Logistics (GLM):",self)
        self.glmLabel2.move(7,325)
        self.glmLabel2.resize(260,25)
        self.glmLabel2.setFont(QFont('Arial',10))
        self.glmLabel2.setAlignment(QtCore.Qt.AlignRight)

        self.fsLabel = QLabel("Full Stack Web Development:",self)
        self.fsLabel.move(7,375)
        self.fsLabel.resize(260,25)
        self.fsLabel.setFont(QFont('Arial',10))
        self.fsLabel.setAlignment(QtCore.Qt.AlignRight)
        self.fsLabel1 = QLabel("(FS)",self)
        self.fsLabel1.move(7,400)
        self.fsLabel1.resize(260,25)
        self.fsLabel1.setFont(QFont('Arial',10))
        self.fsLabel1.setAlignment(QtCore.Qt.AlignRight)

        self.dxdLabel = QLabel("Digital Experience Design",self)
        self.dxdLabel.move(7,450)
        self.dxdLabel.resize(260,25)
        self.dxdLabel.setFont(QFont('Arial',10))
        self.dxdLabel.setAlignment(QtCore.Qt.AlignRight)
        self.dxdLabel1 = QLabel("Foundation (DXD):",self)
        self.dxdLabel1.move(7,475)
        self.dxdLabel1.resize(260,25)
        self.dxdLabel1.setFont(QFont('Arial',10))
        self.dxdLabel1.setAlignment(QtCore.Qt.AlignRight)

        self.bookLabel = QLabel("Bookkeeping (BK):",self)
        self.bookLabel.move(7,525)
        self.bookLabel.resize(260,25)
        self.bookLabel.setFont(QFont('Arial',10))
        self.bookLabel.setAlignment(QtCore.Qt.AlignRight)

        self.pcomLabel = QLabel("Professional Communication:",self)
        self.pcomLabel.move(7,575)
        self.pcomLabel.resize(260,25)
        self.pcomLabel.setFont(QFont('Arial',10))
        self.pcomLabel.setAlignment(QtCore.Qt.AlignRight)
        self.pcomLabel1 = QLabel("(PCOM)",self)
        self.pcomLabel1.move(7,600)
        self.pcomLabel1.resize(260,25)
        self.pcomLabel1.setFont(QFont('Arial',10))
        self.pcomLabel1.setAlignment(QtCore.Qt.AlignRight)

        self.bcomLabel = QLabel("Business Communication:",self)
        self.bcomLabel.move(7,650)
        self.bcomLabel.resize(260,25)
        self.bcomLabel.setFont(QFont('Arial',10))
        self.bcomLabel.setAlignment(QtCore.Qt.AlignRight)
        self.bcomLabel1 = QLabel("(BCOM)",self)
        self.bcomLabel1.move(7,675)
        self.bcomLabel1.resize(260,25)
        self.bcomLabel1.setFont(QFont('Arial',10))
        self.bcomLabel1.setAlignment(QtCore.Qt.AlignRight)

        self.t1Label = QLabel("Term 1",self)
        self.t1Label.move(280,160)
        self.t1Label.resize(150,25)
        self.t1Label.setFont(QFont('Arial',10))
        self.t1Label.setStyleSheet("font-weight: bold")
        self.t1Label.setAlignment(QtCore.Qt.AlignCenter)

        self.t2Label = QLabel("Term 2",self)
        self.t2Label.move(440,160)
        self.t2Label.resize(150,25)
        self.t2Label.setFont(QFont('Arial',10))
        self.t2Label.setStyleSheet("font-weight: bold")
        self.t2Label.setAlignment(QtCore.Qt.AlignCenter)

        self.t3Label = QLabel("Term 3",self)
        self.t3Label.move(600,160)
        self.t3Label.resize(150,25)
        self.t3Label.setFont(QFont('Arial',10))
        self.t3Label.setStyleSheet("font-weight: bold")
        self.t3Label.setAlignment(QtCore.Qt.AlignCenter)

        '''making the initial boxes with a value of zero'''
        self.UiComponents()

        '''making the submit button'''
        self.submit = QPushButton("SUBMIT", self)
        self.submit.setGeometry(600,700,150,25)
        self.submit.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.submit.clicked.connect(self.clickSubmit)

        '''making the upload button'''
        self.upload = QPushButton("Upload Excel File ", self)
        self.upload.setGeometry(440,700,150,25)
        self.upload.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.upload.clicked.connect(self.clicked)

        '''showing the initial screen'''
        self.show()

    def UiComponents(self):
        '''this one is used for the initial boxes'''
        self.pm1 = QLineEdit('0',self)
        self.pm1.setGeometry(280,203,150,25)
        self.pm1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pm2 = QLineEdit('0',self)
        self.pm2.setGeometry(440,203,150,25)
        self.pm2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pm3 = QLineEdit('0',self)
        self.pm3.setGeometry(600,203,150,25)
        self.pm3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.ba1 = QLineEdit('0',self)
        self.ba1.setGeometry(280,253,150,25)
        self.ba1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.ba2 = QLineEdit('0',self)
        self.ba2.setGeometry(440,253,150,25)
        self.ba2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.ba3 = QLineEdit('0',self)
        self.ba3.setGeometry(600,253,150,25)
        self.ba3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.glm1 = QLineEdit('0',self)
        self.glm1.setGeometry(280,303,150,25)
        self.glm1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.glm2 = QLineEdit('0',self)
        self.glm2.setGeometry(440,303,150,25)
        self.glm2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.glm3 = QLineEdit('0',self)
        self.glm3.setGeometry(600,303,150,25)
        self.glm3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.fs1 = QLineEdit('0',self)
        self.fs1.setGeometry(280,377,150,25)
        self.fs1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.fs2 = QLineEdit('0',self)
        self.fs2.setGeometry(440,377,150,25)
        self.fs2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.fs3 = QLineEdit('0',self)
        self.fs3.setGeometry(600,377,150,25)
        self.fs3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.dxd1 = QLineEdit('0',self)
        self.dxd1.setGeometry(280,453,150,25)
        self.dxd1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.dxd2 = QLineEdit('0',self)
        self.dxd2.setGeometry(440,453,150,25)
        self.dxd2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.dxd3 = QLineEdit('0',self)
        self.dxd3.setGeometry(600,453,150,25)
        self.dxd3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bk1 = QLineEdit('0',self)
        self.bk1.setGeometry(280,527,150,25)
        self.bk1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bk2 = QLineEdit('0',self)
        self.bk2.setGeometry(440,527,150,25)
        self.bk2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bk3 = QLineEdit('0',self)
        self.bk3.setGeometry(600,527,150,25)
        self.bk3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pcom1 = QLineEdit('0',self)
        self.pcom1.setGeometry(280,577,150,25)
        self.pcom1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pcom2 = QLineEdit('0',self)
        self.pcom2.setGeometry(440,577,150,25)
        self.pcom2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pcom3 = QLineEdit('0',self)
        self.pcom3.setGeometry(600,577,150,25)
        self.pcom3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bcom1 = QLineEdit('0',self)
        self.bcom1.setGeometry(280,653,150,25)
        self.bcom1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bcom2 = QLineEdit('0',self)
        self.bcom2.setGeometry(440,653,150,25)
        self.bcom2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bcom3 = QLineEdit('0',self)
        self.bcom3.setGeometry(600,653,150,25)
        self.bcom3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")




    def UiComponents2(self):
        '''This one is used after the excel button is pressed'''
        self.pm1 = QLineEdit(str(self.dfList[0][0]),self)
        self.pm1.setGeometry(280,203,150,25)
        self.pm1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pm2 = QLineEdit(str(self.dfList[1][0]),self)
        self.pm2.setGeometry(440,203,150,25)
        self.pm2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pm3 = QLineEdit(str(self.dfList[2][0]),self)
        self.pm3.setGeometry(600,203,150,25)
        self.pm3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.ba1 = QLineEdit(str(self.dfList[3][0]),self)
        self.ba1.setGeometry(280,253,150,25)
        self.ba1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.ba2 = QLineEdit(str(self.dfList[4][0]),self)
        self.ba2.setGeometry(440,253,150,25)
        self.ba2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.ba3 = QLineEdit(str(self.dfList[5][0]),self)
        self.ba3.setGeometry(600,253,150,25)
        self.ba3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.glm1 = QLineEdit(str(self.dfList[6][0]),self)
        self.glm1.setGeometry(280,303,150,25)
        self.glm1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.glm2 = QLineEdit(str(self.dfList[7][0]),self)
        self.glm2.setGeometry(440,303,150,25)
        self.glm2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.glm3 = QLineEdit(str(self.dfList[8][0]),self)
        self.glm3.setGeometry(600,303,150,25)
        self.glm3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.fs1 = QLineEdit(str(self.dfList[9][0]),self)
        self.fs1.setGeometry(280,377,150,25)
        self.fs1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.fs2 = QLineEdit(str(self.dfList[10][0]),self)
        self.fs2.setGeometry(440,377,150,25)
        self.fs2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.fs3 = QLineEdit(str(self.dfList[11][0]),self)
        self.fs3.setGeometry(600,377,150,25)
        self.fs3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.dxd1 = QLineEdit(str(self.dfList[12][0]),self)
        self.dxd1.setGeometry(280,453,150,25)
        self.dxd1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.dxd2 = QLineEdit(str(self.dfList[13][0]),self)
        self.dxd2.setGeometry(440,453,150,25)
        self.dxd2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.dxd3 = QLineEdit(str(self.dfList[14][0]),self)
        self.dxd3.setGeometry(600,453,150,25)
        self.dxd3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bk1 = QLineEdit(str(self.dfList[15][0]),self)
        self.bk1.setGeometry(280,527,150,25)
        self.bk1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bk2 = QLineEdit(str(self.dfList[16][0]),self)
        self.bk2.setGeometry(440,527,150,25)
        self.bk2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bk3 = QLineEdit(str(self.dfList[17][0]),self)
        self.bk3.setGeometry(600,527,150,25)
        self.bk3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pcom1 = QLineEdit(str(self.dfList[18][0]),self)
        self.pcom1.setGeometry(280,577,150,25)
        self.pcom1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pcom2 = QLineEdit(str(self.dfList[19][0]),self)
        self.pcom2.setGeometry(440,577,150,25)
        self.pcom2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.pcom3 = QLineEdit(str(self.dfList[20][0]),self)
        self.pcom3.setGeometry(600,577,150,25)
        self.pcom3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bcom1 = QLineEdit(str(self.dfList[21][0]),self)
        self.bcom1.setGeometry(280,653,150,25)
        self.bcom1.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bcom2 = QLineEdit(str(self.dfList[22][0]),self)
        self.bcom2.setGeometry(440,653,150,25)
        self.bcom2.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

        self.bcom3 = QLineEdit(str(self.dfList[23][0]),self)
        self.bcom3.setGeometry(600,653,150,25)
        self.bcom3.setStyleSheet("border: 2px solid;"
                    "border-top-color : #902a39; "
                     "border-left-color :#902a39;"
                     "border-right-color :#902a39;"
                     "border-bottom-color : #902a39")

    def clicked(self):
        '''this uplaods excel file and extracts what is needed from it'''
        self.close()
        self.data = pd.read_excel('C:\\Users\\ayesh\\Documents\\University\\cmpt 395\\test\\2023-01_Team5-Schedule-System-\\test file.xlsx')
        self.df = pd.DataFrame(self.data, columns=['Numbers'])
        self.dfList = self.df.values.tolist()
        self.UiComponents2()
        self.show()
        #print ("ughyt")

    def warning(self, rooms):
        msg = QMessageBox()
        msg.setWindowTitle("Capacity Reached")
        text = "Additional rooms may be required:\n\n"
        for room in rooms:
            text += room + "\n"
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def clickSubmit(self):
        '''this makes it into a list so that can be transferred'''
        self.listText = []
        '''this is converting them into text'''
        text1 = self.pm1.text()
        text2 = self.pm2.text()
        text3 = self.pm3.text()
        text4 = self.ba1.text()
        text5 = self.ba2.text()
        text6 = self.ba3.text()
        text7 = self.glm1.text()
        text8 = self.glm2.text()
        text9 = self.glm3.text()
        text10 = self.fs1.text()
        text11 = self.fs2.text()
        text12 = self.fs3.text()
        text13 = self.dxd1.text()
        text14 = self.dxd2.text()
        text15 = self.dxd3.text()
        text16 = self.bk1.text()
        text17 = self.bk2.text()
        text18 = self.bk3.text()
        text19 = self.pcom1.text()
        text20 = self.pcom2.text()
        text21 = self.pcom3.text()
        text22 = self.bcom1.text()
        text23 = self.bcom2.text()
        text24 = self.bcom3.text()

        '''appending them into the list'''
        self.listText.append(int(text1))
        self.listText.append(int(text2))
        self.listText.append(int(text3))
        self.listText.append(int(text4))
        self.listText.append(int(text5))
        self.listText.append(int(text6))
        self.listText.append(int(text7))
        self.listText.append(int(text8))
        self.listText.append(int(text9))
        self.listText.append(int(text10))
        self.listText.append(int(text11))
        self.listText.append(int(text12))
        self.listText.append(int(text13))
        self.listText.append(int(text14))
        self.listText.append(int(text15))
        self.listText.append(int(text16))
        self.listText.append(int(text17))
        self.listText.append(int(text18))
        self.listText.append(int(text19))
        self.listText.append(int(text20))
        self.listText.append(int(text21))
        self.listText.append(int(text22))
        self.listText.append(int(text23))
        self.listText.append(int(text24))
        print ("numbers of students per program",self.listText)

        settingText.make_cohort(self.listText)
        rooms = request_room(settingText.cohorts)
        if len(rooms) != 0:
            self.warning(rooms)
        #print("clicked")
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    #start the event loop
    App.exec()
