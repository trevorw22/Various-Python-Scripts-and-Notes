#Some Fibonacci Number Sequence examples to practice iteration, recursion, and generators

#Iterative example, can use both pos and neg numbers
def fibiter(n, x = [0,1]):
    for i in range(abs(n)-1):
        x = [x[1], sum(x)]
    return x[1]*pow(-1, abs(n) - 1) if n < 0 else x[1] if n else 0

for i in range(-100, 100):
    print(fibiter(i))


#Recursive example
def fibRec(n):
    if n < 2:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)

for i in range(0, 50):
    print(fibRec(i))


#Generator example
def fibGen(n):
    a, b = 0, 1
    while n>0:
        yield a
        a, b, n = b, a+b, n-1

print([i for i in fibGen(100)])
