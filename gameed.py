import msvcrt
import time

first=5 #number of clicks
count=0 
flag=0 #using to reduce lines of code 
y=0 #just to make count=0 once 
print "press enter"
raw_input()
s_time=time.time()

def down():
	flag=1
	count2=0
	while(flag==1):
		key=msvcrt.getch()
		if key=='s':
			print 17*' ',
			print"I"
			count2=count2+1
		else:
			print "game over"
			break	
		if count2==first:
			flag=2
			print "move right"
			right(flag)

def right(flag):
	count=0
	y=0
	rd=0
	while(flag==0 or flag==2):
		if(flag==2 and y==0):
			count=0
			y=1
		key=msvcrt.getch()
		if key=='d':
			count=count+1
			if (flag==2 and rd==0):
				print 17*' ',
				rd=1
			print"-->",
			if count==first:
				print "move down"
				if flag==0:
					flag=1
					down()
				if flag==2:
					time_elap=time.time()-s_time
					print "congrats you have finished the game"
					print "time taken is " +str(round(time_elap))
					x=raw_input("enter to close")
		else:
			print "game over"
			break

while(1):
	right(flag)
