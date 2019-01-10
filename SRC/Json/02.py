#! 3
# coding:utf-8

import json

student = {
    "name": "zhang san ",
    "age": 20,
    "set": "F"
}

with open("stu.json","w") as f:
    json.dump(student, f )

with open("stu.json", "r") as f:
    stu_json = json.load(f)
    print(stu_json)