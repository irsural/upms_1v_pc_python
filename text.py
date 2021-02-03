from enum import IntEnum


class Text:
    class Lang(IntEnum):
        RU = 0,
        EN = 1,
        DEFAULT = RU

    language = Lang.DEFAULT

    strings = {
        "version": ["Версия программы 1.{}", "Program version 1.{}"],
        "e_stopwatch": ["Электрический\nсекудомер", "Electric stopwatch"],
        "m_stopwatch": ["Механический\nсекудомер", "Mechanical stopwatch"],
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
        "err": ["Ошибка", "Error"],
        "warning": ["Предупреждение", "Warning"],
        "ask_overwrite": ["Запись с id={} уже существует. Перезаписать?",
                          "Entry with id={} is already exists. Overwrite it?"],
        "path_err": ["Неверно указан каталог для загрузки файлов", "Wrong path to download folder"],
        "ini_err": ['Файл конфигурации поврежден. Пожалуйста, удалите файл "settings.ini" и запустите программу заново',
                    'Configuration file is corrupted. Please, remove "settings.ini and restart the program"'],
        "ip_format_err": ["Неверный формат IP адреса", "Invalid IP address format"],
        "connection_err": ["Не удалось установить соединение с устройством. Проверьте IP-адрес",
                           "The connection to the device could not be established. Check the IP address"],
        "main_table_not_found_err": ['Файл "{}" не обнаружен на устройстве', 'File "{}" is not found on device'],
        "download_err": ["Не удалось скачать файлы с устройства", "Couldn't download files from the device"],
        "get_files_list_err": ["Не удалось скачать файлы (upms_tftp.get_files_list() raise TftpTimeout).",
                               "Failed to download files (upms_tftp.get_files_list() raise TftpTimeout)."],
        "download_file_by_tftp_err": ["Не удалось скачать файл {}. Попытка {}/{}",
                                      "Failed to download file {}. Attempt {}/{}"],
        "photo_not_found": ["Файл {} не найден", "File {} not found"],
        "info": ["Информация", "Information"],
        "selection_info": ["Необходимо выделить строки в таблице", "Select rows in the table, please"],
        "confirm": ["Подтвердите действие", "Confirm the action"],
        "delete_confirm": ["Вы действительно хотите удалить выбранные измерения?",
                           "Are you sure you want to remove the selected measurements?"],
    }

    @staticmethod
    def set_language(a_language: Lang):
        Text.language = a_language

    @staticmethod
    def get(a_text_id: str):
        return Text.strings[a_text_id][Text.language]
