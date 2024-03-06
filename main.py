import os
import sys
import math
import inflect
import scipy.stats as st

# user inputs
# create variable name list
var_names = []
# create values list
var_values = []

# input style of option
style_of_option = input("Style of Option (US or EU): ").upper()
while style_of_option not in ("US", "EU"):
    style_of_option = input("Invalid Entry\nPlease enter either \"US\" for American style options "
                            "or \"EU\" for European style options: ").upper()
var_names.append("Style of Option")
var_values.append(style_of_option)

# input type of option
type_of_option = input("Type of Option (Call or Put): ").capitalize()
while type_of_option not in ("Call", "Put"):
    type_of_option = input("Invalid Entry\nPlease enter either \"Call\" for Call options "
                           "or \"Put\" for Put options: ").capitalize()
var_names.append("Type of Option")
var_values.append(type_of_option)

# input current stock price
stock_price = input("Current Stock Price: $")
while True:
    try:
        float(stock_price)
    except ValueError:
        stock_price = input("Invalid Entry\n"
                            "Please enter a decimal or integer value for the current stock price: $")
    else:
        break
stock_price = float(stock_price)
var_names.append("Current Stock Price")
var_values.append(stock_price)

# input strike price
strike_price = input("Strike Price: $")
while True:
    try:
        float(strike_price)
    except ValueError:
        strike_price = input("Invalid Entry\n"
                             "Please enter a decimal or integer value for the strike price of the option: $")
    else:
        break
strike_price = float(strike_price)
var_names.append("Strike Price: ")
var_values.append(strike_price)

print("---------------------------------------------------------------------------------------------------")

# input years to maturity
years_to_maturity = input("Years to Maturity: ")
while True:
    try:
        float(years_to_maturity)
    except ValueError:
        years_to_maturity = (input("Invalid Entry\n"
                                   "Please enter a decimal or integer value for number of years to maturity: "))
    else:
        break
years_to_maturity = float(years_to_maturity)

# input months to maturity
months_to_maturity = input("Months to Maturity (If you entered total time to maturity in years enter 0): ")
while True:
    try:
        float(months_to_maturity)
    except ValueError:
        months_to_maturity = (input("Invalid Entry\n"
                                    "Please enter a decimal or integer value for number of months to maturity "
                                    "(If you entered total time to maturity in years enter 0): "))
    else:
        break
months_to_maturity = float(months_to_maturity)

# input days to maturity
days_to_maturity = input("Days to Maturity (If you entered total time to maturity in years and months enter 0): ")
while True:
    try:
        float(days_to_maturity)
    except ValueError:
        days_to_maturity = (input("Invalid Entry\n"
                                  "Please enter a decimal or integer value for number of days to maturity "
                                  "(If you entered total time to maturity in years and months enter 0): "))
    else:
        break
days_to_maturity = float(days_to_maturity)

print("---------------------------------------------------------------------------------------------------")

# calculate total months to maturity and check if it is correct with user
ttm_correct = "N"
total_years_to_maturity = float(years_to_maturity + (months_to_maturity / 12) + (days_to_maturity / 365))
while ttm_correct == "N":
    print("Option maturity date is in " + str(years_to_maturity) + " years, "
          + str(months_to_maturity) + " months, and " + str(days_to_maturity) + " days")
    print("Total Number of Years to Maturity: " + str(total_years_to_maturity))
    ttm_correct = input("Is the above information about time to maturity correct? (Y or N): ").upper()
    while ttm_correct not in ("Y", "N"):
        ttm_correct = input("Invalid Entry\nPlease enter either \"Y\" for correct "
                            "or \"N\" for incorrect: ").upper()
    if ttm_correct == "Y":
        break
    # input years to maturity
    years_to_maturity = input("Years to Maturity: ")
    while True:
        try:
            float(years_to_maturity)
        except ValueError:
            years_to_maturity = (
                input("Invalid Entry\n"
                      "Please enter a decimal or integer value for number of years to maturity: "))
        else:
            break
    years_to_maturity = float(years_to_maturity)

    # input months to maturity
    months_to_maturity = input("Months to Maturity (If you entered total time to maturity in years enter 0):: ")
    while True:
        try:
            float(months_to_maturity)
        except ValueError:
            months_to_maturity = (
                input("Invalid Entry\n"
                      "Please enter a decimal or integer value for number of months to maturity "
                      "(If you entered total time to maturity in years enter 0): "))
        else:
            break
    months_to_maturity = float(months_to_maturity)

    # input days to maturity
    days_to_maturity = input("Days to Maturity (If you entered total time to maturity in years and months enter 0): ")
    while True:
        try:
            float(days_to_maturity)
        except ValueError:
            days_to_maturity = (input("Invalid Entry\n"
                                      "Please enter a decimal or integer value for number of days to maturity "
                                      "(If you entered total time to maturity in years and months enter 0): "))
        else:
            break
    days_to_maturity = float(days_to_maturity)

