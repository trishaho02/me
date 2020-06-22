# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    the_numbers = []
    x = start 
    while x < stop:
        print(x) 
        the_numbers.append(x) 
        x = x + step 
    return the_numbers


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    the_numbers = []
    for x in range(1)
    x = start 
    while x < stop: 
        print(x) * 2
        x = x * 2 + step 
    return the_numbers

        
def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    def two_step_ranger(start, stop, step=2):
        if step = 2:
            start, stop, step = 2
        
    while 






def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    
    stubborn_number = int(input('Enter a number between low and high'))
    while not (low < stubborn_number < high):

    if stubborn_number < low: 
        print ('Try a higher number')

    if stubborn_number > high:
        print ("Try a lower number")

    if stubborn_number > low and stubborn_number < high: 
        print ("Try again")
        return stubborn_number
    stubborn_number = int(input("Enter a number between low and high"))

    return stubborn_number



def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "Enter a number only"

    number = input('Enter a number: ')
    while not number.isdigit():
        number = input(message)

    return number

    


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    
    message = ("Type a number: ")
    not_number_rejector()
    Wrong = False 

    Combine = input("What number is between low and high?")
    while Wrong != True:
        while not Combine.isdigit():
            Combine = input("Try again")
            return Combine 

            while not (low < Combine < high):
                if Combine < low:
                    print ("Try higher")
                if Combine > high:
                    print ("Try lower")
                if Combine > low and Combine < high:
                    Wrong = True 
                    
                    return Combine 


   

if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
