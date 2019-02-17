import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def latest():
    conn = sqlite3.connect("sensors.db")
    c = conn.cursor()
    c.execute("SELECT * FROM readings ORDER BY timestamp DESC LIMIT 1")
    alldata = c.fetchall()

    latest = alldata[0]
    latest_temp = latest[2]
    return "Latest temperature is {:.2f}C".format(latest_temp)

if __name__ == '__main__':
    app.run()
