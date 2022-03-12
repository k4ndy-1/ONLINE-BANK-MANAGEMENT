#menu driven program in python

#add records to bank database
#loan management system in bank
import os
import pickle

#accept data

def InsertRec():
    accno=int(input("Enter the account number:"))
    name=input("Enter the withdrawers name:")
    amt=int(input("Enter the amount withdrawn:"))
    #create the dict.
    rec={"AC/NO":accno,"Name":name,"Amount":amt}
    #Writing the dict
    f=open("loan.dat","wb")
    pickle.dump(rec,f)
    f.close()
    print("SUCCESS!")

def searchrec(r):
	f=open("loan.dat","rb")
	flag=False
	while True:
		try:
			rec=pickle.load(f)
			if rec['AC/NO']==r:
				print("AC/NO",rec["AC/NO"])
				print("Name",rec["Name"])
				print("Amount",rec["Amount"])
				flag=True
		except EOFError:
			break
	if flag==False:
		print("No records")
	f.close()

def updaterec(r,m):
	f=open("loan.dat","rb")
	reclst=[]
	while True:
		try:
			rec=pickle.load(f)
			reclst.append(rec)
		except EOFError:
			break
	f.close()
	for i in range(len(reclst)):
		if reclst[i]['AC/NO']==r:
			reclst[i]['Amount']==m
	f=open("loan.dat","wb")
	for x in reclst:
		picle.dump(x,f)
	f.close()

def readrec():
	f=open("loan.dat","rb")
	while True:
		try:
			rec=pickle.load(f)
			print("Your account number is:",rec['AC/NO'])
			print("Your name is:",rec["Name"])
			print("You have withdrawn:",rec["Amount"])
		except EOFError:
			break
	f.close()

def deleterec(r):
	f=open("loan.dat","rb")
	reclst=[]
	while True:
		try:
			rec=pickle.load(f)
			reclst.append(rec)
		except EOFError:
			break
		f.close()
		f=open("loan.dat","wb")
		for x in reclst:
			if x['AC/NO']==r:
				continue
			pickle.dump(x,f)
		f.close()

while True:
	print('###BANK MANAGEMENT USING FILE HANDLING###')
	print("1.Add the withdrawers details>")
	print("2.To modify the withdrawers detail>")
	print("3.Delete the record>")
	print("4.View the withdrawers details>")
	print("5.Search the records>")
	print("6.EXIT>")
	ch=input("Enter the choice>")
	if ch=='1':
		InsertRec()
	elif ch=='5':
		r=int(input("Account number:"))
		searchrec(r)
		print("###YOUR RECORD IS FOUND!!!###")
	elif ch=='2':
		r=int(input("Enter the accno to be updated:"))
		m=int(input("Enter the new amount:"))
	elif ch=="3":
		r=int(input("Enter the account number:"))
		deleterec(r)
	elif ch=='4':
		readrec()
		print("###HERE ARE ALL THE RECORDS###")
	elif ch=="6":
		print("###THANKS FOR USING ARE LOAN MANAGEMENT SYSTEM! HAVE A GREAT DAY!")
		break


#transanctions and billings in csv format(excel)

#transanctions and billings in csv format(excel)
print("CSV FILES!")
import csv
fh=open("loan.csv","w")
loanwriter=csv.writer(fh)
loanwriter.writerow(['AC/NO','Name','Amount'])
n=int(input("Enter number of customers:"))
for i in range(n):
    print("Transanctions record",(i+1))
    accno=int(input("Enter AC/NO:"))
    name=input("Enter the name:")
    amt=int(input("Enter the amount:"))
    loanrec=[accno,name,amt]
    loanwriter.writerow(loanrec)
fh.close()





    
#end
'''
#mysql python connector
#main

from tkinter import *

window=Tk()
window.geometry("400x400") 
window.title("Employee database")

label=Label(window,text="Hello Welcome to our Employee database",
	relief=RAISED,
	padx=20,
	pady=10,
	compound='up',
	)
label.pack()
window.mainloop()
'''