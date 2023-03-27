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
from scheduleGUI import MainWindow2
import data_structures as dataStruct
from algorithm import *
from cohorts import *
from request_rooms import *
import settingText as setText
from courses import *


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def openScheduleBuilder(self):
        self.window = QMainWindow()
        self.ui = MainWindow2(self.window)
        self.window.show()

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
        #self.pixmap = QPixmap(getcwd() + "\\macewan1.png")
        self.pixmap = QPixmap("macewan1.png")
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.label.move(797,0)

        self.label2 = QLabel(self)
        self.pixmap = QPixmap("macewanlogo.png")
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

        '''making the edit course button'''
        self.aCourse = QPushButton("Edit Courses", self)
        self.aCourse.setGeometry(280,700,150,25)
        self.aCourse.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.aCourse.clicked.connect(self.editCourse)

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



    '''this uplaods excel file and extracts what is needed from it'''
    def clicked(self):
        #closing scrren so other new screen can open
        self.close()

        #code will change here to account for students
        self.data = pd.read_excel('test file.xlsx', sheet_name='Sheet1')
        self.df = pd.DataFrame(self.data, columns=['Numbers'])
        self.dfList = self.df.values.tolist()


        #code for room list
        self.data1 = pd.read_excel('test file.xlsx', sheet_name='Sheet2')
        self.room = pd.DataFrame(self.data1, columns=['Room Number', 'Lab (Y/N)','Capacity'])
        self.roomList = self.room.values.tolist()
        #print(self.roomList)

        self.globalRoomList = []

        #showing new screens
        self.UiComponents2()
        self.show()
        #print ("ughyt")

    '''Warning that rooms entered are not enough'''
    def warning(self, rooms):
        msg = QMessageBox()
        msg.setWindowTitle("Capacity Reached")
        text = "Additional rooms may be required:\n\n"
        for room in rooms:
            text += room + "\n"
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()



    '''add/edit courses'''
    def editCourse(self):
        self.w = AnotherWindow()
        self.w.show()


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
        #print ("numbers of students per program",self.listText)

        settingText.make_room_object(self.roomList,self.globalRoomList)
        settingText.make_cohort(self.listText)
        rooms = request_room(settingText.cohorts, self.globalRoomList)
        if len(rooms) != 0:
            self.warning(rooms)
        #print("clicked")
        self.close()
        #self.openScheduleBuilder()


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        '''making the courses window'''
        self.acceptDrops()
        self.setWindowTitle("Courses")
        self.setGeometry(0, 0, 900, 600) # x,y,w,h
        self.setFixedSize(QSize(900, 600)) # w,h
        self.setStyleSheet("background-color: whitesmoke")
        self.table_widget = MyTableWidget(self)
        self.show()

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        #self.layout = QVBoxLayout(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        #submit button
        self.Submit2 = QPushButton("Add Course")
        self.Submit2.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.Submit2.clicked.connect(self.addCourse)
        
        self.Label = QLabel("ADD COURSES")
        self.Label.setFont(QFont('Arial',12))
        self.Label.setStyleSheet("color: #902a39; font-weight: bold")
        self.Label.setAlignment(QtCore.Qt.AlignRight)

        #choose term
        self.Label1 = QLabel("Choose Term:")
        self.Label1.setFont(QFont('Arial',10))
        self.Label1.setStyleSheet("color: #902a39;")
        self.Label1.setAlignment(QtCore.Qt.AlignRight)

        self.listofTerms = ["PCOM_TERM_1", "PCOM_TERM_2", "PCOM_TERM_3", "BCOM_TERM_1", "BCOM_TERM_2",
                     "BCOM_TERM_3", "FS_TERM_1", "FS_TERM_2", "FS_TERM_3", "DXDI_TERM_1", "DXDI_TERM_2",
                     "DXDI_TERM_3", "BK_TERM_1", "BK_TERM_2", "BK_TERM_3", "GL_TERM_1", "GL_TERM_2", 
                     "GL_TERM_3", "BA_TERM_1", "BA_TERM_2", "BA_TERM_3", "PM_TERM_1", "PM_TERM_2",
                     "PM_TERM_3"]
        self.termsList = QComboBox(self)
        self.termsList.move(275,250)
        self.termsList.resize(190,35)
        #self.termsList.setStyleSheet("color: #902a39;")
        for term in self.listofTerms:
              self.termsList.addItem(term)
        
        #enter Course Name to add
        self.Label11 = QLabel("Enter Course Name(eg. CMSK_0101):")
        self.Label1.resize(260,25)
        self.Label11.setFont(QFont('Arial',10))
        self.Label11.setStyleSheet("color: #902a39;")
        self.Label11.setAlignment(QtCore.Qt.AlignRight)
        self.addCourseName = QLineEdit()
        self.addCourseName.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")

        #enter hours
        self.Label12 = QLabel("Enter Hours:")
        self.Label12.setFont(QFont('Arial',10))
        self.Label12.setStyleSheet("color: #902a39;")
        self.Label12.setAlignment(QtCore.Qt.AlignRight)


        self.addHours = QLineEdit()
        self.addHours.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")
        
        #enter lab
        self.Label13 = QLabel("Is it a Lab? (YES/NO)")
        self.Label13.setFont(QFont('Arial',10))
        self.Label13.setStyleSheet("color: #902a39;")
        self.Label13.setAlignment(QtCore.Qt.AlignRight)

        self.addLab = QLineEdit()
        self.addLab.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")

        self.layout.addWidget(self.Label, 0,0)
        self.layout.addWidget(self.Label1, 1,0)
        self.layout.addWidget(self.termsList,1,1)
        self.layout.addWidget(self.Label11, 1,2)
        self.layout.addWidget(self.addCourseName, 1,3)
        self.layout.addWidget(self.Label12, 2,0)
        self.layout.addWidget(self.addHours, 2,1)
        self.layout.addWidget(self.Label13, 2,2)
        self.layout.addWidget(self.addLab, 2,3)
        self.layout.addWidget(self.Submit2, 3,3)

        '''
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Add Course")
        self.tabs.addTab(self.tab2,"Edit Course")
        self.tabs.addTab(self.tab3,"Remove Course")

        # Create first tab
        self.tab1.layout = QHBoxLayout(self)
        self.Label1 = QLabel("Choose Term:",self)
        self.Label1.setFont(QFont('Arial',8))
        self.Label1.setStyleSheet("color: #902a39;")
        self.Label1.setAlignment(QtCore.Qt.AlignRight)

        self.Label11 = QLabel("Enter Course Name (eg. CMSK_0101):",self)
        #self.Label1.resize(260,25)
        self.Label11.setFont(QFont('Arial',8))
        self.Label11.setStyleSheet("color: #902a39;")
        self.Label11.setAlignment(QtCore.Qt.AlignRight)

        self.Label12 = QLabel("Enter Hours:",self)
        #self.Label2.resize(260,25)
        self.Label12.setFont(QFont('Arial',8))
        self.Label12.setStyleSheet("color: #902a39;")
        self.Label12.setAlignment(QtCore.Qt.AlignRight)

        self.Label13 = QLabel("Is it a Lab? (YES/NO)",self)
        #self.Label3.resize(260,25)
        self.Label13.setFont(QFont('Arial',8))
        self.Label13.setStyleSheet("color: #902a39;")
        self.Label13.setAlignment(QtCore.Qt.AlignRight)


        self.listofTerms = ["PCOM_TERM_1", "PCOM_TERM_2", "PCOM_TERM_3", "BCOM_TERM_1", "BCOM_TERM_2",
                     "BCOM_TERM_3", "FS_TERM_1", "FS_TERM_2", "FS_TERM_3", "DXDI_TERM_1", "DXDI_TERM_2",
                     "DXDI_TERM_3", "BK_TERM_1", "BK_TERM_2", "BK_TERM_3", "GL_TERM_1", "GL_TERM_2", 
                     "GL_TERM_3", "BA_TERM_1", "BA_TERM_2", "BA_TERM_3", "PM_TERM_1", "PM_TERM_2",
                     "PM_TERM_3"]
        self.termsList = QComboBox(self)
        self.termsList.move(275,250)
        self.termsList.resize(190,35)
        #self.termsList.setStyleSheet("color: #902a39;")
        for term in self.listofTerms:
              self.termsList.addItem(term)

        self.addCourseName = QLineEdit(self)
        self.addCourseName.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")
        
        self.addHours = QLineEdit(self)
        self.addHours.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")

        self.addLab = QLineEdit(self)
        self.addLab.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")
        

        #adding to second tab (edit courses)
        self.tab2.layout = QHBoxLayout(self)
        self.Label2 = QLabel("Choose Term:",self)
        self.Label2.setFont(QFont('Arial',9))
        self.Label2.setStyleSheet("color: #902a39;")
        self.Label2.setAlignment(QtCore.Qt.AlignRight)
        
        self.termsList2 = QComboBox(self)
        self.termsList2.move(275,250)
        self.termsList2.resize(190,35)
        #self.termsList.setStyleSheet("color: #902a39;")
        for term in self.listofTerms:
              self.termsList2.addItem(term)
        
        self.Label21 = QLabel("Enter Old Course Name (eg. CMSK_0101):",self)
        self.Label21.setFont(QFont('Arial',8))
        self.Label21.setStyleSheet("color: #902a39;")
        self.Label21.setAlignment(QtCore.Qt.AlignRight)

        self.Label24 = QLabel("Enter New Course Name (eg. CMSK_0101):",self)
        self.Label24.setFont(QFont('Arial',8))
        self.Label24.setStyleSheet("color: #902a39;")
        self.Label24.setAlignment(QtCore.Qt.AlignRight)

        self.Label22 = QLabel("Enter Hours:",self)
        self.Label22.setFont(QFont('Arial',9))
        self.Label22.setStyleSheet("color: #902a39;")
        self.Label22.setAlignment(QtCore.Qt.AlignRight)

        self.Label23 = QLabel("Is it a Lab? (YES/NO)",self)
        self.Label23.setFont(QFont('Arial',8))
        self.Label23.setStyleSheet("color: #902a39;")
        self.Label23.setAlignment(QtCore.Qt.AlignRight)

        self.addOldCourseName = QLineEdit(self)
        self.addOldCourseName.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")
        
        self.addNewCourseName = QLineEdit(self)
        self.addNewCourseName.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")
        
        self.addHours2 = QLineEdit(self)
        self.addHours2.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")

        self.addLab2 = QLineEdit(self)
        self.addLab2.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")
        
        #making third tab(remove course)
        self.tab3.layout = QHBoxLayout(self)
        #self.tab3.layout = QGridLayout(self)
        #self.tab3.layout.addWidget(QLabel("Choose Program",self), 1, 1)
        self.Label3 = QLabel("Choose Program",self)
        self.Label3.setFont(QFont('Arial',8))
        self.Label3.setStyleSheet("color: #902a39;")
        self.Label3.setAlignment(QtCore.Qt.AlignRight)

        
        self.listofProgram = ["PCOM","BCOM", "FS", "DXDI", "BK", "GL", "BA", "PM"]
        self.programList = QComboBox(self)
        self.programList.move(275,250)
        self.programList.resize(190,35)
        #self.termsList.setStyleSheet("color: #902a39;")
        for program in self.listofProgram:
              self.programList.addItem(program)
        
        self.Label31 = QLabel("Enter Course Name To Remove (eg. CMSK_0101)",self)
        self.Label31.setFont(QFont('Arial',8))
        self.Label31.setStyleSheet("color: #902a39;")
        self.Label31.setAlignment(QtCore.Qt.AlignRight)

        self.removeCourse3 = QLineEdit(self)
        self.removeCourse3.setStyleSheet("border: 2px solid;"
                    "border-top-color : black; "
                     "border-left-color :black;"
                     "border-right-color :black;"
                     "border-bottom-color : black")

        #adding to tabs
        self.tab1.layout.addWidget(self.Label1)
        self.tab1.layout.addWidget(self.termsList)
        self.tab1.layout.addWidget(self.Label11)
        self.tab1.layout.addWidget(self.addCourseName)
        self.tab1.layout.addWidget(self.Label12)
        self.tab1.layout.addWidget(self.addHours)
        self.tab1.layout.addWidget(self.Label13)
        self.tab1.layout.addWidget(self.addLab)


        self.tab2.layout.addWidget(self.Label2)
        self.tab2.layout.addWidget(self.termsList2)
        self.tab2.layout.addWidget(self.Label21)
        self.tab2.layout.addWidget(self.addOldCourseName)
        self.tab2.layout.addWidget(self.Label24)
        self.tab2.layout.addWidget(self.addNewCourseName)
        self.tab2.layout.addWidget(self.Label22)
        self.tab2.layout.addWidget(self.addHours2)
        self.tab2.layout.addWidget(self.Label23)
        self.tab2.layout.addWidget(self.addLab2)

        #self.tab3.layout.addWidget(self.Label3)
        #self.tab3.layout.addWidget(self.programList)
        #self.tab3.layout.addWidget(self.Label31)
        #self.tab3.layout.addWidget(self.removeCourse3)

        #Shows things on tab
        self.tab1.setLayout(self.tab1.layout)
        self.tab2.setLayout(self.tab2.layout)
        self.tab3.setLayout(self.tab3.layout)'''

        # Add tabs to widget
        #self.layout.addWidget(self.tabs)
        #self.layout.addWidget(self.Submit2)
        #self.setLayout(self.layout)

        #self.show()

    #def addCourse(self):
        #addCourse(self.programListValue, self.courseNameValue, self.hoursValue, self.labValue)


'''
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    #start the event loop
    App.exec()
'''
