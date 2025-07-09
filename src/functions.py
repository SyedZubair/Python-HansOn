import requests as rq




def sendRequest(url="https://fake-json-api.mock.beeceptor.com/users"):
    response = rq.get(url)
    return response


def processResponse(response):
    if response.status_code == 200:
        print("Successfull")
        data = response.json()
        print("data in json: ",data)
    return data

#res = sendRequest()
#print(res)


#data = processResponse(res)




# Arguments 
# url, name, age
# 1,2,3

#*(star) Arguments considering as tuple
def sumNumbers(*arg):
    return sum(arg)

#print(sumNumbers(4,5,6,9,8))

#*kwarg

# state : Karnataka, city: Bangalore

def printResponse(**kvargs):
    for key, value in kvargs.items():
        print(f"{key}: {value}")

#printResponse(name="Bharath", age=25)
