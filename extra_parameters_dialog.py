from typing import List, Tuple
from enum import IntEnum

from PyQt5 import QtGui, QtWidgets, QtCore

from irspy.qt.qt_settings_ini_parser import QtSettings
from irspy.qt.custom_widgets.QTableDelegates import TransparentPainterForWidget
from irspy.qt import qt_utils

from ui.py.extra_parameters_dialog import Ui_extra_parameters_dialog as ExtraParametersForm
from text import Text


class ExtraParametersDialog(QtWidgets.QDialog):
    class Column(IntEnum):
        PARAMETER = 0
        VALUE = 1

    def __init__(self, a_init_parameters: List[Tuple[str, str]], a_settings: QtSettings,  a_parent=None):
        super().__init__(a_parent)

        self.ui = ExtraParametersForm()
        self.ui.setupUi(self)

        self.settings = a_settings

        self.settings.restore_qwidget_state(self)
        self.settings.restore_qwidget_state(self.ui.parameters_table)

        self.ui.parameters_table.setItemDelegate(TransparentPainterForWidget(self.ui.parameters_table, "#d4d4ff"))

        for row_data in a_init_parameters:
            qt_utils.qtablewidget_append_row(self.ui.parameters_table, row_data)

        self.ui.add_parameter_button.clicked.connect(self.add_parameter_button_clicked)
        self.ui.remove_parameter_button.clicked.connect(self.remove_parameter_button_clicked)

        self.ui.ok_button.clicked.connect(self.accept)
        self.ui.cancel_button.clicked.connect(self.reject)

    def add_parameter_button_clicked(self):
        qt_utils.qtablewidget_append_row(self.ui.parameters_table, ["", ""])

    def remove_parameter_button_clicked(self):
        qt_utils.qtablewidget_delete_selected(self.ui.parameters_table)

    def get_parameters(self) -> List[Tuple[str, str]]:
        parameters = []
        for row in range(self.ui.parameters_table.rowCount()):
            parameters.append((self.ui.parameters_table.item(row, self.Column.PARAMETER).text(),
                               self.ui.parameters_table.item(row, self.Column.VALUE).text()))
        return parameters

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.settings.save_qwidget_state(self.ui.parameters_table)
        self.settings.save_qwidget_state(self)

    def __del__(self):
        print("ExtraParametersDialog deleted")