var_names.append("Total Years to Maturity")
var_values.append(total_years_to_maturity)

print("---------------------------------------------------------------------------------------------------")

# input risk free rate
risk_free_rate = input("Annual Risk Free Rate: ")
while True:
    try:
        float(risk_free_rate)
    except ValueError:
        risk_free_rate = (input("Invalid Entry\n"
                                "Please enter a decimal value for the annual risk free rate: "))
    else:
        break
risk_free_rate = float(risk_free_rate)
var_names.append("Risk Free Rate")
var_values.append(risk_free_rate)

# up and down factors while also checking if up>down
up_factor = 0
down_factor = 0.1
stock_volatility = 0

d_u_given = input("Do you have the up and down movement factors? "
                  "(\"Y\" for yes | "
                  "\"N\" for no, I have stock volatility instead): ").upper()
while d_u_given not in ("Y", "N"):
    d_u_given = input("Invalid Entry\nPlease enter either \"Y\" for yes, I have the up and down movement factors "
                      "or \"N\" for no, I have stock volatility instead: ").upper()

if d_u_given == "Y":
    while up_factor < down_factor:
        # input up movement factor
        up_factor = input("Up Movement Factor: ")
        while True:
            try:
                float(up_factor)
            except ValueError:
                up_factor = (input("Invalid Entry\n"
                                   "Please enter an integer or decimal value for "
                                   "the up movement factor of the option: "))
            else:
                break
        up_factor = float(up_factor)

        # input down movement factor
        down_factor = input("Down Movement Factor: ")
        while True:
            try:
                float(down_factor)
            except ValueError:
                down_factor = (input("Invalid Entry\n"
                                     "Please enter an integer or decimal value for the down "
                                     "movement factor of the option: "))
            else:
                break
        down_factor = float(down_factor)
        if up_factor < down_factor:
            print("Up movement factor must be greater than or equal to down movement factor, please try again.")
    var_names.append("Up Movement Factor")
    var_values.append(up_factor)
    var_names.append("Down Movement Factor")
    var_values.append(down_factor)
else:
    stock_volatility = input("Enter stock volatility: ")
    while True:
        try:
            float(stock_volatility)
        except ValueError:
            stock_volatility = (input("Invalid Entry\n"
                                      "Please enter an integer or decimal value for "
                                      "the stock volatility of the option: "))
        else:
            break
    stock_volatility = float(stock_volatility)
    var_names.append("Stock Volatility")
    var_values.append(stock_volatility)

# input number of steps
num_steps = input("Number of Steps: ")
while True:
    try:
        int(num_steps)
    except ValueError:
        num_steps = (input("Invalid Entry\n"
                           "Please enter a positive integer value for the number of steps for the binomial tree: "))
    else:
        break
num_steps = int(num_steps)
while num_steps < 1:
    num_steps = input("Invalid Entry\n"
                      "Number of steps must be an integer value greater than 0\n"
                      "Please try again: ")
    while True:
        try:
            int(num_steps)
        except ValueError:
            num_steps = (input("Invalid Entry\n"
                               "Please enter a positive integer value for the number of steps for the binomial tree: "))
        else:
            break
    num_steps = int(num_steps)
