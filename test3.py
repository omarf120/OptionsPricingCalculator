import array
import math
import sys
import os

d_u_given = "Y"
stock_volatility = 0.1
time_step = 1
up_factor = 1.1
down_factor = 0.9

if d_u_given == "N":
    while True:
        try:
            up_factor = math.exp(stock_volatility * math.sqrt(time_step))
        except OverflowError:
            print("Something was wrong with your numbers that resulted in calculator overflow, please try again.")
            try_again = input("Would you like to try again? (Y or N): ").upper()
            while try_again not in ("Y", "N"):
                try_again = input(
                    "Invalid Entry\nPlease enter either \"Y\" for yes, try again "
                    "or \"N\" for no, end program: ").upper()
            if try_again == "Y":
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                sys.exit()
        else:
            break
    while True:
        try:
            down_factor = math.exp(-stock_volatility * math.sqrt(time_step))
        except OverflowError:
            print("Something was wrong with your numbers that resulted in calculator overflow, please try again.")
            try_again = input("Would you like to try again? (Y or N): ").upper()
            while try_again not in ("Y", "N"):
                try_again = input(
                    "Invalid Entry\nPlease enter either \"Y\" for yes, try again "
                    "or \"N\" for no, end program: ").upper()
            if try_again == "Y":
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                sys.exit()
        else:
            break
else:
    stock_volatility = 0.5*(math.log(up_factor)/math.sqrt(time_step)) + \
                       0.5*(math.log(down_factor)/-(math.sqrt(time_step)))


print(up_factor)
print(down_factor)
print(stock_volatility)



