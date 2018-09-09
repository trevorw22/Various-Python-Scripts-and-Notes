#Various notes/examples on lists and generators

#Magic 8 ball generator
import random

input()

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])



#Cat name generator

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)



#Lets you type in a pet name and then checks if that name is in the list of pets.

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

# >>> name = 'Zophie'
# >>> name[0]
# 'Z'
# >>> name[-2]
# 'i'
# >>> name[0:4]
# 'Zoph'
# >>> 'Zo' in name
# True
# >>> 'z' in name
# False
# >>> 'p' not in name
# False
# >>> for i in name:
#         print('* * * ' + i + ' * * *')

# * * * Z * * *
# * * * o * * *
# * * * p * * *
# * * * h * * *
# * * * i * * *
# * * * e * * *


# >>> name = 'Zophie a cat'
# >>> newName = name[0:7] + 'the' + name[8:12]
# >>> name
# 'Zophie a cat'
# >>> newName
# 'Zophie the cat'



# # The comma is what lets Python know this is a tuple value. (Unlike some other programming languages,
# # in Python it’s fine to have a trailing comma after the last item in a list or tuple.) Enter the
# # following type() function calls into the interactive shell to see the distinction:
# >>> type(('hello',))
# <class 'tuple'>
# >>> type(('hello'))
# <class 'str'>
# # You can use tuples to convey to anyone reading your code that you don’t intend for that sequence
# # of values to change. If you need an ordered sequence of values that never changes, use a tuple.
# # A second benefit of using tuples instead of lists is that, because they are immutable and their
# # contents don’t change, Python can implement some optimizations that make code using tuples
# # slightly faster than code using lists.

# ❶ >>> spam = [0, 1, 2, 3, 4, 5]
# ❷ >>> cheese = spam
# ❸ >>> cheese[1] = 'Hello!'
#    >>> spam
#    [0, 'Hello!', 2, 3, 4, 5]
#    >>> cheese
#    [0, 'Hello!', 2, 3, 4, 5]

# def eggs(someParameter):
#     someParameter.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)
# #gives us this output
# [1, 2, 3, 'Hello']


# >>> import copy
# >>> spam = ['A', 'B', 'C', 'D']
# >>> cheese = copy.copy(spam)
# >>> cheese[1] = 42
# >>> spam
# ['A', 'B', 'C', 'D']
# >>> cheese
# ['A', 42, 'C', 'D']
# If the list you need to copy contains lists, then use the copy.deepcopy() function instead
# of copy.copy(). The deepcopy() function will copy these inner lists as well.
