import sqlite3
import icecream as ic

from sqlalchemy import Text


def create_sqlite_session(db_file) -> sqlite3.Connection:
    session = None
    try:
        session = sqlite3.connect(db_file)
        return session
    except sqlite3.Error as error:
        print(error)

def cursor_to_list_of_dict(cursor) -> list:
    list_of_dicts = []
    for row in cursor:
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]

        list_of_dicts.append(d)
    return list_of_dicts





