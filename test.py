import math

dividend_number_list = []
dividend_date_list = []
dividend_amount_list = []
var_names = []
var_values = []

style_of_option = "EU"
type_of_option = "Call"
stock_price = 50
strike_price = 48
total_years_to_maturity = .5
risk_free_rate = .12
up_factor = 1.2
down_factor = .84
num_steps = 1
time_step = .5
pv_factor = math.exp(-time_step * risk_free_rate)
if up_factor == down_factor:
    pseudo_prob_up = 0.5
else:
    pseudo_prob_up = (math.exp(time_step * risk_free_rate) - down_factor) / (up_factor - down_factor)
pseudo_prob_down = 1 - pseudo_prob_up
dividends = "N"

# start calculations for option price

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

def option_value_call(list):
    for value in list:
        if value > strike_price:
            option_values.append(value - strike_price)
        else:
            option_values.append(0)


def option_value_put(list):
    for value in list:
        if value < strike_price:
            option_values.append(strike_price - value)
        else:
            option_values.append(0)


if type_of_option == "Call":
    option_value_call(stock_values)
else:
    option_value_put(stock_values)

pv_nodes = []
node_counter = 0

if style_of_option == "EU" or (style_of_option == "US" and type_of_option == "Call"):
    while len(option_values) > 1:
        while node_counter + 1 < len(option_values):
            option_values[node_counter] = pv_factor * (pseudo_prob_up * option_values[node_counter] + pseudo_prob_down *
                                                       option_values[node_counter + 1])
            node_counter += 1
        option_values.pop()
        node_counter = 0
if type_of_option == "Put":
    for x in option_values:
        x -= strike_price

print(option_values)
print(len(option_values))
print(option_values)

