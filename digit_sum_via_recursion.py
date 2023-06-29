#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 4/28/2023
#Project: Digit Sum Via Recursion.
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Write a Python program that asks the user for a positive integer and then, via recursion, 
#will sum all of the digits of the given number. Remember to do error checking and input 
#validation Example: 123's digits sum to 6"
#--------------------------------------------------------------------------------------------
#Algorithm
#-----------------
#Step 1) Display program explanation.
#Step 2) Prompt user for input.
#Step 3) If input valid, proceed to calculate and display digit sum; else, display error 
#       prompt user user for input.
#Step 4) prompt user to iterate again or quit.
#--------------------------------------------------------------------------------------------
#Simply void function used to display program explanation.
def display_program_explanation():

    print('''\nGreetings...
    \tThis program takes a postive integer value and returns
    \tdigit sum. Example: input = 123 -> output = 6''')

#Recursive function designed to calculate the digit some of a given postive integer.
def digit_sum(n):
    
    #Recursively sums the digits of a given positive integer.

    #Verify positive integer.
    if n < 0 or isinstance(n, str):
        raise ValueError('\nInput must be a positive integer.')
    
    #Base case.
    elif n < 10: #Single digit, no recursion needed.
        return n
    
    #Recursive case.
    else:
        return n % 10 + digit_sum(n // 10) #Get number mod. ten (remainder) add to return of
                                           #of recursive call with arg. number int. div. ten.
                                           #Example: n = 11 -> (11 % 10) + (digit_sum(11 // 10))
                                           #1 + 1 = 2

#Main method used to compile all necassary logic to complete the programing task and iterate
#based on user input.
def main():

    #Call function to output explanation to screen.
    display_program_explanation()

    #Declare and initialize variable to control program iteration.
    go_again = True

    #Loop used to iterate program.
    while go_again:

        #Declare and initialize variable for input validation.
        invalid = True

        #Loop used to validate user inpput.
        while invalid:

            #Try block used to catch string values and values less than or equal to zero.
            try:
                num = int(input('\nEnter a positive integer(eg. 123 or 3999): '))#May throw exception.
                
                #Verify that the number is greater than zero.
                if num < 1:
                    raise ValueError
                
                #If this statement is reach, input is valid.
                invalid = False

            #Used to catch all input error exceptions.
            except ValueError:
                print('\nInvalid input. Please enter a positive integer(eg. 123 or 3999).')

        #Display returned results to screen.
        print('\nThe sum of the digits in', num, 'is', digit_sum(num)) #Call digit sum (recursive function)
                                                                       #pass the valid number as an arg.

        #Reset input validation indicating variable.
        invalid = True

        #Loop used to validate user input for iterating program.
        while invalid:
            
            #Prompt user to input "Y" or "N" to indicate termination or iteration.
            print('\nEnter "Y" to calculate another digit sum or "N" to quit.')
            choice = input('\nWould you like to calculate another digit sum? ')

            #Iterate again.
            if choice == 'Y' or choice == 'y':
                invalid = False #Valid input.
                go_again = True #User selected to go again.

            #Quit.
            elif choice == 'N' or choice == 'n':
                invalid = False  #Valid input.
                go_again = False #User selected to quit.

            #Invalid input.
            else:
                print('\nERROR: Invalid input')

    #Display good-bye.
    print('\nGood-Bye...')

#If ran as main, execute main method.
if __name__ == '__main__':
    main()