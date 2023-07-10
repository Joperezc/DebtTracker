
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    amountPaid = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 192)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 70, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(190, 70, 104, 21))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 110, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.paySubmit(Form))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cuanto Desea Pagar: "))
        self.pushButton.setText(_translate("Form", "Pagar"))
    
    def paySubmit(self, Form):
        self.amountPaid = self.textEdit.toPlainText()
        Form.close()
