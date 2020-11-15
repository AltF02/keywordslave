import sqlite3


class DataBase:
    conn: sqlite3.Connection = None

    @staticmethod
    def connect():
        try:
            DataBase.conn = sqlite3.connect('./keyword-bot.db')
        except Exception as e:
            print(e)

    @staticmethod
    def get_keywords() -> list[str, int]:
        if DataBase.conn:
            cursor = DataBase.conn.cursor()
            cursor.execute("SELECT * FROM main.keywords")
            rows = [row for row in cursor.fetchall()]
            cursor.close()
            DataBase.conn.commit()
            return rows
