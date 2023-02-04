Dependencies-
Make sure you have installed all the requirements
(which are in the requirements.txt file).

How to run-
An example how to run magic list without class-
a = MagicList()
a[0] = 5
print(a)
a[1] = 7
print(a)

An example how to run magic list with class-
first, define a class:
@dataclass
class Person:
    age: int = 1

next, add the following code:
b = MagicList(class_type=Person)
b[0].age = 6
print(b)
b[1].age = 8
print(b)

Exceptions-
Please note that if you insert indexes that are'nt continuity,
an exception will raise.
For example, an exception will raise if you will add the following code
a[0] = 5
print(a)
a[2] = 7
print(a)

Tests-
In 'Tests' directory there is a pytest file that you can with