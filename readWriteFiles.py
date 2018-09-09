# Reading and Writing files and directories
# Read the Docs: https://docs.python.org/3/library/os.path.html

# os.path.join() allows us to build paths that will work on any OS 
import os
os.path.join('usr', 'bin', 'spam')
# returns: 'usr\\bin\\spam'
# on linux or OS X it would have returned usr/bin/spam


# the following example joins names from a list of filenames to the end of a folder’s name:
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('C:\\Users\\t1337', filename))
# C:\Users\t1337\accounts.txt
# C:\Users\t1337\details.csv
# C:\Users\t1337\invite.docx


# current working directory and change directory as strings
import os
os.getcwd()
# 'C:\\Users\\t1337\\Documents\\automation'
os.chdir('C:\\Windows\\System32')
os.getcwd()
# 'C:\\Windows\\System32'


# you get an error if you try to change to a dir that doesn't exist
os.chdir('C:\\ThisFolderDoesNotExist')
# FileNotFoundError: [WinError 2] The system cannot find the file specified:


# Create new folders with os.makedirs()
import os
os.makedirs('C:\\delicious\\walnut\\waffles')
# os.makedirs() will create any intermediate folders so that the full path exists



# convert a relative path to an absolute one with
os.path.abspath(path)

# the following will return True if the argument is an absolute path and False if it's relative
os.path.isabs(path)

# to return a string of a relative path from the start path to path. Default start is pwd
os.path.relpath(path, start)
# examples
os.path.abspath('.')
'C:\\Python34'
os.path.abspath('.\\Scripts')
'C:\\Python34\\Scripts'
os.path.isabs('.')
False
os.path.isabs(os.path.abspath('.'))
True

# relative path examples
os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'
os.getcwd()
'C:\\Python34'


# Dir name and Base name
# C:\Windows\System32\calc.exe   The Dir name is C:\Windows\System32 and the Base name is calc.exe
path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)
'calc.exe'
os.path.dirname(path)
'C:\\Windows\\System32'

# to split the path's dir name and base name together use os.path.split() to get a tuple value with both strings
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')
# the following does the same thing, but os.path.split() is a greate shortcut if you need both values
(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
('C:\\Windows\\System32', 'calc.exe')


# to split the file path into a list of strings of each folder use os.path.sep
calcFilePath.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']

# on OS X and Linux there will be a blank string at the start of the returned list:
'/usr/bin'.split(os.path.sep)
['', 'usr', 'bin']


# Finding folder and file sizes
os.path.getsize(path) # this returns the size in bytes of the file
os.listdir(path) # this returns a list of filename strings for each file in the path argument

os.path.getsize('C:\\Windows\\System32\\calc.exe')
776192

os.listdir('C:\\Windows\\System32')
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--snip--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

# to find the total size of files in this directory use the following..
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
1117846456
# when I call os.path.getsize(), I use os.path.join() to join the folder name with the current filename


# Checking Path Validity
# the following will return True or False depending on whether the file of folder exists
os.path.exists(path)

# the following will return True of False depending on whether it exists and is a file
os.path.isfile(path)

# the following will return True of False depending on whether it exists and is a folder
os.path.isdir(path)

>>> os.path.exists('C:\\Windows')
True
>>> os.path.exists('C:\\some_made_up_folder')
False
>>> os.path.isdir('C:\\Windows\\System32')
True
>>> os.path.isfile('C:\\Windows\\System32')
False
>>> os.path.isdir('C:\\Windows\\System32\\calc.exe')
False
>>> os.path.isfile('C:\\Windows\\System32\\calc.exe')
True
'''
You can determine whether there is a DVD or flash drive currently attached to the computer by checking 
for it with the os.path.exists() function. For instance, if I wanted to check for a flash drive with the 
volume named D:\ on my Windows computer, I could do that with the following:
'''
os.path.exists('D:\\')
True


# Reading/Writing Process with .txt files
# Binary files are all other file types, like word documents, PDFs, images, spreadsheets, and .exe's
'''
There are three steps to reading or writing files in Python.

Call the open() function to return a File object.

Call the read() or write() method on the File object.

Close the file by calling the close() method on the File object.'''

# open() function
helloFile = open('C:\\Users\\your_home_folder\\hello.txt')
# in OS X use
helloFile = open('/Users/your_home_folder/hello.txt')


# Reading the Contents of Files
helloContent = helloFile.read()
helloContent
'Hello World!'

# use the readlines() method to get a list of string values from the file, one string for each line of text
sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()
#[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
# outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
# look upon myself and curse my fate,']


# Writing To Files.. write mode will overwrite the existing file and start from scratch
'''
Write mode will overwrite the existing file and start from scratch, just like when you overwrite a 
variable’s value with a new value. Pass 'w' as the second argument to open() to open the file in write 
mode. Append mode, on the other hand, will append text to the end of the existing file. You can think 
of this as appending to a list in a variable, rather than overwriting the variable altogether. 
Pass 'a' as the second argument to open() to open the file in append mode.

If the filename passed to open() does not exist, both write and append mode will create a new, blank 
file. After reading or writing a file, call the close() method before opening the file again.
'''
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
13
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
25
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
'Hello world!'
'Bacon is not a vegetable.'



# Saving Variables with the shelve Module

# The shelve module will let you add Save and Open features to your program. For example, if you ran a 
# program and entered some configuration settings, you could save those settings to a shelf file and then 
# have the program load them the next time it is run.
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
# 3 new files are created: mydata.bak, mydata.dat, and mydata.dir (on OS X mydata.db is created)
# This frees you from worrying about how to store your program's data to a file
# use shelve module to later reopen the data from these files.
# we can open them up and check to make sure the data was properly store by doing the following
shelfFile = shelve.open('mydata')
type(shelfFile)
<class 'shelve.DbfilenameShelf'>
shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
shelfFile.close()
# just like dictionaries, shelf values have keys() and values() methods that return list like values
# to get them to the list for use the list() function
shelfFile = shelve.open('mydata')
list(shelfFile.keys())
['cats'] # the output we get
list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']] # the output
shelfFile.close()
# Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit, 
# but if you want to save data from your Python programs, use the shelve module.



# Saving Variables with the pprint.pformat() Function
'''
remember that pprint.pprint() pretty prints contents of a list or dictionary, while the 
pprint.pformat() function will return this same text as a string instead of printint it
Not only is this string formatted to be easy to read, but it is also syntactically correct 
Python code. Say you have a dictionary stored in a variable and you want to save this variable 
and its contents for future use. Using pprint.pformat() will give you a string that you can 
write to .py file. This file will be your very own module that you can import whenever you want 
to use the variable stored in it.
'''
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
fileObj.close()
'''
The modules that an import statement imports are themselves just Python scripts. When the string from 
pprint.pformat() is saved to a .py file, the file is a module that can be imported just like any other.

And since Python scripts are themselves just text files with the .py file extension, your Python 
programs can even generate other Python programs. You can then import these files into scripts.
'''
import myCats
myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
myCats.cats[0]['name']
'Zophie'