var_names.append("Number of Steps")
var_values.append(num_steps)

time_step = float(total_years_to_maturity / num_steps)
var_names.append("Time Step (dt)")
var_values.append(time_step)

# Inquire and obtain dividend information
dividend_number_list = []
dividend_date_list = []
dividend_amount_list = []
dividend_num_counter = 1
p = inflect.engine()
dividend_correct = "N"
dividends = ""

while dividend_correct == "N":
    dividends = input("Are there ex-dividend dates on this stock before the expiry? (Y or N): ").upper()
    while dividends not in ("Y", "N"):
        dividends = input("Invalid Entry\nPlease enter either \"Y\" for yes "
                          "or \"N\" for no: ").upper()
    if dividends == "Y":
        num_dividend = input("How many ex-dividend dates are there before option expiry?: ")
        while True:
            try:
                int(num_dividend)
            except ValueError:
                num_dividend = (input("Invalid Entry\n"
                                      "Please enter an integer value for the number of "
                                      "ex-dividend dates before option expiry: "))
            else:
                break
        num_dividend = int(num_dividend)
        while num_dividend > num_steps:
            num_dividend = input("Invalid Entry\n"
                                 "Number of ex-dividend dates cannot exceed number of steps (" + str(num_steps) + ")\n"
                                 "Please enter number of ex-dividend dates before option expiry: ")
            while True:
                try:
                    int(num_dividend)
                except ValueError:
                    num_dividend = (input("Invalid Entry\n"
                                          "Please enter an integer value for the number of "
                                          "ex-dividend dates before option expiry: "))
                else:
                    break
            num_dividend = int(num_dividend)
        if num_dividend == num_steps:
            print("Since you have entered number of dividends equal to number of steps, "
                  "the dividends will occur at time steps every " + str(time_step) +
                  " years.")
            while num_dividend > 0:
                dividend_number_list.append("Dividend " + str(dividend_num_counter))
                dividend_date_list.append(float(dividend_num_counter * time_step))
                dividend_amount = input("How much is the " + p.ordinal(dividend_num_counter) +
                                        " dividend " + str(dividend_num_counter * time_step) + " years from today: $")
                print(
                    "--------------------------------------------------"
                    "-------------------------------------------------")
                while True:
                    try:
                        float(dividend_amount)
                    except ValueError:
                        dividend_amount = (input("Invalid Entry\n"
                                                 "Please enter a integer or decimal value for the amount of the "
                                                 + p.ordinal(dividend_num_counter) +
                                                 " dividend dates before option expiry: "))
                    else:
                        break
                dividend_amount = float(dividend_amount)
                dividend_amount_list.append(dividend_amount)
                dividend_num_counter += 1
                num_dividend -= 1
            dividend_correct = "Y"

        while num_dividend not in (0, num_steps):
            dividend_number_list.append("Dividend " + str(dividend_num_counter))
            dividend_date = (input("When is the " + p.ordinal(dividend_num_counter) + " ex-dividend date?\n"
                                   "Please enter the number of years from now of the "
                                   + p.ordinal(dividend_num_counter) + " ex-dividend date: "))
            while True:
                try:
                    float(dividend_date)
                except ValueError:
                    dividend_date = input("Invalid Entry\n"
                                          "Please enter a decimal or integer value for years from now of the "
                                          + p.ordinal(dividend_num_counter) + " ex-dividend date: ")
                else:
                    break
            dividend_date = float(dividend_date)
            while dividend_date > total_years_to_maturity:
                dividend_date = input("Invalid Entry\n"
                                      "Dividend date in years from now must be less than the total time to maturity of "
                                      + str(total_years_to_maturity) + " years\n"
                                      "Please try again with the time in years from now of the " +
                                      p.ordinal(dividend_num_counter) + " ex-dividend date: ")
                while True:
                    try:
                        float(dividend_date)
                    except ValueError:
                        dividend_date = input("Invalid Entry\n"
                                              "Please enter a decimal or integer value for years from now of "
                                              + p.ordinal(dividend_num_counter) + " dividend: ")
                    else:
                        break
                dividend_date = float(dividend_date)
            while (dividend_date / time_step) % 1 != 0:
                dividend_date = input("Invalid Entry\n"
                                      "Time in years from now of the ex-dividend date should be an "
                                      "integer multiple of the time step (" + str(time_step) + "), please try again\n"
                                      "Enter the time in years from now of the " +
                                      p.ordinal(dividend_num_counter) + " ex-dividend date: ")
                while True:
                    try:
                        float(dividend_date)
                    except ValueError:
                        dividend_date = input("Invalid Entry\n"
                                              "Please enter a decimal or integer value for years from now of "
                                              + p.ordinal(dividend_num_counter) + " ex-dividend date: ")
                    else:
                        break
                dividend_date = float(dividend_date)
            dividend_date_list.append(dividend_date)
            dividend_amount = input("How much is the " + p.ordinal(dividend_num_counter) +
                                    " dividend " + str(dividend_date) + " years from today: $")
            print(
                "---------------------------------------------------------------------------------------------------")
            while True:
                try:
                    float(dividend_amount)
                except ValueError:
                    dividend_amount = (input("Invalid Entry\n"
                                             "Please enter a integer or decimal value for the amount of the "
                                             + p.ordinal(dividend_num_counter) +
                                             " dividend dates before option expiry: "))
                else:
                    break
            dividend_amount = float(dividend_amount)
            dividend_amount_list.append(dividend_amount)
            dividend_num_counter += 1
            num_dividend -= 1
    else:
        dividend_correct = "Y"
        num_dividend = 0
        dividend_number_list = []
        dividend_date_list = []
        dividend_amount_list = []

    for x in range(len(dividend_number_list)):
        print(dividend_number_list[x] + ": " + "in " + str(dividend_date_list[x]) + " years for $" +
              str(dividend_amount_list[x]))
    if len(dividend_number_list) == 0:
        print("No Dividends")
    dividend_correct = input("Is the above information about the dividends correct? (Y or N): ").upper()
    while dividend_correct not in ("Y", "N"):
        dividend_correct = input("Invalid Entry\nPlease enter either \"Y\" for correct "
                                 "or \"N\" for incorrect: ").upper()
    print(
        "---------------------------------------------------------------------------------------------------")
    if dividend_correct == "N":
        num_dividend = 0
        dividend_number_list = []
        dividend_date_list = []
        dividend_amount_list = []
        dividend_num_counter = 1

