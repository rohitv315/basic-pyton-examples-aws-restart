import math

print("number",math.fabs(10))
print("number",math.floor(7.6))
print("num",math.ceil(0.5))
print("string",math.floor('rohit'))

import json

data={
    "name":"John", "age":30, "car":2
    
}
j=json.dumps(data)
print(j)

making os file and delete file directory by using os

import os
print(os.getcwd())
# os.mkdir("/home/ec2-user/environment/rohit")
os.rmdir("/home/ec2-user/environment/rohit")


import os
print(os.getcwd())
os.rmdir("/home/ec2-user/environment/gedam")

get login command to find the file
import os
print(os.getlogin())
os.getlogin()
print(os.getlogin())

string="R o h i t"
string=string.replace(" ","")
print(string)
