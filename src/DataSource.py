import sqlite3
from PyQt5.QtCore import QDate

class DataSource():
    
    def __init__(self):
        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()
    
    def saveDebt(self, name, totalDue, monthlyPay, interest, date ):
        self.cur.execute("INSERT INTO Debts VALUES ('"+name+"', '"+totalDue+"', '"+monthlyPay+"', '"+interest+"', '"+date+"', '"+monthlyPay+"')")
        self.con.commit()
    
    def loadDebts(self):
        res = self.cur.execute("SELECT * FROM Debts")
        for i in res.fetchall():
            dateSplit = i[4].split("/")
            qtDate = QDate(int(dateSplit[2]), int(dateSplit[0]), int(dateSplit[1]))
            if qtDate <= QDate.currentDate():
                if(int(i[3]) == 0):
                    self.cur.execute("UPDATE Debts SET monthlyPay = flatMonthlyPay WHERE name = '"+i[0]+"'")
                else:
                    self.cur.execute("UPDATE Debts SET monthlyPay = '"+str(int(i[2]) + int(i[5]))+"' WHERE name = '"+i[0]+"'")
                self.con.commit
                self.cur.execute("UPDATE Debts SET Date = '"+qtDate.addMonths(1).toString("MM/dd/yyyy")+"' WHERE name = '"+i[0]+"'")
                self.con.commit()
        res = self.cur.execute("SELECT * FROM Debts")
        return res.fetchall()

    def makePayment(self, name, amountRemain, amountPaidToday):
        self.cur.execute("UPDATE Debts SET totalDue = '"+amountRemain+"', monthlyPay = '0' WHERE name = '"+name+"'")
        self.con.commit()
        try:
            self.cur.execute("SELECT * FROM '"+name+"'")
        except:
            self.cur.execute("CREATE TABLE '"+name+"'(payment, date)")
        self.cur.execute("INSERT INTO '"+name+"' VALUES('"+amountPaidToday+"', '"+QDate.currentDate().toString("MM/dd/yyyy")+"')")
        self.con.commit()
    
    
    def makePartialPayment(self, name, amountRemain, amountPayed, amountPaidToday):
        self.cur.execute("UPDATE Debts SET totalDue = '"+amountRemain+"', monthlyPay = '"+amountPayed+"' WHERE name = '"+name+"'")
        try:
            self.cur.execute("SELECT * FROM '"+name+"'")
        except:
            self.cur.execute("CREATE TABLE '"+name+"'(payment, date)")
        self.con.commit()
        self.cur.execute("INSERT INTO '"+name+"' VALUES('"+amountPaidToday+"', '"+QDate.currentDate().toString("MM/dd/yyyy")+"')")
        self.con.commit()

    def deleteDebt(self, name):
        self.cur.execute("DELETE FROM Debts WHERE name = '"+name+"'")
        self.con.commit()

    def grabPayments(self, name):
        return self.cur.execute("SELECT * FROM '"+name+"'")
