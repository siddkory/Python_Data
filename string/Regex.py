import re

"""
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string

https://www.w3schools.com/python/python_regex.asp

Character	Description	Example	 
[]	A set of characters	"[a-m]"	
\ 	Signals a special sequence (can also be used to escape special characters)	"\d"
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group	 

"""