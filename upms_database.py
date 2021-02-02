from typing import Optional, List
import sqlite3

from upms_measure import UpmsMeasure


class UpmsDatabase:
    def __init__(self, a_database_filename: str):
        self.conn = sqlite3.connect(a_database_filename)
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS measures (
                id integer PRIMARY KEY,
                user_id integer,
                type integer,
                date text,
                comment text,
                interval text,
                result text,
                other text
            )"""
        )

    def get(self, a_id: int) -> Optional[UpmsMeasure]:
        self.cursor.execute("SELECT * FROM measures WHERE id=?", (a_id,))
        rows = self.cursor.fetchall()
        if rows:
            return UpmsMeasure(*rows[0])
        else:
            return None

    def get_all(self) -> List[UpmsMeasure]:
        self.cursor.execute("SELECT * FROM measures ORDER BY id")
        return [UpmsMeasure(*row) for row in self.cursor.fetchall()]

    def add(self, a_upms_measure: UpmsMeasure):
        with self.conn:
            self.cursor.execute("""INSERT INTO measures (id, user_id, type, date, comment, interval, result, other) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (a_upms_measure.id, a_upms_measure.user_id, a_upms_measure.type,
                                                     a_upms_measure.date, a_upms_measure.comment, a_upms_measure.interval,
                                                     a_upms_measure.result, a_upms_measure.other))

    def update(self, a_upms_measure: UpmsMeasure):
        with self.conn:
            self.cursor.execute(f"UPDATE measures SET user_id=?, type=?, date=?, comment=?, interval=?, result=?, other=?"
                                f"WHERE id={a_upms_measure.id}", (a_upms_measure.user_id, a_upms_measure.type,
                                                                  a_upms_measure.date, a_upms_measure.comment,
                                                                  a_upms_measure.interval, a_upms_measure.result,
                                                                  a_upms_measure.other))

    def remove(self, a_id: UpmsMeasure):
        with self.conn:
            self.cursor.execute(f"DELETE FROM measures WHERE id={a_id}")
