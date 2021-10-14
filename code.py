i=15
k=4
n=1
print("YOU HAVE ONLY 5 NUM OF GUESSES")
while(k<=4):
    inp=int(input("Enter Num=>"))
    if(inp==i):
        print("You Entered Right Num")
        print("TOOK",n,"GUESSES")
        break
    if(k==0):
        print("NUM OF GUESSES FINISHED")
        break
    elif(inp>i):
        print("Your Num Is Greater , No Of Guesses Left=",k)
        k=k-1
        n=n+1
        continue
    elif(inp<i):
        print("Your Num Is Lesser , No Of Guesses Left=",k)
        k=k-1
        n=n+1
        continue        