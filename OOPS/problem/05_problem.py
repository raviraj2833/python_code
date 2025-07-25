from random import randint
class train:
    
    def __init__(self,trainNo):
       self.trainNo=trainNo
    
    def book(self,fro,to):
      print(f"ticket is booked in train no:{self.trainNo} from {fro} to {to}")
    
    def getFair(self,fro,to):
        print(f"Ticket fare in train no:{self.trainNo} from {fro} to {to} is {randint(223,1000)}")
    
    
    def getStatus(self):
        print(f"TrainNo {self.trainNo} is running successfully on time")
   
t=train(23455)
t.book("delhi","ranchi")
t.getFair("delhi","ranchi")
t.getStatus()