import json
from json import JSONEncoder

class Animal:
    def __init__(self, name):
        self.name = name

pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('c') }

# print(json.dumps(pythonDict))

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        else:
            return super().default(o)


print(json.dumps(pythonDict, cls=AnimalEncoder))
