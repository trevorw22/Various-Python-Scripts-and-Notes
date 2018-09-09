'''
Exceptions are raised with a raise statement. In code, a raise statement consists of the following:

The raise keyword

A call to the Exception() function

A string with a helpful error message passed to the Exception() function
'''
# >>> raise Exception('This is the error message.')
# Traceback (most recent call last):
#   File "<pyshell#191>", line 1, in <module>
#     raise Exception('This is the error message.')
# Exception: This is the error message.


def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symbol must be a single character string.')
	if width <= 2:
		raise Exception('Width must be greater than 2.')
	if height <= 2:
		raise Exception('Height must be greater than 2.')
	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		boxPrint(sym, w, h)
	except Exception as err:
		print('An exception happened: ' + str(err))


# The traceback includes the error message, the line number and the sequence of the function calls that led to the error.
# This sequence of calls is called the call stack.
def spam():
	bacon()
def bacon():
	raise Exception('This is the error message.')
spam()
# Output:
Traceback (most recent call last):
  File "debug.py", line 42, in <module>
    spam()
  File "debug.py", line 38, in spam
    bacon()
  File "debug.py", line 40, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.



# We can make python give us a traceback log.txt by calling traceback.format_exc().
import traceback 
try:
	raise Exception('This is the error message.')
except:
	errorFile = open('errorInfo.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written to errorInfo.txt')



# Assertions- a sanity check to make sure your code isn't doing something obviously wrong.
# These sanity checks are performed by assert statements.
# Assert statements consist of the assert keyword, a condition (boolean), a comma, a string to display when false.
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
'''
In plain English, an assert statement says, “I assert that this condition holds true, and if not, there 
is a bug somewhere in the program.” Unlike exceptions, your code should not handle assert statements with 
try and except; if an assert fails, your program should crash. By failing fast like this, you shorten the 
time between the original cause of the bug and when you first notice the bug. This will reduce the amount 
of code you will have to check before finding the code that’s causing the bug.

Assertions are for programmer errors, not user errors. For errors that can be recovered from (such as a 
file not being found or the user entering invalid data), raise an exception instead of detecting it with 
an assert statement.
'''


# Using an Assertion in a Traffic Light Simulation. ew is east west and ns is north south
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		elif stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		elif stoplight[key] == 'red':
			stoplight[key] = 'green'
switchLights(market_2nd)

assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


# Assertions can be disabled by passing -o option when running python.

# Using the Logging Module
# Copy the following at the top of your code, but under the shebang line #! python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')



>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
>>> logging.debug('Some debugging details.')
2015-05-18 19:04:26,901 - DEBUG - Some debugging details.
>>> logging.info('The logging module is working.')
2015-05-18 19:04:35,569 - INFO - The logging module is working.
>>> logging.warning('An error message is about to be logged.')
2015-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
>>> logging.error('An error has occurred.')
2015-05-18 19:05:07,737 - ERROR - An error has occurred.
>>> logging.critical('The program is unable to recover!')
2015-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!



'''
The logging.disable() function disables these so that you don’t have to go into your program and 
remove all the logging calls by hand. You simply pass logging.disable() a logging level, and it will 
suppress all log messages at that level or lower. So if you want to disable logging entirely, just add 
logging.disable(logging.CRITICAL) to your program. For example, enter the following into the 
interactive shell:
'''
>>> import logging
>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
>>> logging.critical('Critical error! Critical error!')
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
>>> logging.disable(logging.CRITICAL)
>>> logging.critical('Critical error! Critical error!')
>>> logging.error('Error! Error!')
'''
Since logging.disable() will disable all messages after it, you will probably want to add it near 
the import logging line of code in your program. This way, you can easily find it to comment out or 
uncomment that call to enable or disable logging messages as needed.'''


# Logging to a File
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Breakpoints
import random
heads = 0
for i in range(1, 1001):
	if random.randint(0, 1) == 1:	# The random.randint(0, 1) call will return 0 half the time and 1 the other half. This is basically a 50/50 coin flip.
		heads = heads + 1
		if i == 500:
			print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')


