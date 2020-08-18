# Lesson 5, Task 7

import json

with open('companies_balance.txt', encoding='utf-8') as f:
    list_companies_balance = f.readlines()

total_profit = 0
d_profit = {}
list_temp = []
for i in range(len(list_companies_balance)):
    list_temp = list_companies_balance[i].split()
    profit = int(list_temp[2]) - int(list_temp[3])
    d_profit[list_temp[0]] = profit
    if profit > 0:
        total_profit += profit

d_average_profit = {'Average profit': int(total_profit/len(list_companies_balance))}

final_list = [d_profit, d_average_profit]
print(final_list)

with open('companies_balance.json', 'w') as f:
    json.dump(final_list, f)