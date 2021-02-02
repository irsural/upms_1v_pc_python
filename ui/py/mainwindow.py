# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 673)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./ui\\../main_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mw_splitter_1 = QtWidgets.QSplitter(self.centralwidget)
        self.mw_splitter_1.setOrientation(QtCore.Qt.Vertical)
        self.mw_splitter_1.setObjectName("mw_splitter_1")
        self.frame = QtWidgets.QFrame(self.mw_splitter_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.download_progress_bar = QtWidgets.QProgressBar(self.frame)
        self.download_progress_bar.setProperty("value", 0)
        self.download_progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.download_progress_bar.setInvertedAppearance(False)
        self.download_progress_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.download_progress_bar.setObjectName("download_progress_bar")
        self.gridLayout_3.addWidget(self.download_progress_bar, 1, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.download_from_upms_button = QtWidgets.QPushButton(self.frame)
        self.download_from_upms_button.setObjectName("download_from_upms_button")
        self.gridLayout_3.addWidget(self.download_from_upms_button, 0, 4, 1, 1)
        self.ip_edit = QtWidgets.QLineEdit(self.frame)
        self.ip_edit.setObjectName("ip_edit")
        self.gridLayout_3.addWidget(self.ip_edit, 0, 1, 1, 1)
        self.download_path_edit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_path_edit.sizePolicy().hasHeightForWidth())
        self.download_path_edit.setSizePolicy(sizePolicy)
        self.download_path_edit.setMinimumSize(QtCore.QSize(0, 0))
        self.download_path_edit.setObjectName("download_path_edit")
        self.gridLayout_3.addWidget(self.download_path_edit, 0, 3, 1, 1)
        self.measures_table = QtWidgets.QTableView(self.frame)
        self.measures_table.setAlternatingRowColors(True)
        self.measures_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.measures_table.setSortingEnabled(True)
        self.measures_table.setObjectName("measures_table")
        self.measures_table.horizontalHeader().setSortIndicatorShown(True)
        self.measures_table.horizontalHeader().setStretchLastSection(True)
        self.measures_table.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.measures_table, 2, 0, 1, 4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_result_button = QtWidgets.QPushButton(self.frame)
        self.input_result_button.setObjectName("input_result_button")
        self.verticalLayout_2.addWidget(self.input_result_button)
        self.create_report_button = QtWidgets.QPushButton(self.frame)
        self.create_report_button.setObjectName("create_report_button")
        self.verticalLayout_2.addWidget(self.create_report_button)
        self.remove_selected_button = QtWidgets.QPushButton(self.frame)
        self.remove_selected_button.setObjectName("remove_selected_button")
        self.verticalLayout_2.addWidget(self.remove_selected_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.frame_2 = QtWidgets.QFrame(self.mw_splitter_1)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.log_text_edit = QtWidgets.QTextEdit(self.frame_2)
        self.log_text_edit.setObjectName("log_text_edit")
        self.gridLayout.addWidget(self.log_text_edit, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.mw_splitter_1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.open_about_action = QtWidgets.QAction(MainWindow)
        self.open_about_action.setObjectName("open_about_action")
        self.menu.addAction(self.open_about_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UPMS-1V PC"))
        self.download_progress_bar.setFormat(_translate("MainWindow", "%p%"))
        self.label_2.setText(_translate("MainWindow", "Каталог для загрузки файлов:"))
        self.label.setText(_translate("MainWindow", "IP-адрес:"))
        self.download_from_upms_button.setText(_translate("MainWindow", "Скачать результаты\n"
"с установки"))
        self.input_result_button.setText(_translate("MainWindow", "Ввести\n"
"результат"))
        self.create_report_button.setText(_translate("MainWindow", "Сформировать\n"
"отчет"))
        self.remove_selected_button.setText(_translate("MainWindow", "Удалить\n"
"выделенные"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.open_about_action.setText(_translate("MainWindow", "О программе..."))
import icons_rc
