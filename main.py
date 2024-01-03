
# Online Python - IDE, Editor, Compiler, Interpreter
# Prime number
x=int(input("Enter Number:"))
count=0
for i in range(2,x):
    if(x%i==0):
        count=count+1
if(count==0):
    print("Prime")
else:
    print("Not Prime")