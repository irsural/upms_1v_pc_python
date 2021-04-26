from irspy.qt.qt_settings_ini_parser import QtSettings


def get_ini_settings():
    return QtSettings("./settings.ini", [
        QtSettings.VariableInfo(a_name="save_folder_path", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="ip", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="path", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="name_template", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="save_folder", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="language", a_section="PARAMETERS", a_type=QtSettings.ValueType.INT, a_default=1),
        QtSettings.VariableInfo(a_name="generate_excel", a_section="PARAMETERS", a_type=QtSettings.ValueType.INT, a_default=0),
        QtSettings.VariableInfo(a_name="generate_calc", a_section="PARAMETERS", a_type=QtSettings.ValueType.INT, a_default=1),
    ])
