import hashlib

num=-1
with open("input.txt") as fp:
    secret_key=fp.readline()

while True:
    num+=1
    data=secret_key+str(num)
    res=hashlib.md5(data.encode())
    if res.hexdigest()[0:6] == '000000':
        print(num)
        break
