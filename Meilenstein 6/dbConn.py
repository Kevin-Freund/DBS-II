import pyodbc

def getConn ():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=141.56.2.45;"
                          "Database=iw21s83794;"
                          "uid=s83794;pwd=s83794")
    return cnxn
