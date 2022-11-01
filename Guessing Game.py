import random as rand
import math as m
lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))
num=rand.randint(lower,upper)
print("\nYou have",round(m.log(upper-lower+1,2)),"chances to guess the intger. Good luck!\n")
count=0
while (count<m.log(upper-lower+1,2)):
	count+=1
	guess=int(input("Enter your guess: "))
	if num==guess:
		print("\nCongratulations you did it in",count,"tries!")
		break
	elif num>guess:
		print("Your guess is too small.")
	elif num<guess:
		print("Your guess is too big.")
flag=True if (num==guess) else False
if flag==False:
	print("\nThe number is:",num)
	print("\nBetter luck next time!\n") 