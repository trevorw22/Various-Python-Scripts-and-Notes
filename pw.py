#! python3
#pw.py - An insecure password locker
import sys, pyperclip

PASSWORDS = {'email': 's3cr3T_3M41L_P4$$w0rd',
             'blog': 's3cr3T_8L0gging_P4$$',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
