#By Claire Francis, Feb 9th, 2025, Program_3.py
# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average
# rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    Years = 0
    m=0
    rainfall = 0
    total_rain = 0

    Years = int(input("how many years? "))
    for y in range(1,Years+1):                  # y for years
        for m in range(1,13):                 # m for months
            print("How many inches of rainfall per year", y, "month ", m)
            rainfall = float(input(""))
            total_rain = total_rain + rainfall
    total_months = Years * 12


    print("total number of months: ", total_months)
    print("total inches of rainfall: ", total_rain)
    print("average rainfall per month for entire period:", total_rain / total_months)
    ######################


if __name__ == '__main__':
    main()
