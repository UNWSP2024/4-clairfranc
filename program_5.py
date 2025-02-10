# By Claire Francis, Feb 9, 2025, Program_5.py
# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. (Enter 0 to exit the loop)
# When the loop finishes, the program should display the amount that the
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    budget = float(input("Enter amount for budget: "))
    spent = True
    while spent == True:
        spent = float(input("Enter expense for that month and enter 0 to stop program: "))
        total = total + spent

        if spent > 0:
            spent = True
        else:
            spent = False

    difference = budget - total
    print('What remains of budget after expenses: $' , format(difference, '.2f'))

    ######################


if __name__ == '__main__':
    main()
