TODO: Reflect on what you learned this week and what is still unclear.

For guessing games: 
Exercise 3 and 4 follow a similar structure 

For exercise 1:
- needed help with the lone rangers where i didnt understand the stepping
- first intro to the guessing game - currently doesn't work 
- for stubborn_asker - fix the last statement for the code 

For exercise 3: 
- need to fix the guessing game and how to end it 

For exercise 4: 
- redo the code 
- plan below 
 # mid = middle_range 

    # guess the number between -50 and 20 

    print("Guess the number I am thinking of!")
    print("It is between {} and {}")

    print("Take a guess")
    guess = input()
    guess = int(guess)

    # first split the range into half to make guess more efficient 

for exercise 4: 
test a number
# actual_number = the result 
    # guess between the numbers 

    while True:
        guess = (low + high) // 2
        print(guess)

        if (guess < actual_number):
            low = guess + 1

        elif (guess > actual_number):
            high = guess - 1

        elif (guess == actual_number):
            return {"guess": guess, "tries": tries}
2. second try 
    if high >= low:
        mid = (high + low) // 2

    # while guess is actual_number 

    if arr[mid] == actual_number: 
        return mid 

    elif arr[mid] > actual_number:
        print("Try a smaller number")
        return {low, high, mid - 1, actual_number}

    else arr[mid] < actual_number:

