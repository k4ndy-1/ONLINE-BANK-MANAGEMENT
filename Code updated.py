
import pickle

import pymysql as pym

#binary

def InsertRec():
		
	cus={}
	cusfile=open("cus.dat","wb")
	ans='y'
	while ans=='y':
		ano=int(input("Enter the account number:"))
		name=input("Enter the name:")
		cus["AccNo"]=ano
		cus["Name"]=name
		pickle.dump(cus,cusfile)
		ans=input("Yes(y)/no(n)?")
	cusfile.close()
			


def readrec():
	f=open("cus.dat","rb")
	while True:
		try:
			rec=pickle.load(f)
			print("Your account number is:",rec['AccNo'])
			print("Your name is:",rec["Name"])
			
		except EOFError:
			break
	f.close()


def searchfile(r):
	f=open("cus.dat","rb")
	
	
	flag=False
	while True:
		
		try:
			rec=pickle.load(f)
			if rec["AccNo"]==r:
				print("Account number:",rec['AccNo'])
				print("Name:",rec["Name"])
				flag=True
		except EOFError:
			break
	if flag==False:
		print("NOT FOUND!")
	f.close()


def deleterec(r):				#
	f=open("cus.dat","rb")
	reclst=[]
	while True:
		try:
			rec=pickle.load(f)
			reclst.append(rec)
		except EOFError:
			break
	f.close()
	f=open("cus.dat","wb")
	for x in reclst:
		if x["AccNo"]==r:
			print("Deleted!")
			continue
		pickle.dump(x,f)
		
	f.close()

def update(r,m):
	f=open("cus.dat","rb")
	reclst=[]
	while  True:
		try:
			rec=pickle.load(f)
			reclst.append(rec)
		except EOFError:
			break
	f.close()
	f=len([reclst])
	for i in range(f):
		if reclst[i]['AccNo']==r:
			reclst[i]['Name']==m
	f=open("cus.dat","wb")
	for x in reclst:
		pickle.dump(x,f)
	f.close()






#part 2
import csv 



def readcsv():
	with open("cus.csv","r",newline='\r\n') as csvf:
		file=csv.reader(csvf)
		for row in file:
			if len(row)!=0:
				print(row)
	csvf.close()

def insertcsv():
	ans='y'
	while ans=="y":
		Name=input("Enter your name:")
		Amount=int(input("Enter amount you want to deposit:"))
		Account_Type=input("Select type of account(f,c or s):")
		time=int(input("Enter the time(in years):"))

		if Account_Type=="f":
			interest=Amount*6/100*time
			Net_Balance=interest+Amount
		elif Account_Type=='s':
			interest=Amount*4/100*time
			Net_Balance=interest+Amount
		elif Account_Type=='c':
			interest=Amount
			Net_Balance=interest+Amount
		with open("cus.csv","a",newline='\r\n') as csvfile:
			writer=csv.writer(csvfile)
			
			writer.writerow([Name,Amount,Account_Type,time,Net_Balance])
			ans=input("Want more(y or n?)")
		csvfile.close()		

def searchcsv(searchitem):
 	
	with open("cus.csv","r") as csvfile:
		
		reader=csv.reader(csvfile)
		for row in reader:
			for field in row:
				if field==searchitem:
					print(row)
				else:
					pass
		
	csvfile.close()
def updatecsv():						#
	f=open("cust.csv",'r',newline='\r')
	Name=input("Enter name of record to be updated:")
	found=0
	r=csv.reader(f)
	nrec=[]
	for rec in r:
		if rec[0]==Name:
			print("Current record is:",rec)
			rec[0]=input("Enter a new name:")
			print("Updated record is",rec)
			found=1
		nrec.append(rec)

	if found==0:
		print("Sorry not found..")
		f.close()
	else:
		f=open('cust.csv','w',newline='\r')
		w=csv.writer(f)
		w.writerows(nrec)
		f.close()





#mysql code

import mysql.connector
import pymysql
mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank" )
mycursor=mydb.cursor()
def store(Accno,nam,bal,typ="Fixed",tim=0):
    insert="INSERT INTO CUSTOMERS(Accno,nam,bal,typ,tim) VALUES(%s,%s,%s,%s,%s)"
    val=(Accno,nam,bal,typ,tim)
    mycursor.execute(insert,val)
    mydb.commit()

def update (Accno,nam,bal,typ="Fixed",tim=0):
    update="UPDATE CUSTOMERS SET nam= %s  WHERE Accno=%s"
    updte=(nam,Accno)
    mycursor.execute(update,updte)
    update="UPDATE CUSTOMERS SET bal= %s  WHERE Accno=%s"
    updte=(nam,bal)
    mycursor.execute(update,updte)
    update="UPDATE CUSTOMERS SET tim= %s  WHERE Accno=%s"
    updte=(tim,Accno)
    mycursor.execute(update,updte)
    mydb.commit()



def delete(Accno):
	delet="DELETE FROM CUSTOMERS WHERE Accno=%s"
	record=(Accno,)
	mycursor.execute(delet,record)
	mydb.commit()

#reports 

def reportsbin():
	f=open("cus.dat","rb")
	try:
		print("ALL YOUR BINARY RECORDS")
		while True:
			stu=pickle.load(f)
			print(stu)
	except EOFError:
		f.close()
