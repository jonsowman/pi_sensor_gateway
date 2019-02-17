import sqlite3
import time
from datetime import datetime
import json

if __name__ == '__main__':
    conn = sqlite3.connect('sensors.db')
    c = conn.cursor()
    c.execute('SELECT * FROM readings WHERE uploaded = 0 ORDER BY timestamp ASC LIMIT 20')
    rows = c.fetchall()

    # Upload rows to server
    print("Uploading {} rows".format(len(rows)))
    print("POST: {}".format(json.dumps(rows)))
    success = True

    # Mark the rows as uploaded
    if success and len(rows) > 0:
        for row in rows:
            c.execute('UPDATE readings SET uploaded = 1 WHERE id = {}'.format(row[0]))
            conn.commit()

    # Prune old uploaded rows
    c.execute("DELETE FROM readings WHERE uploaded = 1".format(row[0]))
    conn.commit()

    c.close()
    time.sleep(60)
