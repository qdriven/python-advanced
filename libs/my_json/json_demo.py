# encoding: utf-8
# https://realpython.com/python-json/
# load json
import json

import jsonpickle

with open('demo.json') as json_file:
    json_result = json.load(json_file, encoding='utf-8')

print(json_result)
print(type(json_result))

from collections import namedtuple


def custom_object_hook(json_data):
    return namedtuple('X', json_data.keys())(*json_data.values())


with open('demo.json') as json_file:
    json_result = json.load(json_file, encoding='utf-8', object_hook=custom_object_hook)

print(json_result.firstName)

import json
from collections import namedtuple
from json import JSONEncoder


class Student:
    def __init__(self, rollNumber, name, marks):
        self.rollNumber, self.name, self.marks = rollNumber, name, marks


class Marks:
    def __init__(self, english, geometry):
        self.english, self.geometry = english, geometry


class StudentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())


marks = Marks(82, 74)
student = Student(1, "Emma", marks)

# dumps() produces JSON in native str format. if you want to writ it in file use dump()
studentJson = json.dumps(student, indent=4, cls=StudentEncoder)
print("Student JSON")
print(studentJson)

# Parse JSON into an object with attributes corresponding to dict keys.
studObj = json.loads(studentJson, object_hook=customStudentDecoder)

print("After Converting JSON Data into Custom Python Object")
print(studObj.rollNumber, studObj.name, studObj.marks.english, studObj.marks.geometry)

# dumps() produces JSON in native str format. if you want to writ it in file use dump()
studentJsonData = json.dumps(student, indent=4, cls=StudentEncoder)
print("Student JSON")
print(studentJsonData)

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace
# Parse JSON into an custom Student object.
studObj = json.loads(studentJsonData, object_hook=lambda d: Namespace(**d))
print("After Converting JSON Data into Custom Python Object using SimpleNamespace")
print(studObj.rollNumber, studObj.name, studObj.marks.english, studObj.marks.geometry)


marks = Marks(82, 74)
student = Student(1, "Emma", marks)

print("Encode Object into JSON formatted Data using jsonpickle")
studentJSON = jsonpickle.encode(student)
print(studentJSON)

print("Decode and Convert JSON into Object using jsonpickle")
studentObject = jsonpickle.decode(studentJSON)
print("Object type is: ", type(studentObject))

print("Student Details")
print(studentObject.rollNumber, studentObject.name, studentObject.marks.english, studentObject.marks.geometry)