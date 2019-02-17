from datetime import datetime
import requests
import sqlite3
import time
import random

if __name__ == '__main__':
    conn = sqlite3.connect('sensors.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS readings ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            timestamp VARCHAR(255),
            temperature DOUBLE(2,2),
            uploaded TINYINT)''')
    conn.commit()
    conn.close()

    # Run readings
    while(True):
        temperature = random.randint(0, 2000) / 100
        conn = sqlite3.connect('sensors.db')
        c = conn.cursor()
        c.execute('''INSERT INTO readings VALUES ( NULL, 
                "{}",
                {:.2f},
                0 )'''.format(datetime.now(), temperature))
        conn.commit()
        conn.close()

        time.sleep(5)
