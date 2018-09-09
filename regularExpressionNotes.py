# Regular Expression Notes/Examples from Automate the Boring Stuff

''' REVIEW QUICK REFERENCE
The ? matches zero or one of the preceding group.

The * matches zero or more of the preceding group.

The + matches one or more of the preceding group.

The {n} matches exactly n of the preceding group.

The {n,} matches n or more of the preceding group.

The {,m} matches 0 to m of the preceding group.

The {n,m} matches at least n and at most m of the preceding group.

{n,m}? or *? or +? performs a nongreedy match of the preceding group.

^spam means the string must begin with spam.

spam$ means the string must end with spam.

The . matches any character, except newline characters.

\d, \w, and \s match a digit, word, or space character, respectively.

\D, \W, and \S match anything except a digit, word, or space character, respectively.

[abc] matches any character between the brackets (such as a, b, or c).

[^abc] matches any character that isn’t between the brackets.
'''




'''
Import the regex module with import re.

Create a Regex object with the re.compile() function. (Remember to use a raw string.)

Pass the string you want to search into the Regex object’s search() method. This returns a Match object.

Call the Match object’s group() method to return a string of the actual matched text.
'''

# \d means digit, we can use \d\d\d-\d\d\d-\d\d\d\d to find phone numbers.
# {3} means find three of that type, so we can use \d{3}-\d{3}-\d{4} to do the same thing but shorter.
import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# the r in re.compile() is what tells it to use a regexpression instead of having to use \\d
mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo variable name is just a generic name to use for Match objects
print('Phone number found: ' + mo.group())
# Phone number found: 415-555-4242
'''
Here, we pass our desired pattern to re.compile() and store the resulting Regex object
in phoneNumRegex. Then we call search() on phoneNumRegex and pass search() the string we
want to search for a match. The result of the search gets stored in the variable mo. In
this example, we know that our pattern will be found in the string, so we know that a Match
object will be returned. Knowing that mo contains a Match object and not the null value
None, we can call group() on mo to return the match. Writing mo.group() inside our print
statement displays the whole match, 415-555-4242.
'''

# example 2, grabbing parts of the regex with group(1), group(2), etc.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
# '415'
mo.group(2)
# '555-4242'
mo.group(0)
# '415-555-4242'
mo.group()
# '415-555-4242'

# to return all the groups at once use the groups() method
mo.groups()
# ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
# 415
print(mainNumber)
# 555-4242

# regex with parenthesis
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
# '(415)'
mo.group(2)
# '555-4242'
# The \( and \) escape characters in the raw string passed to re.compile() will match
# actual parenthesis characters.



# Matching multiple groups with |   The first match will be returned, and it acts as an 'or'
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
'Batman'

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
'Tina Fey'


# finding all words that begin with 'bat'
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
'Batmobile'

mo.group(1)
'mobile'


# optional pattern matching. The ? is used to mark an optional part of the regex.
# It will return a match whether or not what preceedes the ? is in there.
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'


# to find phone numbers that do or do not have an area code use what we just learned
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
'415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
'555-4242'


# the * means to match zero or more, the group preceeding the * can occur any number or times
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
'Batwowowowoman'


# the + means to match one or more, must appear atleast once
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
'True'


# curly braces. the regex (Ha){3} will match the string 'HaHaHa', but it will
# not match 'HaHa', since the latter has only two repeats of the (Ha) group.
# the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
'HaHaHa'
mo2 = haRegex.search('Ha')
mo2 == None
'True'


'''
Python’s regular expressions are greedy by default, which means that in ambiguous
situations they will match the longest string possible. The non-greedy version of
the curly brackets, which matches the shortest string possible, has the closing curly
bracket followed by a question mark.
'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
'HaHaHa'
# Note that the question mark can have two meanings in regular expressions:
# declaring a nongreedy match or flagging an optional group. These meanings are
#entirely unrelated.


# the findall() method will return the strings of every match in the searched string
# search example
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
'415-555-9999'
# findall example
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
# with groups, each tuple represents a found match
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
'''
To summarize what the findall() method returns, remember the following:

When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method
findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].

When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\ d\d\d), the
method findall() returns a list of tuples of strings (one string for each group),
such as [('415', '555', '9999'), ('212', '555', '0000')].
'''


'''
\d
Any numeric digit from 0 to 9.

\D
Any character that is not a numeric digit from 0 to 9.

\w
Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

\W
Any character that is not a letter, numeric digit, or the underscore character.

\s
Any space, tab, or newline character. (Think of this as matching “space” characters.)

\S
Any character that is not a space, tab, or newline.
'''
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
'''
The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+),
followed by a whitespace character (\s), followed by one or more letter/digit/underscore
characters (\w+). The findall() method returns all matching strings of the regex pattern
in a list.
'''

'''
There are times when you want to match a set of characters but the shorthand character classes
(\d, \w, \s, and so on) are too broad. You can define your own character class using square
brackets. For example, the character class [aeiouAEIOU] will match any vowel, both lowercase
and uppercase.
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
# You can also include ranges of letters or numbers by using a hyphen
# [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers

