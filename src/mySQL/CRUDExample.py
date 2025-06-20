import oracledb
try:
    servername = "localhost:1521/XE"
    username = "NITIN"
    password ="NITIN"
    oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_23_8")
    connection = oracledb.connect(user=username, password =password, dsn=servername)
    uId = int(input("Enter the userid"))
    empName = input("Enter the name")
    Job     = input("Enter the Jom name")
    Salary  = float(input("Enter the salary"))

    cursor = connection.cursor()
    cursor.execute("insert into EMP (EMPNO,ENAME,JOB, SAL) VALUES(:1,:2, :3,:4)", (uId, empName, Job,Salary))
    connection.commit()
    print("Inserted record")
    cursor.execute("SELECT * FROM EMP")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except oracledb.DatabaseError as e:
    print("Databse Exxception",e)
except Exception as ex:
    print("Unexpected errror:",ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    
    if 'connection' in locals():
        connection.close()
    print("Exception connection closed")