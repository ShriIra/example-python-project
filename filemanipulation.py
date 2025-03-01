import json

# f = open('a.txt', 'w')
# f.write("Hello\n")
# f.write("This is a sample text\n")
# f.close()

# f = open('a.txt', 'r')
# text = f.read()
# print(json.dumps(text))
# print(text)
# f.close()

# f = open('a.txt', 'a')
# f.write("This is another text\n")
# f.close()
# f.write("I forgot to add something to the text file\n")

# with open('a.txt', 'a') as f:
#     f.write("Yet another line\n")

myDictionary = {'a': 'apple', 'b': "ball"}

# with open('a.json', 'w') as f:
#     f.write(json.dumps(myDictionary))


with open('a.json', 'r') as f:
    jsonData = f.read()

unpackedDs = json.loads(jsonData)

print(unpackedDs)
print(type(unpackedDs))