for x in range(len(var_names)):
    print(var_names[x] + ": " + str(var_values[x]))

print("---------------------------------------------------------------------------------------------------")

for x in range(len(dividend_number_list)):
    print(dividend_number_list[x] + ": " + "in " + str(dividend_date_list[x]) + " years for $" +
          str(dividend_amount_list[x]))

if len(dividend_number_list) == 0:
    print("No Dividends")

print("---------------------------------------------------------------------------------------------------")

info_correct = input("Is all of the above information about the option correct? "
                     "(Y to proceed or N to restart): ").upper()
while info_correct not in ("Y", "N"):
    info_correct = input("Invalid Entry\nPlease enter either \"Y\" for correct and proceed "
                         "or \"N\" for incorrect and restart: ").upper()
if info_correct == "N":
    os.execl(sys.executable, sys.executable, *sys.argv)

print("---------------------------------------------------------------------------------------------------")

# Option Calculator
# variables

pv_factor = math.exp(-time_step * risk_free_rate)

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
    stock_volatility = 0.5 * (math.log(up_factor) / math.sqrt(time_step)) + \
                       0.5 * (math.log(down_factor) / -(math.sqrt(time_step)))

if up_factor == down_factor:
    pseudo_prob_up = 0.5
else:
    while True:
        try:
            pseudo_prob_up = (math.exp(time_step * risk_free_rate) - down_factor) / (up_factor - down_factor)
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

pseudo_prob_down = 1 - pseudo_prob_up

if d_u_given == "N":
    var_names.append("Up Movement Factor")
    var_values.append(up_factor)
    var_names.append("Down Movement Factor")
    var_values.append(down_factor)
