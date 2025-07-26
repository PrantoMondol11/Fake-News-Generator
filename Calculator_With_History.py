print("Welcome To My Calculator App!")
print("............................")

while (True):
    f = open("History.txt", "a")
    print("\n1.Calculate\n2.History\n3.Clear\n4.Exit")
    
    opt=int(input())
    


    if opt==1:
        print("Enter Your Equation Here:")
        eq=str(input())
        res=str(eval(eq))  
        his=eq + "=" + res
        print("Result:" + his)
        f.write(his+"\n")  
    elif opt==2:
        f = open("History.txt", "r") 
        content=f.read()
        if content == "":
            print("Nothing to show!")
        else:
            print("History:")
            print("..........................")
            print(content)
    elif opt==3:
        f.seek(0)
        f.truncate()
        print("Cleared")
    elif opt==4:
        break
    else:
        print("Invalid Option!")



