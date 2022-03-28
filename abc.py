#editing csv

import csv

ModList=[]

#1

with open('cus.csv','r') as file:
	myFile=csv.reader(file)
	for row in myFile:
		ModList.append(row)



for i in range(len(ModList)):
	print('Row'+str(i)+':'+str(ModList[i]))

editRow=int(input("\n Which details do you want to change (1 to"+str(len(ModList)-1)+":"))




for i in range(len(ModList)):
	print("Row"+str(i)+":"+str(ModList[i])


	