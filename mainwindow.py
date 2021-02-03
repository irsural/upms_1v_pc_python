from logging.handlers import RotatingFileHandler
from typing import List, Optional
import logging
import socket
import os

from PyQt5 import QtWidgets, QtCore, QtGui

from irspy.qt.custom_widgets.QTableDelegates import TransparentPainterForView
from irspy.utils import exception_decorator, exception_decorator_print
from irspy.settings_ini_parser import BadIniException
from irspy.qt import qt_utils

from ui.py.mainwindow import Ui_MainWindow as MainForm
from result_input_dialog import ResultInputDialog
from upms_db_model import UpmsDatabaseModel
from upms_database import UpmsDatabase
from about_dialog import AboutDialog
from upms_measure import UpmsMeasure
from text import Text
import upms_tftp
import settings


class MainWindow(QtWidgets.QMainWindow):
    measures_filename = "main_table.csv"

    def __init__(self):
        super().__init__()

        self.ui = MainForm()
        self.ui.setupUi(self)

        try:
            self.settings = settings.get_ini_settings()
            ini_ok = True
        except BadIniException:
            ini_ok = False
            QtWidgets.QMessageBox.critical(self, Text.get("err"), Text.get("ini_err"))
        if ini_ok:
            self.settings.restore_qwidget_state(self)
            self.settings.restore_qwidget_state(self.ui.mw_splitter_1)
            self.settings.restore_qwidget_state(self.ui.measures_table)

            self.ui.download_progress_bar.setHidden(True)

            self.set_up_logger()

            self.ui.measures_table.setItemDelegate(TransparentPainterForView(self.ui.measures_table, "#d4d4ff"))
            self.ui.download_path_edit.setText(self.settings.save_folder_path)

            self.ui.ip_edit.setText(self.settings.ip)
            self.ui.download_path_edit.setText(self.settings.path)

            self.db = UpmsDatabase("database.db")
            self.measures_table_model: Optional[UpmsDatabaseModel] = None
            self.proxy: Optional[QtCore.QSortFilterProxyModel] = None
            self.update_model()

            self.show()
            self.connect_all()

            self.tick_timer = QtCore.QTimer(self)
            self.tick_timer.timeout.connect(self.tick)
            self.tick_timer.start(10)
        else:
            self.close()

    def connect_all(self):
        self.ui.open_about_action.triggered.connect(self.open_about)
        self.ui.download_from_upms_button.clicked.connect(self.download_from_upms_button_clicked)
        self.ui.ip_edit.textChanged.connect(self.ip_changed)
        self.ui.download_path_edit.textChanged.connect(self.path_changed)

        self.ui.input_result_button.clicked.connect(self.input_result_button_clicked)
        self.ui.create_report_button.clicked.connect(self.create_report_button_clicked)
        self.ui.remove_selected_button.clicked.connect(self.remove_selected_button_clicked)

    def set_up_logger(self):
        log = qt_utils.QTextEditLogger(self.ui.log_text_edit)
        log.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%H:%M:%S'))

        file_log = RotatingFileHandler("upms_1v_pc.log", maxBytes=30*1024*1024, backupCount=3, encoding='utf8')
        file_log.setLevel(logging.DEBUG)
        file_log.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S'))

        logging.getLogger().addHandler(file_log)
        logging.getLogger().addHandler(log)
        logging.getLogger().setLevel(logging.WARNING)

    def update_model(self):
        self.measures_table_model = UpmsDatabaseModel(self.db, self)
        self.proxy = QtCore.QSortFilterProxyModel()
        self.proxy.setSourceModel(self.measures_table_model)
        self.ui.measures_table.setModel(self.proxy)
        self.ui.measures_table.resizeRowsToContents()

    @exception_decorator
    def tick(self):
        pass

    def download_measures_list(self, a_download_filepath: str) -> bool:
        result = False
        ip = self.ui.ip_edit.text()
        try:
            socket.inet_aton(ip)
        except socket.error:
            QtWidgets.QMessageBox.critical(self, Text.get("err"), Text.get("ip_format_err"),
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            try:
                files_list = upms_tftp.get_files_list(self.ui.ip_edit.text())
            except ConnectionResetError:
                QtWidgets.QMessageBox.critical(self, Text.get("err"), Text.get("connection_err"),
                                               QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            else:
                if files_list is not None:
                    if self.measures_filename in files_list:
                        try:
                            upms_tftp.download_file_by_tftp(ip, self.measures_filename, a_download_filepath)
                            result = True
                        except FileNotFoundError:
                            QtWidgets.QMessageBox.critical(self, Text.get("err"), Text.get("path_err"),
                                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
                    else:
                        QtWidgets.QMessageBox.critical(self, Text.get("err"),
                                                       Text.get("main_table_not_found_err").format(self.measures_filename),
                                                       QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(self, Text.get("err"), Text.get("download_err"),
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        return result

    def download_photo(self, a_measure_id: int, a_files_list: List[str], a_download_folder: str):
        photo_name = f"{a_measure_id}.jpg"
        download_path = a_download_folder.rstrip(os.sep) + os.sep + photo_name
        if photo_name in a_files_list:
            logging.warning(f"Download {photo_name}")
            upms_tftp.download_file_by_tftp(self.ui.ip_edit.text(), photo_name, download_path)

    @exception_decorator
    def download_from_upms_button_clicked(self, _):
        download_folder = self.ui.download_path_edit.text()
        if download_folder and os.path.isdir(download_folder):
            download_filepath = download_folder.rstrip(os.sep) + os.sep + self.measures_filename

            if self.download_measures_list(download_filepath):
                with open(download_filepath, 'r', encoding='utf8') as measures_list_file:
                    # Первая строка - заголовок
                    measures_list = [file for idx, file in enumerate(measures_list_file) if idx != 0]

                update_all = False
                upms_files_list = upms_tftp.get_files_list(self.ui.ip_edit.text())
                self.ui.download_progress_bar.setHidden(False)
                for number, measure in enumerate(measures_list):
                    self.ui.download_progress_bar.setValue(number / len(upms_files_list) * self.ui.download_progress_bar.maximum())

                    measure_params = [meas.strip() for meas in measure.strip().split(',')]
                    upms_measure = UpmsMeasure(*measure_params)
                    upms_prev_measure = self.db.get(upms_measure.id)

                    if upms_measure != upms_prev_measure:
                        if upms_prev_measure is None:
                            self.db.add(upms_measure)
                            self.download_photo(upms_measure.id, upms_files_list, download_folder)
                        else:
                            if update_all:
                                res = QtWidgets.QMessageBox.Yes
                            else:
                                res = QtWidgets.QMessageBox.question(
                                    self, Text.get("warning"), Text.get("ask_overwrite").format(upms_measure.id),
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.YesAll |
                                    QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Yes
                                )
                            if res == QtWidgets.QMessageBox.Yes:
                                self.db.update(upms_measure)
                                self.download_photo(upms_measure.id, upms_files_list, download_folder)
                            elif res == QtWidgets.QMessageBox.YesAll:
                                self.db.update(upms_measure)
                                self.download_photo(upms_measure.id, upms_files_list, download_folder)
                                update_all = True
                            elif res == QtWidgets.QMessageBox.Cancel:
                                break
                    elif not os.path.isfile(download_folder.rstrip(os.sep) + os.sep + f"{upms_measure.id}.jpg"):
                        # Докачиваем файл, если запись в БД есть, а файла нет
                        self.download_photo(upms_measure.id, upms_files_list, download_folder)

                self.ui.download_progress_bar.setValue(0)
                self.ui.download_progress_bar.setHidden(True)
                self.update_model()
        else:
            QtWidgets.QMessageBox.critical(self, Text.get("err"), Text.get("path_err"),
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def ip_changed(self, a_ip):
        self.settings.ip = a_ip

    def path_changed(self, a_path):
        self.settings.path = a_path

    @exception_decorator_print
    def input_result_button_clicked(self, _):
        rows = self.ui.measures_table.selectionModel().selectedRows()
        if rows:
            for idx in rows:
                real_row = self.proxy.mapToSource(idx).row()

                self.ui.measures_table.selectionModel().setCurrentIndex(
                    self.measures_table_model.index(idx.row(), 0),
                    QtCore.QItemSelectionModel.ClearAndSelect | QtCore.QItemSelectionModel.Rows
                )
                files_path = self.ui.download_path_edit.text()
                if files_path and os.path.isdir(files_path):
                    upms_measure = self.measures_table_model.get_upms_measure_by_row(real_row)
                    dialog = ResultInputDialog(upms_measure, files_path, self.settings, self)
                    res = dialog.exec()
                    if res == QtWidgets.QDialog.Accepted:
                        new_result = dialog.get_result()
                        self.measures_table_model.update_result(real_row, new_result)
                        logging.warning(upms_measure.result)
                        # Для сохранения состояния (иначе не вызывается closeEvent)
                        dialog.close()
                    else:
                        break
                else:
                    QtWidgets.QMessageBox.critical(self, Text.get("err"), Text.get("path_err"),
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, Text.get("info"), Text.get("selection_info"),
                                              QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def create_report_button_clicked(self, _):
        rows = self.ui.measures_table.selectionModel().selectedRows()
        if rows:
            for idx in rows:
                real_row = self.proxy.mapToSource(idx).row()
        else:
            QtWidgets.QMessageBox.information(self, Text.get("info"), Text.get("selection_info"),
                                              QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def remove_selected_button_clicked(self, _):
        rows = self.ui.measures_table.selectionModel().selectedRows()
        if rows:
            res = QtWidgets.QMessageBox.question(self, Text.get("confirm"), Text.get("delete_confirm"),
                                                 QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
                                                 QtWidgets.QMessageBox.Cancel)
            if res == QtWidgets.QMessageBox.Ok:
                real_rows = [self.proxy.mapToSource(r).row() for r in rows]
                real_rows.sort(reverse=True)
                for row in real_rows:
                    self.measures_table_model.remove_row(row)
        else:
            QtWidgets.QMessageBox.information(self, Text.get("info"), Text.get("selection_info"),
                                              QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def open_about(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec()

    def closeEvent(self, a_event: QtGui.QCloseEvent):
        self.settings.save_qwidget_state(self.ui.measures_table)
        self.settings.save_qwidget_state(self.ui.mw_splitter_1)
        self.settings.save_qwidget_state(self)
        a_event.accept()
