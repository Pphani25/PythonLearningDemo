# with open("file.txt") as reader:
#     reader.read()
try:
    with open("file.txt") as file:
        file.read()
except Exception as e:
    print(e)