var_names.append("Pseudo Probability Up")
var_values.append(pseudo_prob_up)
var_names.append("Pseudo Probability Down")
var_values.append(pseudo_prob_down)

# Calculations for option price
'''
if dividends == "N"
'''

middle = [0] * (num_steps - 1)
for i in range(num_steps - 1):
    middle[i] = stock_price * up_factor ** (i + 1) * down_factor ** (num_steps - i - 1)

top = stock_price * up_factor ** num_steps
bottom = stock_price * down_factor ** num_steps
stock_values = [top]
stock_values.extend(list(reversed(middle)))
stock_values.append(bottom)


option_values = []


# def functions for call and put option values

def option_value_call(your_list):
    for value in your_list:
        if value > strike_price:
            option_values.append(value - strike_price)
        else:
            option_values.append(0)


def option_value_put(your_list):
    for value in your_list:
        if value < strike_price:
            option_values.append(strike_price - value)
        else:
            option_values.append(0)


if type_of_option == "Call":
    option_value_call(stock_values)
else:
    option_value_put(stock_values)

pv_nodes = []
us_put_values = [0] * len(stock_values)
node_counter = 0
put_counter = 0

if style_of_option == "EU" or (style_of_option == "US" and type_of_option == "Call"):
    while len(option_values) > 1:
        while node_counter + 1 < len(option_values):
            option_values[node_counter] = pv_factor * (pseudo_prob_up * option_values[node_counter] + pseudo_prob_down *
                                                       option_values[node_counter + 1])
            node_counter += 1
        option_values.pop()
        node_counter = 0
else:
    while len(option_values) > 1:
        while node_counter + 1 < len(option_values):
            option_values[node_counter] = pv_factor * (pseudo_prob_up * option_values[node_counter] + pseudo_prob_down *
                                                       option_values[node_counter + 1])
            node_counter += 1
        option_values.pop()
        stock_values.pop()
        node_counter = 0
        while node_counter < len(stock_values):
            stock_values[node_counter] = stock_values[node_counter] / up_factor
            for i in range(len(stock_values)):
                option_values[i] = max(strike_price - stock_values[i], option_values[i])
            node_counter += 1
        node_counter = 0

# Calculate Black-Scholes-Mertin

pv_dividend_list = [0.0] * len(dividend_amount_list)

if dividends == "Y":
    for i in range(len(dividend_amount_list)):
        pv_dividend_list[i] = dividend_amount_list[i] * math.exp(-risk_free_rate * dividend_date_list[i])
    pv_all_dividends = sum(pv_dividend_list)
    if stock_price <= pv_all_dividends:
        print("With the following information: ")

        for x in range(len(var_names)):
            print(var_names[x] + ": " + str(var_values[x]))

        for x in range(len(dividend_number_list)):
            print(dividend_number_list[x] + ": " + "in " + str(dividend_date_list[x]) + " years for $" +
                  str(dividend_amount_list[x]))

        if len(dividend_number_list) == 0:
            print("No Dividends")

        print("---------------------------------------------------------------------------------------------------")

        print("The binomial tree model with " + str(num_steps) + " steps produces the " +
              type_of_option + " option value of: " + str(option_values[0]))

        print("---------------------------------------------------------------------------------------------------")

        print("The present value of your dividends equals or exceeds the stock price which causes a math error when"
              " calculating the Black-Scholes model")

        print("The calculator has excluded the Black-Scholes model and the Greeks\n"
              "If you would like to include those please retry the calculator with different dividend information")

        print("---------------------------------------------------------------------------------------------------")

        try_again = input("Would you like to run the calculator again? (Y or N): ").upper()
        while try_again not in ("Y", "N"):
            try_again = input(
                "Invalid Entry\nPlease enter either \"Y\" for yes, run again "
                "or \"N\" for no, end program: ").upper()
        if try_again == "Y":
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            sys.exit()

    stock_price = stock_price - pv_all_dividends


