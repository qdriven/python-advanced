# encoding: utf-8
import jsonpickle


class IoThing:
    def __init__(self,name):
        self.name=name

iot=IoThing("test")

result =jsonpickle.encode(iot,unpicklable=False)
print(result)