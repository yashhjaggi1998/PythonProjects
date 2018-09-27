import random
import time

def generateSelector(random_obj):
	a = random.randint(1,4)
	element = generateElement(a,random_obj)
	return element

def generateElement(a,random_obj):
	if a == 1:
		#lower
		return random_obj.choice(lower)
		
	elif a == 2:
		#upper
		return random_obj.choice(upper)
		
	elif a == 3:
		#number
		return random_obj.choice(numbers)
		
	else:
		#symbol
		return random_obj.choice(symbols)
		

lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','@','#','$','%','&']

#defining main in this manner executes it only when file is executed and not when imported by some other file
if __name__ == '__main__':
	random_obj = random.SystemRandom() #provides a cryptographically secure number generator
	#ranom_obj returns a pointer

	print()
	print("Welcome to Password Generator!!!")
	print("Sit back and relax untill we generate a paasword for you...")
	time.sleep(2)
	print()
	print("Your generated password is.... " , end=" ")
	for i in range(8):
		element = generateSelector(random_obj)
		print(element,end="")
	print()
