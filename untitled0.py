months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
profits = (20000, 45000, 78000, 97000, 12000, 400000, 65000, 54000, 10000,30000,70000,90000)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = months[max_profit_index]
print("The Maximum Profit of " + str(max_profit) + " was recorded in " + str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = months[min_profit_index]
print("The Minimun Profit of " + str(min_profit) + " was recorded in " + str(min_profit_month))