# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGeraCPF = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnGeraCPF.setFont(font)
        self.btnGeraCPF.setObjectName("btnGeraCPF")
        self.gridLayout.addWidget(self.btnGeraCPF, 0, 3, 1, 1)
        self.btnValidaCPF = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnValidaCPF.setFont(font)
        self.btnValidaCPF.setObjectName("btnValidaCPF")
        self.gridLayout.addWidget(self.btnValidaCPF, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.labelValidaCPF = QtWidgets.QLabel(self.centralwidget)
        self.labelValidaCPF.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelValidaCPF.setFont(font)
        self.labelValidaCPF.setStyleSheet("background: white; color: grey;")
        self.labelValidaCPF.setText("")
        self.labelValidaCPF.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValidaCPF.setObjectName("labelValidaCPF")
        self.gridLayout.addWidget(self.labelValidaCPF, 2, 0, 1, 4)
        self.inputGeraCPF = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.inputGeraCPF.setFont(font)
        self.inputGeraCPF.setStyleSheet("border: 1px solid grey;;")
        self.inputGeraCPF.setText("")
        self.inputGeraCPF.setReadOnly(True)
        self.inputGeraCPF.setObjectName("inputGeraCPF")
        self.gridLayout.addWidget(self.inputGeraCPF, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputValidaCPF = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.inputValidaCPF.setFont(font)
        self.inputValidaCPF.setStyleSheet("border: 1px solid grey;")
        self.inputValidaCPF.setText("")
        self.inputValidaCPF.setObjectName("inputValidaCPF")
        self.gridLayout.addWidget(self.inputValidaCPF, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador/Validador"))
        self.btnGeraCPF.setText(_translate("MainWindow", "Gerar"))
        self.btnValidaCPF.setText(_translate("MainWindow", "Validar"))
        self.label_2.setText(_translate("MainWindow", "VALIDA CPF:"))
        self.inputGeraCPF.setPlaceholderText(_translate("MainWindow", "Selecione o botão para gerar o CPF."))
        self.label.setText(_translate("MainWindow", "NOVO CPF:"))
        self.inputValidaCPF.setPlaceholderText(_translate("MainWindow", "Insira o CPF para verificação."))
