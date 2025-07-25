with open("poems.txt") as f:
    content=f.read()
    if("Twinkle" in content):
        print("yes")
    else:
        print("No")    