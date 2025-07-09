import requests as rq
endpointurl = "https://fake-json-api.mock.beeceptor.com/users"
response = rq.get(endpointurl)
print("Response Code: ",response.status_code)

if response.status_code == 200:
    print("Successfull")
    data = response.json()
    print("data in json: ",data)

    for d in data:
        print("inside data element d ", d['country'])
        cursor.execute("insert into EMP (EMPNO,ENAME) VALUES(:1,:2)", (d['id'], d['name']))
        connection.commit()
        print("Inserted record")

else:
    print("Not Successfull, check with your admin!")

'''
inside data element d  {
    'id': 10, 
    'name': 'Karine Collins', 
    'company': 'Lang and Sons', 
    'username': 'Shany_Waelchi42', 
    'email': 'Crystal.Rempel90@gmail.com', 
    'address': '922 Barrows Rest', 
    'zip': '06343', 
    'state': 'Arizona', 
    'country': 'Bahrain', 
    'phone': '307-343-7407 x60566', 
    'photo': 'https://json-server.dev/ai-profiles/52.png'
    }'''