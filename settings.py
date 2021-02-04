from irspy.qt.qt_settings_ini_parser import QtSettings


def get_ini_settings():
    return QtSettings("./settings.ini", [
        QtSettings.VariableInfo(a_name="save_folder_path", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="ip", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="path", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="name_template", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="save_folder", a_section="PARAMETERS", a_type=QtSettings.ValueType.STRING),
        QtSettings.VariableInfo(a_name="language", a_section="PARAMETERS", a_type=QtSettings.ValueType.INT, a_default=1),
        # QtSettings.VariableInfo(a_name="log_scale_enabled", a_section="PARAMETERS", a_type=QtSettings.ValueType.INT),
        # QtSettings.VariableInfo(a_name="graph_points_count", a_section="PARAMETERS", a_type=QtSettings.ValueType.INT),
        # QtSettings.VariableInfo(a_name="fixed_step_list", a_section="PARAMETERS", a_type=QtSettings.ValueType.LIST_FLOAT,
        #                         a_default=[0.0001, 0.01, 0.1, 1, 10, 20, 100]),
        # QtSettings.VariableInfo(a_name="checkbox_states", a_section="PARAMETERS", a_type=QtSettings.ValueType.LIST_INT),
        # QtSettings.VariableInfo(a_name="rough_step", a_section="PARAMETERS", a_type=QtSettings.ValueType.FLOAT, a_default=0.5),
    ])
