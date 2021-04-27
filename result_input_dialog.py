import logging
import os

from PyQt5 import QtGui, QtWidgets, QtCore

from ui.py.result_input_dialog import Ui_result_input_dialog as ResultInputForm
from upms_measure import UpmsMeasure
from text import Text
from irspy.qt.qt_settings_ini_parser import QtSettings


class ResultInputDialog(QtWidgets.QDialog):
    def __init__(self, a_upms_measure: UpmsMeasure, a_images_file_path: str, a_settings: QtSettings, a_parent=None):
        super().__init__(a_parent)

        self.ui = ResultInputForm()
        self.ui.setupUi(self)
        self.settings = a_settings

        a_image_path = a_images_file_path.rstrip(os.sep) + os.sep + "{}.jpg".format(a_upms_measure.id)
        if os.path.isfile(a_image_path):
            self.ui.photo_layout.removeItem(self.ui.photo_layout.itemAt(0))
            image = QtGui.QImage(a_image_path)
            image_label = QtWidgets.QLabel("")
            image_label.setPixmap(QtGui.QPixmap.fromImage(image))
            image_label.adjustSize()
            self.ui.photo_layout.addWidget(image_label)
        else:
            logging.warning(Text.get("photo_not_found").format(a_image_path))

        self.ui.id_label.setText(str(a_upms_measure.id))
        self.ui.interval_label.setText(a_upms_measure.interval)
        self.ui.result_edit.setText(a_upms_measure.result)

        self.settings.restore_qwidget_state(self)

        self.ui.next_button.clicked.connect(self.accept)
        self.ui.cancel_button.clicked.connect(self.reject)

    def get_result(self):
        return self.ui.result_edit.text()

    def closeEvent(self, a_event: QtGui.QCloseEvent) -> None:
        self.settings.save_qwidget_state(self)

    def __del__(self):
        print("ResultInputDialog deleted")
