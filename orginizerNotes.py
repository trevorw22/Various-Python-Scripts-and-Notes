# Copying Files and Folders with shutil

import shutil, os
# File Copy
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')
'C:\\delicious\\spam.txt'
shutil.copy('eggs2.txt', 'C:\\eggs2.txt')
'C:\\delicious\\eggs2.txt'

# Folder Copy (backing up your precious bacon folder)
import shutil, os
os.chdir('C:\\')
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
'C:\\bacon_backup'

# Moving and Renaming Files and Folders
# This will overwrite any files in the destination folder
# There has to be a folder named eggs or else this will rename bacon.txt to a file named eggs
import shutil
shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'

# In the following example, the source file is moved and renamed.
# There needs to be an eggs folder for this one too
import shutil
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'

# Example with no folder named eggs
# This can be a tough to spot bug in your code!!!!
import shutil
shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs'

# Exception error if folder doesn't exist
import shutil
shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
Traceback (most recent call last):


# Permanently Deleting Files and Folders
# You can delete a single file or single empty folder with the os module, but to delete a folder and all
# contents, you use the shutil module
os.unlink(path) # will delete the file at path
os.rmdir(path)  # will delete the folder at path (this folder must be empty of any files and folders)
shutil.rmtree(path) # removes folder at path, and all files and folders it contains

# It’s often a good idea to first run your program with these calls commented out and with print() calls added to show the files that would be deleted
import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
# If you had any important files ending with .rxt, they would have been accidentally, permanently deleted.
# Instead, you should have first run the program like this:


import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)

# Deletes all files in a folder that end in .txt
import os
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)


# Safe deletes with the send2trash module. (Sends deleted items to your recycle bin)
# Install it by running pip install send2trash
# This won't free up disk space like os and shutil, also send2trash cannot recover from recycle bin
import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
25
baconFile.close()
send2trash.send2trash('bacon.txt')


# Walking a Directory Tree using os.walk
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': ' + filename)

	print('')
# os.walk() will return 3 values on each iteration through the loop
# 1. A string of the current folder's name in the current iteration of the for loop
# 2. A list of strings of the folders in the current folder in the current iteration of the for loop
# 3. A list of strings of the files in the current folder in the current iteration of the for loop
# Keep in mind the current working directory is not changed by os.walk()
# The output of the program will look like the following..
'''
The current folder is C:\delicious
SUBFOLDER OF C:\delicious: cats
SUBFOLDER OF C:\delicious: walnut
FILE INSIDE C:\delicious: spam.txt

The current folder is C:\delicious\cats
FILE INSIDE C:\delicious\cats: catnames.txt
FILE INSIDE C:\delicious\cats: zophie.jpg

The current folder is C:\delicious\walnut
SUBFOLDER OF C:\delicious\walnut: waffles

The current folder is C:\delicious\walnut\waffles
FILE INSIDE C:\delicious\walnut\waffles: butter.txt.


"Since os.walk() returns lists of strings for the subfolder and filename variables, you can use these
lists in their own for loops. Replace the print() function calls with your own custom code.
(Or if you don’t need one or both of them, remove the for loops.)""
'''


# Compressing Files with the zipfile Module
# To read a zip file you must create a ZipFile object by calling the zipfile.ZipFile()
# we then pass it a string of the .zip file's name
import zipfile, os
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
13908
spamInfo.compress_size
3828
# The following command calculates how efficiently example.zip is compressed by dividing the original
# file size by the compressed file size and prints this information using a string formatted with %s.
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
'Compressed file is 3.63x smaller!'
exampleZip.close()
# a ZipFile object has a namelist() method that returns a list of strings for all the files and folders in the Zip file
# These strings can be passed to the getinfo() ZipFile method to return a ZipInfo object about that file.
# ZipFile object represents the entire archive file, and ZipInfo holds information about a single file in the archive.

# Extracting From ZIP Files
# the extractall() method extracts all the files and folders from a ZIP file into the current working directory.
import zipfile, os
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()
# Optionally you can pass a folder name to extractall() to extract to a specific folder other than the CWD
# If the folder passed to extractall() doesn't exist, it will be created.
# an example would be if you replaced line 4 with:
exampleZip.extractall('C:\\ delicious') # not sure about the space there...


# Creating and Adding to ZIP Files
# to create a zip file we open the ZipFile object in write mode by passing 'w' as the second argument
# write(filename, compressionType) a commong compression type is zipfile.ZIP_DEFLATED
import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
# This code creates a new ZIP file named new.zip that has the compressed contents of spam.txt
