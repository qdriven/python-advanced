# encoding: utf-8
from attr import attr


@attr.s
class SomeClass(object):
    a_number = attr.ib(default=22)
    list_of_numbers = attr.ib(factory=list)

    def hard_math(self, another_number):
        return self.a_number + sum(self.list_of_numbers) * another_number

sc =SomeClass(a_number=12,lsit_of_numbers=[1,2,3])

C = attr.make_class("C", ["a", "b"])
print(c)