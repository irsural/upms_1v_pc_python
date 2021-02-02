from enum import IntEnum


class Text:
    class Lang(IntEnum):
        RU = 0,
        EN = 1,
        DEFAULT = RU

    language = Lang.DEFAULT

    strings = {
        "e_stopwatch": ["Электрический секудомер", "Electric stopwatch"],
        "m_stopwatch": ["Механический секудомер", "Mechanical stopwatch"],
        "clock": ["Часы", "Clock"],
        "id": ["ID", "ID"],
        "uid": ["ID пользователя", "User ID"],
        "type": ["Тип", "Type"],
        "date": ["Дата", "Date"],
        "сomment": ["Комментарий", "Сomment"],
        "interval": ["Интервал", "Interval"],
        "result": ["Результат", "Result"],
        "other": ["Другое", "Other"],
        "err": ["Ошибка", "Error"],
        "warning": ["Предупреждение", "Warning"],
        "ask_overwrite": ["Запись с id={} уже существует. Перезаписать?", "Entry with id={} is already exists. Overwrite it?"],
        "path_err": ["Неверно указан каталог для загрузки файлов", "Wrong path to download folder"],
        "ini_err": ['Файл конфигурации поврежден. Пожалуйста, удалите файл "settings.ini" и запустите программу заново',
                    'Configuration file is corrupted. Please, remove "settings.ini and restart the program"'],
    }

    @staticmethod
    def set_language(a_language: Lang):
        Text.language = a_language

    @staticmethod
    def get(a_text_id: str):
        return Text.strings[a_text_id][Text.language]
