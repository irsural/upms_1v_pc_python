from enum import IntEnum
from copy import deepcopy
from typing import List
import logging

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QColor

from utils import exception_decorator_print

from upms_database import UpmsDatabase
from upms_measure import UpmsMeasure
from text import Text


class UpmsDatabaseModel(QAbstractTableModel):
    class Column(IntEnum):
        ID = 0
        USER_ID = 1
        TYPE = 2
        DATE = 3
        COMMENT = 4
        INTERVAL = 5
        RESULT = 6
        COUNT = 7

    COLUMN_TO_NAME = {
        Column.ID: Text.get("id"),
        Column.USER_ID: Text.get("uid_2"),
        Column.TYPE: Text.get("type"),
        Column.DATE: Text.get("date"),
        Column.COMMENT: Text.get("comment"),
        Column.INTERVAL: Text.get("interval"),
        Column.RESULT: Text.get("result"),
    }

    COLUMN_TO_UPMS_MEASURE_ATTR = {
        Column.ID: "id",
        Column.USER_ID: "user_id",
        Column.TYPE: "type",
        Column.DATE: "date",
        Column.COMMENT: "comment",
        Column.INTERVAL: "interval",
        Column.RESULT: "result",
    }

    TABLE_COLOR = QColor(255, 255, 255)

    def __init__(self, a_db: UpmsDatabase, a_parent=None):
        super().__init__(a_parent)
        self.__db = a_db
        self.__records = self.__db.get_all()

    def rowCount(self, parent=QModelIndex()):
        return len(self.__records)

    def columnCount(self, parent=QModelIndex()):
        return UpmsDatabaseModel.Column.COUNT

    def headerData(self, section: int, orientation: Qt.Orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == QtCore.Qt.Horizontal:
            if section == UpmsDatabaseModel.Column.ID:
                text = Text.get("id")
            elif section == UpmsDatabaseModel.Column.USER_ID:
                text = Text.get("uid_2")
            elif section == UpmsDatabaseModel.Column.TYPE:
                text = Text.get("type")
            elif section == UpmsDatabaseModel.Column.DATE:
                text = Text.get("date")
            elif section == UpmsDatabaseModel.Column.COMMENT:
                text = Text.get("comment")
            elif section == UpmsDatabaseModel.Column.INTERVAL:
                text = Text.get("interval")
            else:  # section == UpmsDatabaseModel.Column.RESULT:
                text = Text.get("result")

            return text

        return QVariant()

    def get_id_by_row(self, a_row):
        return self.__records[a_row].__getattribute__(UpmsDatabaseModel.COLUMN_TO_UPMS_MEASURE_ATTR[self.Column.ID])

    def get_upms_measure_by_row(self, a_row) -> UpmsMeasure:
        return deepcopy(self.__records[a_row])

    def remove_row(self, a_row: int):
        self.beginRemoveRows(QModelIndex(), a_row, a_row)
        self.__db.remove(self.__records[a_row].id)
        del self.__records[a_row]
        self.endRemoveRows()

    def update_result(self, a_row: int, a_value: str):
        self.__records[a_row].result = a_value
        self.__db.update(self.__records[a_row])

    def get_type(self, a_row: int):
        return self.__records[a_row].type

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or (self.rowCount() < index.row()) or \
                (role != Qt.DisplayRole and role != Qt.EditRole and role != Qt.BackgroundRole):
            return QVariant()
        if role == Qt.BackgroundRole:
            return QtCore.QVariant(QtGui.QBrush(UpmsDatabaseModel.TABLE_COLOR))
        else:
            cell_value = self.__records[index.row()].__getattribute__(
                UpmsDatabaseModel.COLUMN_TO_UPMS_MEASURE_ATTR[index.column()])

            if index.column() == UpmsDatabaseModel.Column.TYPE:
                type_to_str = {
                    UpmsMeasure.MeasureType.MECH_STOPWATCH: Text.get("m_stopwatch"),
                    UpmsMeasure.MeasureType.ELEC_STOPWATCH: Text.get("e_stopwatch"),
                    UpmsMeasure.MeasureType.CLOCK: Text.get("clock"),
                }
                cell_value = type_to_str[cell_value]

            return str(cell_value)

    def setData(self, index: QModelIndex, value: str, role=Qt.EditRole):
        self.__records[index.row()].__setattr__(
            UpmsDatabaseModel.COLUMN_TO_UPMS_MEASURE_ATTR[index.column()], value)
        self.__db.update(self.__records[index.row()])
        return True

    def flags(self, index):
        item_flags = super().flags(index)
        if index.isValid():
            if index.column() in (UpmsDatabaseModel.Column.COMMENT, UpmsDatabaseModel.Column.RESULT):
                item_flags |= Qt.ItemIsEditable
        return item_flags