def reportscsv():
	with open("cus.csv",'r',newline='\r\n') as fh:
		creader=csv.reader(fh)
		print("ALL YOUR CSV RECORDS")
		for rec in creader:
			print(rec)
                        


def reportsql():
	mycon=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank" )
	cursor=mycon.cursor()
	cursor.execute("select * from customers")
	data=cursor.fetchall()
	count=cursor.rowcount

	print("ALL YOUR SQL RECORDS",count)

	for row in data:
		print(row)


#end


#menu

while True:
	print("************************************************************************************")
	print("========== WELCOME TO OUR ONLINE BANKING SYSTEM ===================")
	print("************************************************************************************")
	print("============ 1.CUSTOMERS ============================")
	print("============ 2.ACCOUNTS================================")
	print("============ 3.TRANSANCTIONS====================================")
	print("============ 4.REPORTS============================")
	print("============ 5.EXIT====================================")
	print("=============6.GRAPHS FOR THE DATA=======================")
	
	print("************************************************************************************")

	ch=int(input("Enter choice:"))

	if ch==1:
		while True:
			print("************************************************************************************")
			print("========== WELCOME TO OUR ONLINE BANKING SYSTEM ===================")
			print("************************************************************************************")
			print("============ 1.Add the withdrawers details ============================")
			print("============ 2.To update the details  =================================")
			print("============ 3.Delete the record ====================================")
			print("============ 4.View the withdrawers details ============================")
			print("============ 5.Search the records ====================================")
			print("============ 6.Exit  =========================")
			print("************************************************************************************")
			ch=input("Enter the choice>")
			if ch=='1':
				InsertRec()
			elif ch=='5':
				r=int(input("Account number:"))
				searchfile(r)
				print("======== YOUR RECORD IS FOUND!!! =========")
			elif ch=='2':
				r=int(input("Enter the account number:"))
				m=input("Enter the name:")
				update(r,m)
			elif ch=="3":
				r=int(input("Enter the account number:"))
				deleterec(r)
			elif ch=='4':
				readrec()
				print("========= HERE ARE ALL THE RECORDS =============")
			elif ch=="6":
				print("=========== THANKS FOR USING ARE LOAN MANAGEMENT SYSTEM! HAVE A GREAT DAY! ========")
				break


	if ch==2:
		while True:
			print("**********************************************************************************")
			print("========== WELCOME TO OUR ONLINE BANKING SYSTEM ===============")
			print("******************************************************************************")
			print("============ 1.Put money in accounts ===========================")
			print("****************************************************************************")
			print("*********************SAVINGS = 4% ROI**************************************")
			print("******************CURRENT = 1% ROI*******************************************")
			print("******************FIXED   = 2% ROI*********************************************")
			print("*************************************************************************************")
			print("============ 2.To update the details  ==================================")
			print("============ 3.Search the record details ===============================")
			print("============ 4.View the clients details ================================")
			print("============ 5.Exit ======================================")
			print("***************************************************************************************")
			ch=input("Enter the choice>")

			if ch=="1":
				insertcsv()
			elif ch=='2':
				insertcsv()
			elif ch=="3":
				searchitem=input("Enter item to be seached for:")
				searchcsv(searchitem)
			elif ch=="4":
				readcsv()
			elif ch=="5":
				print("=========== THANKS FOR USING ARE LOAN MANAGEMENT SYSTEM! HAVE A GREAT DAY! ========")
				break

	if ch==3:
		while True:
			print("**********************************************************")
			print("=============== MYSQL TABLE MANAGEMENT ================")
			print("**********************************************************")
			print("============ 1.CREATE TABLE ===========================")
			print("============ 2.UPDATE TABLE ===========================")
			print("============ 3.DELETE TABLE ===========================")
			print("============ 4.EXIT THE PROGRAM =======================")
			print("**********************************************************")
			print("***WE DONT CHANGE ACCOUNT TYPE ENTER DETAILS CAREFULLY****")
			print("**********************************************************")
			print("**********************************************************")
			ch=input("Enter the choice>")

			if ch=="1":
				Accno=int(input("Enter your account number:"))
				nam=input('Enter your name:')
				bal=int(input("Enter the amount of money:"))
				typ=input("Enter account type:(fixed,current,deposit,savings):")
				tim=int(input("Enter the time for which money is kept:"))
				store(Accno,nam,bal,typ,tim)
			elif ch=='2':
				Accno=int(input("Enter your account number:"))
				nam=input('Enter your name:')
				bal=int(input("Enter the amount of money:"))
				tim=int(input("Enter the time for which money is kept:"))
				update(Accno,nam,bal,tim)

			elif ch=='3':
				Accno=int(input("Enter account number to be deleted:"))
				delete(Accno)

			elif ch=="4":
				print("=========== THANKS FOR USING ARE LOAN MANAGEMENT SYSTEM! HAVE A GREAT DAY! ========")
				break

	if ch==4:
		reportscsv()
		reportsql()
		reportsbin()
			

	if ch==5:
		break

#art integration
	if ch==6:
		import pandas as pd
		import matplotlib.pyplot as plt

		df = pd.read_csv('cus.csv')
		x=df['Name']
		y=df['Amount']
		plt.xlabel('Name',fontsize=18)
		plt.ylabel('Amount(₹)',fontsize=20)
		plt.bar(x,y)

		plt.show()
