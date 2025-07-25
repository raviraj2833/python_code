import random

def game():
    print("you are playing a game:")
    score=random.randint(1,100)
    with open("highScore.txt") as f:
        highScore=f.read()
        if(highScore!=""):
            highScore=int(highScore)
        else:
            highScore=0
                
        print(f"your score is {score}")    
        if(score>highScore):
           with open("highScore.txt","w") as f:
               f.write(str(score))
        
        return score       

game() 
     