#Simple script to login to an FTP server and download/upload files to itself.
#Useful for automating backups, but not the most secure (needs to be re-written to use SFTP or SCP)

from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')

#Change the current working directory
ftp.cwd('/specificdomain-or-location/')

def grabFile():
	filename = 'fileName.txt'
	localfile = open(filename, 'wb')
	#retrieve file and write and specify the buffer size
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	#close the connection
	ftp.quit()
	#close the file
	localfile.close()

def placeFile():
	filename = 'fileName.txt'
	ftp.storbinary('STOR '+filename, open(filename, 'rb'))#rb is read binary
	ftp.quit()
