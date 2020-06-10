"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

for word in some_words:
    #I think this will print the words in the string. 
    print(word) # it printed  "what"
    
for x in some_words:
    #I think this will print "?" because there's no value/
    print(x) # it printed "?"

print(some_words)
#I think this will print ['what', 'does', 'this', 'line', 'do', '?']

if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
