from text import Text


class UpmsMeasure:
    TYPE_TO_STR = {
        1: Text.get("e_stopwatch"),
        2: Text.get("m_stopwatch"),
        3: Text.get("clock"),
    }

    def __init__(self, a_id: int, a_user_id: int, a_type: int, a_date: str, a_comment: str, a_interval: str,
                 a_result: str, a_other: str):
        self.id = int(a_id)
        self.user_id = int(a_user_id)
        self.type = int(a_type)
        self.date = a_date
        self.comment = a_comment
        self.interval = a_interval
        self.result = a_result
        self.other = a_other

    def __eq__(self, other):
        if isinstance(other, UpmsMeasure):
            return self.id == other.id and \
                   self.user_id == other.user_id and \
                   self.type == other.type and \
                   self.date == other.date and \
                   self.comment == other.comment and \
                   self.interval == other.interval and \
                   self.result == other.result and \
                   self.other == other.other
        else:
            return NotImplemented

    def __repr__(self):
        return f"id: {self.id}, "\
               f"user_id: {self.user_id}, "\
               f"type: {self.type}, "\
               f"date: {self.date}, "\
               f"comment: {self.comment}, "\
               f"interval: {self.interval}, "\
               f"result: {self.result}, "\
               f"other: {self.other}"

    def __str__(self):
        return f"{Text.get('id')}: {self.id}, " \
               f"{Text.get('uid')}: {self.user_id}, " \
               f"{Text.get('type')}: {UpmsMeasure.TYPE_TO_STR[self.type]}, " \
               f"{Text.get('date')}: {self.date}, " \
               f"{Text.get('сomment')}: {self.comment}, " \
               f"{Text.get('interval')}: {self.interval}, " \
               f"{Text.get('result')}: {self.result}, " \
