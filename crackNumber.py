import os
import random


os.system("clear")

Robot = """                          
"""
def asia():
	op = open("combo.txt","w")
	os.system("clear")
	print(Robot)
	e = "0770"
	for x in range(10000):
		c = "1234567"
		x1 = random.choice(c)
		x2 = random.choice(c)
		x3 = random.choice(c)
		x4 = random.choice(c)
		x5 = random.choice(c)
		x6 = random.choice(c)
		x7 = random.choice(c)
		x8 = random.choice(c)
		x9 = random.choice(c)
		x10 = random.choice(c)
		x11 = random.choice(c)
		x12 = random.choice(c)
		x13 = random.choice(c)
		x14 = random.choice(c)
		b = ""+e+""+x1+x2+x3+x4+x5+x6+x7+":"""+e+""+x1+x2+x3+x4+x5+x6+x7+""
		print(b)
		op.write(b+"\n")

def kor():
	op = open("combo.txt","w")
	os.system("clear")
	print(Robot)
	e = "0750"
	for x in range(100000):
		c = "1234567"
		x1 = random.choice(c)
		x2 = random.choice(c)
		x3 = random.choice(c)
		x4 = random.choice(c)
		x5 = random.choice(c)
		x6 = random.choice(c)
		x7 = random.choice(c)
		x8 = random.choice(c)
		x9 = random.choice(c)
		x10 = random.choice(c)
		x11 = random.choice(c)
		x12 = random.choice(c)
		x13 = random.choice(c)
		x14 = random.choice(c)
		b = ""+e+""+x1+x2+x3+x4+x5+x6+x7+":"""+e+""+x1+x2+x3+x4+x5+x6+x7+""
		print(b)
		op.write(b+"\n")
	

def dr():
		print(Robot)
		os.system('figlet Number')
		print("----------------------------------------")
		print("[1] Asia : pass")
		print("[2] Korek : pass")
		print("----------------------------------------")
		z = int(input("Code ? : "))
		if z==1:
			os.system("clear")
			asia()
		elif z==2:
			os.system("clear")
			kor()
			
dr()
		
	


	

	