'''
Note that inside the square brackets, the normal regular expression symbols are not interpreted
as such. This means you do not need to escape the ., *, ?, or () characters with a preceding
backslash. For example, the character class [0-5.] will match digits 0 to 5 and a period. You
do not need to write it as [0-5\.].

By placing a caret character (^) just after the character class’s opening bracket, you can
make a negative character class. A negative character class will match all the characters
that are not in the character class. For example, enter the following into the
interactive shell:
'''
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
# Now, instead of matching every vowel, we’re matching every character that isn’t a vowel.


'''
You can also use the caret symbol (^) at the start of a regex to indicate that a match must
occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the
end of the regex to indicate the string must end with this regex pattern. And you can use
the ^ and $ together to indicate that the entire string must match the regex—that is, it’s
not enough for a match to be made on some subset of the string.
For example, the r'^Hello' regular expression string matches strings that begin with 'Hello'.
'''
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said hello.') == None
True

# The r'\d$' regular expression string matches strings that end with a numeric character
# from 0 to 9
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
<_sre.SRE_Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two.') == None
True

# The r'^\d+$' regular expression string matches strings that both begin and end with one
# or more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
True
wholeStringIsNum.search('12 34567890') == None
True
'''
The last two search() calls in the previous interactive shell example demonstrate how the
entire string must match the regex if ^ and $ are used.

I always confuse the meanings of these two symbols, so I use the mnemonic
“Carrots cost dollars” to remind myself that the caret comes first and the dollar sign
comes last.
'''


# The . (or dot) character in a regular expression is called a wildcard and will match
# any character except for a newline
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
'''
Remember that the dot character will match just one character, which is why the match for
the text flat in the previous example matched only lat. To match an actual dot, escape the
dot with a backslash: \..
'''


'''
t to match the string 'First Name:', followed by any and all text, followed by 'Last Name:',
and then followed by anything again. You can use the dot-star (.*) to stand in for that
“anything.” Remember that the dot character means “any single character except the newline,”
and the star character means “zero or more of the preceding character.”
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
'Al'
mo.group(2)
'Sweigart'
'''
The dot-star uses greedy mode: It will always try to match as much text as possible.
To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?).
Like with curly brackets, the question mark tells Python to match in a nongreedy way.
'''
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
'<To serve man>'
# greedy version
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
'<To serve man> for dinner.>'


# .* matches everything but a newline, to match all chars and newlines we use re.DOTALL
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.'
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'



# To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second
# argument to re.compile()
robocop = re.compile(r'robocop', re.I)
robocop.search('Robocop is part man, part machine, all cop.').group()
'Robocop'
robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'
robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'


'''
The sub() method for Regex objects is passed two arguments. The first argument is a string
to replace any matches. The second is the string for the regular expression. The sub()
method returns a string with the substitutions applied.
'''
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
'''
In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text
of group 1, 2, 3, and so on, in the substitution.”

For example, say you want to censor the names of the secret agents by showing just the first
letters of their names. To do this, you could use the regex Agent (\w)\w* and pass r'\1****'
as the first argument to sub(). The \1 in that string will be replaced by whatever text was
matched by group 1—that is, the (\w) group of the regular expression.
'''
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
'A**** told C**** that E**** knew B**** was a double agent.'



'''
***********************************************
Regular expressions are fine if the text pattern you need to match is simple. But matching
complicated text patterns might require long, convoluted regular expressions. You can mitigate
this by telling the re.compile() function to ignore whitespace and comments inside the regular
expression string. This “verbose mode” can be enabled by passing the variable re.VERBOSE as
the second argument to re.compile().
Now instead of a hard-to-read regular expression like this:
'''
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
you can spread the regular expression over multiple lines with comments like this:

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?            # area code
	(\s|-|\.)?                    # separator
	\d{3}                         # first 3 digits
	(\s|-|\.)                     # separator
	\d{4}                         # last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?  # extension
	)''', re.VERBOSE)

# Note how the previous example uses the triple-quote syntax (''') to create a multiline string
'''	so that you can spread the regular expression definition over many lines, making it much
	more legible.

The comment rules inside the regular expression string are the same as regular Python code:
The # symbol and everything after it to the end of the line are ignored. Also, the extra
spaces inside the multiline string for the regular expression are not considered part of the
text pattern to be matched. This lets you organize the regular expression so it’s easier to
read.
*************************************************
'''

# if you want a regular expression that’s case-insensitive and includes newlines to match
# the dot character, you would form your re.compile() call like this:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
# All three options for the second argument will look like this:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
