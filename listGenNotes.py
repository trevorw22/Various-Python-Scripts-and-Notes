# Notes on generators and lists

#These xyz commands do the same thing
xyz = [i for i in range(5)]
print(xyz)

xyz = []
for i in range(5):
	xyz.append(i)
print(xyz)



#A generator expression is the same thing, we just use parenthesis..
#This is not stored in memory as a list, it is stored as a generator object.
xyz = (i for i in range(5))
print(xyz)
#in order to iterate over the range in the generator we use a for loop.
for i in xyz:
	print(i)
#keep in mind that when you want to iterate a generator it will take longer than the above.




input_list = [5,6,5,3,50,6,75,800,60,10,0,3,2,5,45,47]

def div_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False

xyz = (i for i in input_list if div_by_five(i))

#This is how the logic is working for this generator.
# xyz = []
# for i in input_list:
# 	if div_by_five(i):
# 		xyz.append(i)

#we iterate through the generator
# for i in xyz:
# 	print(i)
#we can also do this to iterate the generator, This saves your memory, but is slowerish.
[print(i) for i in xyz]


#
xyz = (print(i) for i in range(5))
for i in xyz:
	i


#embedded one liner for loops
[[print(i,ii) for ii in range(5)] for i in range(5)]
#The same as..
for in in range(5):
	for ii in range(5):
		print(i, ii)


#to list them as tuples.
xyz = [[(i, ii) for ii in range(5)] for i in range(5)]
print(xyz)

#to list them as a list.
xyz = [[[i, ii] for ii in range(5)] for i in range(5)]
print(xyz)

#to turn it into a generator expression.
xyz = ([[i, ii] for ii in range(5)] for i in range(5))
print([i for i in xyz])

#with big lists you'll run out of memory, with big generators you'll run out of time.
