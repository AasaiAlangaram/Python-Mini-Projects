from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import sys
from datetime import date

class Message(QDialog):
    def __init__(self, parent=None):
        super(Message, self).__init__(parent)
        self.setWindowTitle("Days Calculator Application")
        # self.setStyleSheet("background-color: blue;")
        self.resize(800, 480)
        self.move(0, 0)
        self.init_UI()


    def init_UI(self):

        self.setWindowIcon(QtGui.QIcon("logo.jpg"))

        self.Datelabel = QLabel("Date1", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.Datelabel.setFont(setFnt)
        self.Datelabel.setFixedSize(300, 30)
        self.Datelabel.move(20, 10)

        self.monthlabel = QLabel("Month1", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.monthlabel.setFont(setFnt)
        self.monthlabel.setFixedSize(300, 30)
        self.monthlabel.move(100, 10)

        self.yearlabel = QLabel("Year1", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.yearlabel.setFont(setFnt)
        self.yearlabel.setFixedSize(300, 30)
        self.yearlabel.move(180, 10)

        self.Dateitem = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        self.Monthitem = ['1','2','3','4','5','6','7','8','9','10','11','12']
        self.yearitem = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
        
        self.Datetypecombo = QComboBox(self)
        for i in self.Dateitem:
            self.Datetypecombo.addItem(i)

        self.Datetypecombo.setFixedSize(60, 30)
        self.Datetypecombo.move(20, 40)

        self.monthtypecombo = QComboBox(self)
        for i in self.Monthitem:
            self.monthtypecombo.addItem(i)

        self.monthtypecombo.setFixedSize(60, 30)
        self.monthtypecombo.move(100, 40)

        self.yeartypecombo = QComboBox(self)
        for i in self.yearitem:
            self.yeartypecombo.addItem(i)

        self.yeartypecombo.setFixedSize(60, 30)
        self.yeartypecombo.move(180, 40)


        self.Datelabel1 = QLabel("Date2", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.Datelabel1.setFont(setFnt)
        self.Datelabel1.setFixedSize(300, 30)
        self.Datelabel1.move(360, 10)

        self.monthlabel1 = QLabel("Month2", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.monthlabel1.setFont(setFnt)
        self.monthlabel1.setFixedSize(300, 30)
        self.monthlabel1.move(440, 10)

        self.yearlabel1 = QLabel("Year2", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.yearlabel1.setFont(setFnt)
        self.yearlabel1.setFixedSize(300, 30)
        self.yearlabel1.move(520, 10)
        
        self.Datetypecombo1 = QComboBox(self)
        for i in self.Dateitem:
            self.Datetypecombo1.addItem(i)

        self.Datetypecombo1.setFixedSize(60, 30)
        self.Datetypecombo1.move(360, 40)

        self.monthtypecombo1 = QComboBox(self)
        for i in self.Monthitem:
            self.monthtypecombo1.addItem(i)

        self.monthtypecombo1.setFixedSize(60, 30)
        self.monthtypecombo1.move(440, 40)

        self.yeartypecombo1 = QComboBox(self)
        for i in self.yearitem:
            self.yeartypecombo1.addItem(i)

        self.yeartypecombo1.setFixedSize(60, 30)
        self.yeartypecombo1.move(520, 40)

        self.enter = QPushButton("Calculate", self)
        self.enter.clicked.connect(self.calculate_days)
        self.enter.setFixedSize(70, 40)
        self.enter.move(600, 30)

        self.clr = QPushButton("Clear", self)
        self.clr.clicked.connect(self.clear_days)
        self.clr.setFixedSize(70, 40)
        self.clr.move(690, 30)
        
        self.label = QLabel("Calculated Output", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(20, 100)

        self.out = QTextBrowser(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.out.setFont(setFnt)
        self.out.setFixedSize(100, 30)
        self.out.move(150, 100)

    def calculate_days(self):

        date1 = self.Datetypecombo.currentIndex()
        month1 = self.monthtypecombo.currentIndex()
        year1 = self.yeartypecombo.currentIndex()

        date2 = self.Datetypecombo1.currentIndex()
        month2 = self.monthtypecombo1.currentIndex()
        year2 = self.yeartypecombo1.currentIndex()

        print(date1+1,month1+1,year1+1990)
        print(date2+1,month2+1,year2+1990)

        year1,month1,date1 = year1+1990,month1+1,date1+1
        year2,month2,date2 = year2+1990,month2+1,date2+1
        
        fdate = date(year1,month1,date1)
        sdate = date(year2,month2,date2)
        bdays = (sdate - fdate).days
        print("No of days between two dates:",bdays)
        self.out.setText(str(bdays))
        self.out.setAlignment(QtCore.Qt.AlignCenter)
        self.out.setStyleSheet("color:blue;")

    def clear_days(self):
        self.out.clear()

#https://doc.qt.io/qt-5/qapplication.html#QApplication
app = QApplication(sys.argv)

win = Message()
win.show()

#https://stackoverflow.com/questions/25075954/using-sys-exit-with-app-exec-in-pyqt
sys.exit(app.exec_())
