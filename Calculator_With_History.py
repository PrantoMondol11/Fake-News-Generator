f = open("History.txt", "a")
print("Welcome To My Calculator App!")
print("............................")
print("Enter Your Equation Here:")
eq=str(input())
res=str(eval(eq))

his=eq + "=" + res
print(his)
f.write(his)