from enum import IntEnum


class Text:
    class Lang(IntEnum):
        RU = 0,
        EN = 1,
        DEFAULT = RU

    LANG_TO_QT_TRANSLATE = {
        Lang.RU: "translate_ru",
        Lang.EN: "translate_en",
        Lang.DEFAULT: "translate_ru",
    }

    language = Lang.DEFAULT

    strings = {
        "version": ["Версия программы 1.{}", "Software version 1.{}"],
        "e_stopwatch": ["Электрический\nсекудомер", "Electric stopwatch"],
        "m_stopwatch": ["Механический\nсекудомер", "Mechanical  stopwatch"],
        "clock": ["Часы", "Clock"],
        "id": ["ID", "ID"],
        "uid": ["ID пользователя", "User ID"],
        "uid_2": ["ID\nпользователя", "User\nID"],
        "type": ["Тип", "Type"],
        "date": ["Дата", "Date"],
        "comment": ["Комментарий", "Comment"],
        "interval": ["Интервал", "Interval"],
        "result": ["Результат", "Result"],
        "other": ["Другое", "Other"],
        "measure": ["Номер измерения: {}", "Measurement # {}"],
        "download_folder": ["Папка для загрузки файлов", "Download location"],
        "save_folder": ["Папка для сохранения протоколов", "Protocols’ location"],

        "warning": ["Предупреждение", "Warning"],
        "download_canceled": ["Скачивание отменено", "Download cancelled"],
        "ask_overwrite": ["Запись с id={} уже существует. Перезаписать?",
                          "Entry with id={} already exists. Overwrite?"],

        "err": ["Ошибка", "Error"],
        "path_err": ["Неверно указана папка для загрузки файлов", "Invalid download location"],
        "save_folder_error": ["Неверно указана папка для сохранения протоколов", "Invalid protocols’ location"],
        "templates_are_not_found": ['Файл шаблона не найден', 'Template file not found'],
        "ini_err": ['Файл конфигурации поврежден. Пожалуйста, удалите файл "settings.ini" и запустите программу заново',
                    'Configuration file is corrupted. Please, delete the "settings.ini file and restart the program"'],
        "ip_format_err": ["Неверный формат IP адреса", "Invalid IP address format"],
        "connection_err": ["Не удалось установить соединение с устройством. Проверьте IP-адрес",
                           "Connection with the device unsuccessful. Check IP-address"],
        "main_table_not_found_err": ['Файл "{}" не обнаружен на устройстве', '"{}" file not found on the device'],
        "download_err": ["Не удалось скачать файлы с устройства", "Failed to download files from the device"],
        "get_files_list_err": ["Не удалось скачать файлы (upms_tftp.get_files_list() raise TftpTimeout).",
                               "Failed to download files (upms_tftp.get_files_list() raise TftpTimeout)."],
        "download_file_by_tftp_err": ["Не удалось скачать файл {}. Попытка {}/{}",
                                      "Failed to download file {}. Try {}/{}"],
        "same_type_err": ["Измерения должны быть одного типа", "Measurements must be of the same type"],
        "data_sheet_not_found": ['Страница "Данные" в файле "{}" не найдена', 'The "Data" sheet in "{}" file not found'],
        "photo_not_found": ["Файл {} не найден", "{} file not found"],

        "info": ["Информация", "Information"],
        "selection_info": ["Необходимо выделить строки в таблице", "It is necessary to select rows in the table"],
        "success_download": ["Скачивание успешно завершено", "Download complete"],
        "success_generated": ["Протокол успешно сгенерирован", "Protocol generated"],

        "confirm": ["Подтвердите действие", "Confirm action"],
        "delete_confirm": ["Вы действительно хотите удалить выбранные измерения?",
                           "Are you sure you want to delete the selected measurements?"],
    }

    @staticmethod
    def set_language(a_language: Lang):
        Text.language = a_language

    @staticmethod
    def get(a_text_id: str):
        return Text.strings[a_text_id][Text.language]
