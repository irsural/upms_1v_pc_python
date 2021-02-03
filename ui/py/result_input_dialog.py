# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/result_input_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_result_input_dialog(object):
    def setupUi(self, result_input_dialog):
        result_input_dialog.setObjectName("result_input_dialog")
        result_input_dialog.resize(441, 469)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(result_input_dialog.sizePolicy().hasHeightForWidth())
        result_input_dialog.setSizePolicy(sizePolicy)
        result_input_dialog.setMinimumSize(QtCore.QSize(0, 0))
        result_input_dialog.setMaximumSize(QtCore.QSize(99999, 99999))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/graph_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        result_input_dialog.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(result_input_dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.photo_layout = QtWidgets.QVBoxLayout()
        self.photo_layout.setObjectName("photo_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.photo_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.photo_layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.result_edit = QtWidgets.QLineEdit(result_input_dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.result_edit.setFont(font)
        self.result_edit.setText("")
        self.result_edit.setObjectName("result_edit")
        self.gridLayout.addWidget(self.result_edit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(result_input_dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.next_button = QtWidgets.QPushButton(result_input_dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.next_button.setFont(font)
        self.next_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon1)
        self.next_button.setIconSize(QtCore.QSize(25, 25))
        self.next_button.setDefault(True)
        self.next_button.setObjectName("next_button")
        self.gridLayout.addWidget(self.next_button, 2, 2, 1, 1)
        self.interval_label = QtWidgets.QLabel(result_input_dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.interval_label.setFont(font)
        self.interval_label.setText("")
        self.interval_label.setObjectName("interval_label")
        self.gridLayout.addWidget(self.interval_label, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(result_input_dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(result_input_dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.id_label = QtWidgets.QLabel(result_input_dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.id_label.setFont(font)
        self.id_label.setText("")
        self.id_label.setObjectName("id_label")
        self.gridLayout.addWidget(self.id_label, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(result_input_dialog)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(result_input_dialog)
        QtCore.QMetaObject.connectSlotsByName(result_input_dialog)

    def retranslateUi(self, result_input_dialog):
        _translate = QtCore.QCoreApplication.translate
        result_input_dialog.setWindowTitle(_translate("result_input_dialog", "Ввод результата"))
        self.label.setText(_translate("result_input_dialog", "Интервал"))
        self.label_2.setText(_translate("result_input_dialog", "Результат"))
        self.label_3.setText(_translate("result_input_dialog", "Измерение №"))
        self.cancel_button.setText(_translate("result_input_dialog", "Отмена"))
import icons_rc
