def execute():
	numbers = open("ex01/numbers.txt", "r")
	numberlist = (numbers.read()).split(",")
	for i in numberlist:
		print (i)

if __name__ == '__main__':
	execute()