from logging import raiseExceptions


class remoteControl():
    def __init__(self):
        self.channels=["HBO","CNN","abc"]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r=remoteControl()
iter=iter(r)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


