from irspy.qt import ui_to_py
ui_to_py.convert_resources("../irspy/qt/resources", ".")
ui_to_py.convert_ui("./ui", "./ui/py")
ui_to_py.convert_ui("../irspy/qt/custom_widgets/ui_forms", "../irspy/qt/custom_widgets/ui_py")
ui_to_py.create_translate("./ui/py", "./ui/ts/translate_en.ts")


def main():
    # Импорты здесь, чтобы ловить исключения в собранной версии программы, если они возникнут при импорте
    import sys

    from PyQt5.QtWidgets import QApplication
    from PyQt5 import QtCore, QtGui

    from mainwindow import MainWindow

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QtGui.QFont("MS Shell Dlg 2", 10))

    w = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    try:
        import traceback
        main()
    except Exception as err:
        print(traceback.format_exc())