d1 = (math.log(stock_price / strike_price) + (risk_free_rate + stock_volatility ** 2 / 2) * total_years_to_maturity) / \
     (stock_volatility * math.sqrt(total_years_to_maturity))
d2 = d1 - stock_volatility * math.sqrt(total_years_to_maturity)

if type_of_option == "Call":
    bsm = stock_price * st.norm.cdf(d1) - \
          (strike_price * math.exp(-risk_free_rate * total_years_to_maturity)) * st.norm.cdf(d2)
else:
    bsm = strike_price * math.exp(-risk_free_rate * total_years_to_maturity) * st.norm.cdf(-d2) - \
          stock_price * st.norm.cdf(-d1)

abs_difference = float(option_values[0]) - bsm
rel_difference = ((float(option_values[0] - bsm)) / bsm) * 100

# Calculate Greeks

if type_of_option == "Call":
    delta = st.norm.cdf(d1)
else:
    delta = -st.norm.cdf(d2)

gamma = st.norm.pdf(d1) / (stock_price * stock_volatility * math.sqrt(total_years_to_maturity))

vega = 0.01 * (stock_price * st.norm.pdf(d1) * math.sqrt(total_years_to_maturity))

if type_of_option == "Call":
    theta = (-stock_price * st.norm.pdf(d1) * stock_volatility /
             (2 * math.sqrt(total_years_to_maturity)) - risk_free_rate * strike_price *
             math.exp(-risk_free_rate * total_years_to_maturity) * st.norm.cdf(d2)) / 365
else:
    theta = (-stock_price * st.norm.pdf(d1) * stock_volatility /
             (2 * math.sqrt(total_years_to_maturity)) + risk_free_rate * strike_price *
             math.exp(-risk_free_rate * total_years_to_maturity) * st.norm.cdf(-d2)) / 365

if type_of_option == "Call":
    rho = 0.01 * (strike_price * total_years_to_maturity * math.exp(
        -risk_free_rate * total_years_to_maturity) * st.norm.cdf(d2))
else:
    rho = 0.01 * (-strike_price * total_years_to_maturity * math.exp(-risk_free_rate * total_years_to_maturity) *
                  st.norm.cdf(-d2))

the_greeks_names = ["Delta", "Gamma", "Vega", "Theta", "Rho"]
the_greeks_values = [delta, gamma, vega, theta, rho]

print("With the following information: ")

for x in range(len(var_names)):
    print(var_names[x] + ": " + str(var_values[x]))

for x in range(len(dividend_number_list)):
    print(dividend_number_list[x] + ": " + "in " + str(dividend_date_list[x]) + " years for $" +
          str(dividend_amount_list[x]))

if len(dividend_number_list) == 0:
    print("No Dividends")

print("---------------------------------------------------------------------------------------------------")

print("The binomial tree model with " + str(num_steps) + " steps produces the " +
      type_of_option + " option value of: " + str(option_values[0]))

print("The Black-Scholes-Mertin model produces a " + type_of_option + " option value of " + str(bsm))

print("The binomial tree model has an absolute error of: " + str(abs_difference))
print("And a relative error of: " + str(rel_difference) + "%")

if type_of_option == "Put" and style_of_option == "US":
    print("If a large error is found, it may be due to the fact that US Put options may be exercised early and the\n"
          "Black-Scholes model used in this calculator does not yet account for that.")

if dividends == "Y":
    print("If a large error is found, it may be due to the fact that there are dividends on this stock and the\n"
          "binomial tree model does not yet account for that")

print("---------------------------------------------------------------------------------------------------")

print("The Greeks:")
for x in range(len(the_greeks_names)):
    print(the_greeks_names[x] + ": " + str(the_greeks_values[x]))

print("---------------------------------------------------------------------------------------------------")

try_again = input("Would you like to run the calculator again? (Y or N): ").upper()
while try_again not in ("Y", "N"):
    try_again = input(
        "Invalid Entry\nPlease enter either \"Y\" for yes, run again "
        "or \"N\" for no, end program: ").upper()
if try_again == "Y":
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    sys.exit()
