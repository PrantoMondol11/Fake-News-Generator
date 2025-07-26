import random as rn

subjects=["Sarjis","Sakib","Tamim","Pranto"]
actions=["eat","killed","play","murdered"]
objects=["table","Buildings","football","mobile","at school"]
opt="yes"

while(opt=="yes"):
    new1=rn.choice(subjects)
    new2=rn.choice(actions)
    new3=rn.choice(objects)
    
    print(".....................................")
    print( "-: " + new1 +" "+ new2 +" "+new3+"." )
    print(".....................................")

    print("Do you want to generate another one:")
    opt=str(input())
print("Good Bye")
    