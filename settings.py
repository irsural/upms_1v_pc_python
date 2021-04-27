from irspy.qt.qt_settings_ini_parser import QtSettings


def get_ini_settings(a_path):
    return QtSettings(a_path, [
        QtSettings.VariableInfo(a_name="save_folder_path", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="ip", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="path", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="name_template", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="save_folder", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="language", a_section="PARAMETERS", a_type=QtSettings.ValueType.INT, a_default=1),
    ])
