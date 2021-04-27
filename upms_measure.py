from enum import IntEnum
from text import Text


class UpmsMeasure:
    class MeasureType(IntEnum):
        MECH_STOPWATCH = 1
        ELEC_STOPWATCH = 2
        CLOCK = 3

    TYPE_TO_STR = {
        MeasureType.MECH_STOPWATCH: Text.get("m_stopwatch"),
        MeasureType.ELEC_STOPWATCH: Text.get("e_stopwatch"),
        MeasureType.CLOCK: Text.get("clock"),
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
        return "id: {}, "\
               "user_id: {}, "\
               "type: {}, "\
               "date: {}, "\
               "comment: {}, "\
               "interval: {}, "\
               "result: {}, "\
               "other: {}".format(self.id, self.user_id, self.type,
                                  self.date, self.comment, self.interval, self.result, self.other)

    def __str__(self):
        return "{}: {}, " \
               "{}: {}, " \
               "{}: {}, " \
               "{}: {}, " \
               "{}: {}, " \
               "{}: {}, " \
               "{}: {}, ".format(Text.get('id'), self.id, Text.get('uid'), self.user_id,
                                 Text.get('type'), UpmsMeasure.TYPE_TO_STR[self.type],
                                 Text.get('date'), self.date, Text.get('comment'), self.comment,
                                 Text.get('interval'), self.interval, Text.get('result'), self.result)
