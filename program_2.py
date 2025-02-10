#Program by Claire Francis, Feb 9, 2025, Week_4_Program_2.py
# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    total = 0

    another_movie = True

    while another_movie == True:
        movie = input("Enter name of movie: ")
        tickets = int(input("Enter number of tickets: "))
        total = total + tickets

        answer = input("Want to add another movie? Y/N ")
        if (answer == "Y")|(answer == "y"):
            another_movie = True
        else:
            another_movie = False

    print("Here is your total: ", total)
    ######################

if __name__ == '__main__':
    main()
