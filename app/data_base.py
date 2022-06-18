import sqlite3

from app import config


def add_thread(thread_id):
    try:
        with sqlite3.connect(config.path_to_db) as db:
            db.execute("INSERT INTO thread "
                       "(thread_id) "
                       "VALUES (?)",
                       [thread_id, ])
            db.commit()
            return True
    except sqlite3.IntegrityError:
        return False
