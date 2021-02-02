from enum import IntEnum, auto
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
        USER_ID = auto()
        TYPE = auto()
        DATE = auto()
        COMMENT = auto()
        INTERVAL = auto()
        RESULT = auto()
        COUNT = auto()

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
        self.__db: UpmsDatabase = a_db
        self.__records: List[UpmsMeasure] = self.__db.get_all()

    def rowCount(self, parent=QModelIndex()):
        return len(self.__records)

    def columnCount(self, parent=QModelIndex()):
        return UpmsDatabaseModel.Column.COUNT

    def headerData(self, section: int, orientation: Qt.Orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == QtCore.Qt.Horizontal:
            return UpmsDatabaseModel.COLUMN_TO_NAME[UpmsDatabaseModel.Column(section)]

        return QVariant()

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
                cell_value = UpmsMeasure.TYPE_TO_STR[cell_value]

            return str(cell_value)

    def setData(self, index: QModelIndex, value: str, role=Qt.EditRole):
        return False
