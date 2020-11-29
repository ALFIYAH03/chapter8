
#chapter8
#latihan6

myData = ["apel", "rambutan", "jeruk"]

def sortStringByChar(data):
    data.sort(key = len, reverse = True)
    print(data)
    
sortStringByChar(myData)
