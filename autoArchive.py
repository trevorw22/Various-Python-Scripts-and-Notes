#! python3
# Creates backup zip files, automatically increments the backup.zip filenames
import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of "folder" into a ZIP file
	folder = os.path.abspath(folder) # make sure folder is absolute
	# Figure out the filename this code should use based on what files already exist
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break 		# The first nonexistant filename that exists breaks the loop 
		number = number + 1

	# Create the ZIP file
	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')
	print('Done.')

	# Walk the entire folder tree and compress the files in each folder
	for foldername, subfolders, filenames in os.walk(folder): # You can use os.walk() in a for loop, 
		# and on each iteration it will return the iteration’s current folder name, the subfolders in 
		# that folder, and the filenames in that folder.
		print('Adding files in %s...' % (foldername))
		# Add the current folder to the ZIP file.
		backupZip.write(foldername)
		# Add all the files in this folder to the ZIP file.
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue # don't backup the backup ZIP files
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()
	print('Done')

backupToZip('C:\\delicious')

# TODO: add ability to backup only certain file extensions, analyze disk space and archive the biggest folder.
