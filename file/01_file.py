# f = open("file.txt")
# d=f.read()
# print(d)
# f.close()

with open("file.txt") as f:
    print(f.read())
