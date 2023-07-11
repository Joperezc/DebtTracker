
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from debtItm import debtItm
from inputPop import Ui_Form as inputPop
from DataSource import DataSource
from payPopup import Ui_Form as payPop
from listPop import Ui_Form as listPop

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 541)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(100, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -79, 2018, 2018))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #self.debt1 = debtItm()
    
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # sizePolicy.setHeightForWidth(self.debt1.sizePolicy().hasHeightForWidth())
        # self.debt1.setSizePolicy(sizePolicy)
        # self.debt1.setMinimumSize(QtCore.QSize(1200, 300))
        # self.debt1.setObjectName("debt1")
        # self.verticalLayout_2.addWidget(self.debt1)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(lambda: self.addDebtDialog())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuNew.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuNew.menuAction())
        self.source = DataSource()
        self.loadDebts()
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionNew.setText(_translate("MainWindow", "New Entry"))

    def addDebtDialog(self):

        self.window = QtWidgets.QDialog()
        self.ui = inputPop()
        self.ui.setupUi(self.window)
        self.window.exec_()
        if(self.ui.name == "" and self.ui.total == "" and self.ui.monthPay == 0 and self.ui.interest == "" and self.ui.textDate == ""):
            return
        try:
            int(self.ui.total)
        except:
            print("string instead of num")
            return
        try:
            int(self.ui.monthPay)
        except:
            print("string instead of num")
            return
        try:
            int(self.ui.interest)
        except:
            print("string instead of num")
            return

        self.addDebtWidget(self.ui.name, self.ui.total, self.ui.monthPay, self.ui.interest, self.ui.textDate, False)
        
        
    def addDebtWidget(self, name, total, monthlyPay, interest, date, load):
        debt1 = debtItm()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(debt1.sizePolicy().hasHeightForWidth())
        debt1.setSizePolicy(sizePolicy)
        debt1.setMinimumSize(QtCore.QSize(1300, 300))
        debt1.setObjectName("debt1")
        debt1.nameLab.setText(name)
        debt1.valueDue.setText(total)
        debt1.Percentage.setText(interest)
        debt1.Date.setText(date)
        debt1.monthlyValueDue.setText(monthlyPay)
        self.verticalLayout_2.setAlignment(Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(debt1)
        dateSplit = date.split("/")
        qtDate = QtCore.QDate(int(dateSplit[2]), int(dateSplit[0]), int(dateSplit[1]))
        debt1.calendarWidget.setStyleSheet("background-color: red")
        debt1.calendarWidget.setSelectedDate(qtDate)
        debt1.pushButton.clicked.connect(lambda: self.payClick(debt1))
        debt1.pushButton2.clicked.connect(lambda: self.deleteDebt(debt1.nameLab.text()))
        debt1.pushButton3.clicked.connect(lambda: self.showPayments(debt1.nameLab.text()))
        if(load):
            pass
        else:
            self.source.saveDebt(name, total, monthlyPay, interest, date)
        
    def showPayments(self, name):
        self.window = QtWidgets.QDialog()
        self.ui = listPop()
        self.ui.setupUi(self.window)
        retList = self.source.grabPayments(name)
        for i in retList:
            self.ui.populateList(i, self.window)
        self.window.exec_()


    def loadDebts(self):
        debts = self.source.loadDebts()
        for i in debts:
            self.addDebtWidget(i[0], i[1], i[2], i[3], i[4], True)
    
    def payClick(self, debt):
        self.window = QtWidgets.QDialog()
        self.ui = payPop()
        self.ui.setupUi(self.window)
        self.window.exec_()
        debt.valueDue.setText(str(int(debt.valueDue.text()) - int(self.ui.amountPaid)))
        if(int(self.ui.amountPaid) >= int(debt.valueDue.text())):
            self.deleteDebt(debt.nameLab.text())
        if(int(self.ui.amountPaid) < int(debt.monthlyValueDue.text())):
            debt.monthlyValueDue.setText(str(int(debt.monthlyValueDue.text()) - int(self.ui.amountPaid)))
        else:
            debt.monthlyValueDue.setText("0")
        if(int(self.ui.amountPaid) < int(debt.monthlyValueDue.text())):
            self.source.makePartialPayment(debt.nameLab.text(), str(int(debt.valueDue.text()) - int(self.ui.amountPaid)), str(int(debt.monthlyValueDue.text()) - int(self.ui.amountPaid)), self.ui.amountPaid)
        elif((int(self.ui.amountPaid) - int(debt.monthlyValueDue.text())) < 0):
            self.source.makePayment(debt.nameLab.text(), str(int(debt.valueDue.text()) - int(self.ui.amountPaid)), self.ui.amountPaid)
        else:
            self.source.makePayment(debt.nameLab.text(), str(int(debt.valueDue.text()) - int(self.ui.amountPaid)), self.ui.amountPaid)
    
    def deleteDebt(self, debt):
        self.source.deleteDebt(debt)
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        self.loadDebts()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
