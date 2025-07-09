import oracledb
servername = "localhost:1521/XE"
username = "NITIN"
password ="PASS"
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_23_8")
connection = oracledb.connect(user=username, password =password, dsn=servername)
cursor = connection.cursor()
cursor.execute("SELECT * FROM EMP")
rows = cursor.fetchall()
for row in rows:
    print(row)