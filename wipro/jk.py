#json module
import json
#imp ques strformat
name=input("Enter your name")
age=int(input("eter your age"))
data={"name":name,"age":age}
stringify_json=json.dumps(data)
print("Serialised data of JSON",stringify_json)
