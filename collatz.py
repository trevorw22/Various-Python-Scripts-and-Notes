#Find the Collatz Sequence of an integer

def collatz(number):
	while number != 1:
		if number % 2 == 0:
			number = number // 2
			print(number)
		else:
			number = 3 * number + 1
			print(number)

print("Type an integer: ")
num = int(input())
collatz(num)
