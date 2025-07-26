print("Welcome To My Calculator App!")
print("............................")

while (True):
    print("\n1.Calculate\n2.History\n3.Clear\n4.Exit")
    
    opt=int(input())
    


    if opt==1:
        print("Enter Your Equation Here:")
        eq=str(input())
        res=str(eval(eq))  
        his=eq + "=" + res
        print("Result:" + his)
        f = open("History.txt", "a")
        f.write(his+"\n") 
        f.close() 
    elif opt==2:
        f = open("History.txt", "r") 
        lines = f.readlines()
        if not lines:
            print("Nothing to show!")
        else:
            lines=reversed(lines)
            print("History:")
            print("..........................")
            for line in lines:
                
                print(line,end="")
        f.close()
    elif opt==3:
        f=open("History.txt","a")
        f.seek(0)
        f.truncate()
        print("Cleared")
        f.close()
    elif opt==4:
        break
    else:
        print("Invalid Option!")



