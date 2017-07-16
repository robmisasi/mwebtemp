import sqlite3 as lite
import requests
import datetime

def get_house_temp():
    r = requests.get('http://misasiweb.com/api/getHouseTemp')
    data = r.json()
    return data["temperature"]

def init_db(db="/home/pi/mweb.db", table="temps"):
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE " + table + "(Time TEXT, Temp INT)")

def insert_temp(db="/home/pi/mweb.db", table="temps"):
    temp = get_house_temp()

    time_str = datetime.datetime.now().isoformat('T')
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO " + table + " VALUES(\"" + time_str + "\" , " + str(temp) + ")")

def print_all_temps(db="/home/pi/mweb.db", table="temps"):
    con = lite.connect(db)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM " + table)
        rows = cur.fetchall()

        for row in rows:
            print(row)
