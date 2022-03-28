def Push(stk,item):
    stk.append(item)
    top=len(stk)-1

def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Display(stk):
    if isEmpty(stk):
        if stk==[]:
            return True
        else:
            top=len(item)-1
            print(item[top],"<-top")
            for a in range(top-1,-1,-1):
                print(item[a])

#main

Status=[]
top=None

while True:
    
    ch=int(input("Enter your choice:"))
    if ch==1:
        PhoneNo=int(input("Enter your number:"))
        EmployName=input("Enter your name:")
        item=(PhoneNo,EmployName)
        Push(Status,item)
    

    elif ch==2:
        Display(Status)
