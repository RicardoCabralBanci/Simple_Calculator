# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculadora_Comum.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalculadoraComum(object):
    def setupUi(self, CalculadoraComum):
        CalculadoraComum.setObjectName("CalculadoraComum")
        CalculadoraComum.resize(500, 300)
        CalculadoraComum.setMinimumSize(QtCore.QSize(500, 300))
        self.layoutWidget = QtWidgets.QWidget(CalculadoraComum)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 281))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.igual = QtWidgets.QPushButton(self.layoutWidget)
        self.igual.setObjectName("igual")
        self.gridLayout.addWidget(self.igual, 6, 5, 1, 1)
        self.vezes = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.vezes.setFont(font)
        self.vezes.setObjectName("vezes")
        self.gridLayout.addWidget(self.vezes, 3, 5, 1, 1)
        self.mais = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mais.setFont(font)
        self.mais.setObjectName("mais")
        self.gridLayout.addWidget(self.mais, 5, 5, 1, 1)
        self.oito = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.oito.setFont(font)
        self.oito.setObjectName("oito")
        self.gridLayout.addWidget(self.oito, 3, 1, 1, 2)
        self.menos = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menos.setFont(font)
        self.menos.setObjectName("menos")
        self.gridLayout.addWidget(self.menos, 4, 5, 1, 1)
        self.dois = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dois.setFont(font)
        self.dois.setObjectName("dois")
        self.gridLayout.addWidget(self.dois, 5, 1, 1, 2)
        self.nove = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nove.setFont(font)
        self.nove.setObjectName("nove")
        self.gridLayout.addWidget(self.nove, 3, 3, 1, 2)
        self.seis = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.seis.setFont(font)
        self.seis.setObjectName("seis")
        self.gridLayout.addWidget(self.seis, 4, 3, 1, 2)
        self.apaga = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.apaga.setFont(font)
        self.apaga.setObjectName("apaga")
        self.gridLayout.addWidget(self.apaga, 2, 3, 1, 2)
        self.quatro = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quatro.setFont(font)
        self.quatro.setObjectName("quatro")
        self.gridLayout.addWidget(self.quatro, 4, 0, 1, 1)
        self.trez = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.trez.setFont(font)
        self.trez.setObjectName("trez")
        self.gridLayout.addWidget(self.trez, 5, 3, 1, 2)
        self.sete = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sete.setFont(font)
        self.sete.setObjectName("sete")
        self.gridLayout.addWidget(self.sete, 3, 0, 1, 1)
        self.display = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.display.setFont(font)
        self.display.setText("")
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 1, 0, 1, 6)
        self.C = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.C.setFont(font)
        self.C.setObjectName("C")
        self.gridLayout.addWidget(self.C, 2, 0, 1, 1)
        self.virgula = QtWidgets.QPushButton(self.layoutWidget)
        self.virgula.setObjectName("virgula")
        self.gridLayout.addWidget(self.virgula, 6, 1, 1, 2)
        self.divisao = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.divisao.setFont(font)
        self.divisao.setObjectName("divisao")
        self.gridLayout.addWidget(self.divisao, 2, 5, 1, 1)
        self.cinco = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cinco.setFont(font)
        self.cinco.setObjectName("cinco")
        self.gridLayout.addWidget(self.cinco, 4, 1, 1, 2)
        self.voltar = QtWidgets.QPushButton(self.layoutWidget)
        self.voltar.setObjectName("voltar")
        self.gridLayout.addWidget(self.voltar, 6, 0, 1, 1)
        self.raiz = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.raiz.setFont(font)
        self.raiz.setObjectName("raiz")
        self.gridLayout.addWidget(self.raiz, 2, 1, 1, 2)
        self.zero = QtWidgets.QPushButton(self.layoutWidget)
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 6, 3, 1, 2)
        self.um = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.um.setFont(font)
        self.um.setObjectName("um")
        self.gridLayout.addWidget(self.um, 5, 0, 1, 1)
        self.Titulo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setObjectName("Titulo")
        self.gridLayout.addWidget(self.Titulo, 0, 0, 1, 6)

        self.retranslateUi(CalculadoraComum)
        QtCore.QMetaObject.connectSlotsByName(CalculadoraComum)

    def retranslateUi(self, CalculadoraComum):
        _translate = QtCore.QCoreApplication.translate
        CalculadoraComum.setWindowTitle(_translate("CalculadoraComum", "Calculadora Comum"))
        self.igual.setText(_translate("CalculadoraComum", "="))
        self.vezes.setText(_translate("CalculadoraComum", "*"))
        self.mais.setText(_translate("CalculadoraComum", "+"))
        self.oito.setText(_translate("CalculadoraComum", "8"))
        self.menos.setText(_translate("CalculadoraComum", "-"))
        self.dois.setText(_translate("CalculadoraComum", "2"))
        self.nove.setText(_translate("CalculadoraComum", "9"))
        self.seis.setText(_translate("CalculadoraComum", "6"))
        self.apaga.setText(_translate("CalculadoraComum", "<--"))
        self.quatro.setText(_translate("CalculadoraComum", "4"))
        self.trez.setText(_translate("CalculadoraComum", "3"))
        self.sete.setText(_translate("CalculadoraComum", "7"))
        self.C.setText(_translate("CalculadoraComum", "C"))
        self.virgula.setText(_translate("CalculadoraComum", "."))
        self.divisao.setText(_translate("CalculadoraComum", "/"))
        self.cinco.setText(_translate("CalculadoraComum", "5"))
        self.voltar.setText(_translate("CalculadoraComum", "Voltar"))
        self.raiz.setText(_translate("CalculadoraComum", "sqrt(x)"))
        self.zero.setText(_translate("CalculadoraComum", "0"))
        self.um.setText(_translate("CalculadoraComum", "1"))
        self.Titulo.setText(_translate("CalculadoraComum", "CALCULADORA COMUM"))
