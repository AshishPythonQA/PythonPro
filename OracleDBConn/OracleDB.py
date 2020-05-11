import cx_Oracle

# Run the below command in CMD to set the path. instantclient_19_3 file is requried
# in order to connect to oracle DB from Python (and restart the System).
# set ORACLE_HOME=C:\Oracle\instantclient_19_3
# set PATH=%ORACLE_HOME%;%PATH%

class ConnectDB:
    def oracleDB(self):
        global conn
        try:
            conn = cx_Oracle.connect("username/pwd@host:1521/SID")
            # The cursor returns the arrays. i.e columns will be fetched as arrays.
            cursor = conn.cursor()
            cursor.execute("select * from tablename where columnname = 223")
            for row in cursor:
                if str(row[3]).__contains__("String"):
                    print("The length is %s" % len(row))
                    print(row)
        except Exception as e:
            print("Error Occurred : %s" % str(e))
        finally:
            conn.close()


foo = ConnectDB()
foo.oracleDB()
