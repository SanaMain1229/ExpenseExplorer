# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Programmer\Documents\Python UI Projects\Expense Explorer\AddExpense.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddData(object):
    def setupUi(self, AddData):
        AddData.setObjectName("AddData")
        AddData.resize(446, 277)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        AddData.setFont(font)
        self.frame = QtWidgets.QFrame(AddData)
        self.frame.setGeometry(QtCore.QRect(20, 20, 411, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 131, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.leSDate = QtWidgets.QLineEdit(self.frame)
        self.leSDate.setGeometry(QtCore.QRect(150, 20, 251, 31))
        self.leSDate.setText("")
        self.leSDate.setReadOnly(True)
        self.leSDate.setObjectName("leSDate")
        self.leISpend = QtWidgets.QLineEdit(self.frame)
        self.leISpend.setGeometry(QtCore.QRect(150, 60, 251, 31))
        self.leISpend.setText("")
        self.leISpend.setObjectName("leISpend")
        self.leIPrice = QtWidgets.QLineEdit(self.frame)
        self.leIPrice.setGeometry(QtCore.QRect(150, 100, 251, 31))
        self.leIPrice.setText("")
        self.leIPrice.setObjectName("leIPrice")
        self.comboCat = QtWidgets.QComboBox(self.frame)
        self.comboCat.setGeometry(QtCore.QRect(150, 141, 251, 31))
        self.comboCat.setObjectName("comboCat")
        self.comboCat.addItem("")
        self.comboCat.addItem("")
        self.comboCat.addItem("")
        self.comboCat.addItem("")
        self.comboCat.addItem("")
        self.comboCat.addItem("")
        self.pbAdd = QtWidgets.QPushButton(AddData)
        self.pbAdd.setGeometry(QtCore.QRect(290, 220, 141, 41))
        self.pbAdd.setObjectName("pbAdd")

        self.retranslateUi(AddData)
        self.comboCat.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(AddData)

    def retranslateUi(self, AddData):
        _translate = QtCore.QCoreApplication.translate
        AddData.setWindowTitle(_translate("AddData", "Add Expenses"))
        self.label.setText(_translate("AddData", "Select Date:"))
        self.label_2.setText(_translate("AddData", "Item Spended:"))
        self.label_3.setText(_translate("AddData", "Item Price:"))
        self.label_4.setText(_translate("AddData", "Category:"))
        self.comboCat.setItemText(0, _translate("AddData", "CLOTHES"))
        self.comboCat.setItemText(1, _translate("AddData", "FOODS"))
        self.comboCat.setItemText(2, _translate("AddData", "PAYMENTS/BILLS"))
        self.comboCat.setItemText(3, _translate("AddData", "SPORTS"))
        self.comboCat.setItemText(4, _translate("AddData", "GIFTS"))
        self.comboCat.setItemText(5, _translate("AddData", "OTHERS"))
        self.pbAdd.setText(_translate("AddData", "ADD EXPENSE"))