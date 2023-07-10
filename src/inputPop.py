
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):

    name = ""
    total = ""
    monthPay = 0
    interest = ""
    textDate = ""
    qt5Date = ""
    state = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 347)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(180, 10, 211, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 60, 211, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 110, 211, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(180, 160, 211, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QDateEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(180, 210, 211, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 270, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.onClick(Form))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nombre de Deuda"))
        self.label_2.setText(_translate("Form", "Cantidad"))
        self.label_3.setText(_translate("Form", "Pago Mensual"))
        self.label_4.setText(_translate("Form", "Interes"))
        self.label_5.setText(_translate("Form", "Fecha de Pago"))
        self.pushButton.setText(_translate("Form", "OK"))

    def onClick(self, Form):
        self.name = self.textEdit.toPlainText()
        self.total = self.textEdit_2.toPlainText()
        self.monthPay = self.textEdit_3.toPlainText()
        self.interest = self.textEdit_4.toPlainText()
        self.qt5Date = self.textEdit_5.date()
        self.textDate = self.qt5Date.toString("MM/dd/yyyy")
        self.state = 1
        Form.close()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
