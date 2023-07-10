import sqlite3
import os

if(os.path.exists("test.db")):
    pass
else:
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE Debts(name, totalDue, monthlyPay, Interest, Date, flatMonthlyPay)")