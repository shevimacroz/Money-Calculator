#this code finds your money spent on everyday life

money_in_hand = float(input('How much money have you got last month?, $: '))

#let's make different variables for different purposes e.g. financial debt, funds spent towards food

entertainment = float(input('Enter your monthly expenses towards Entertainment, $:'))
essentials = float(input('Enter your monthly expenses towards essential equipment and items, $:'))
travel = float(input('Enter your monthly expenses towards travel, $:'))
business_expense = float(input('Enter your monthly expenses towards business, $:'))
charity = float(input('Enter your monthly expenses towards charity, $:'))
materialistic_desires = float(input('Enter your monthly expenses towards your desires, $:'))
other = float(input('Enter your monthly expenses towards other stuff, $:'))
rent = float(input('Enter your monthly expenses towards rent, $:'))
self_improvement = float(input('Enter your monthly expenses towards self improvement, $:'))

#now i am going to calculate the total

total = (entertainment + essentials + travel + business_expense + charity + materialistic_desires + other + rent + self_improvement)

#now lets print how much the total was

print ('This is how much you have spent:', total)

#now lets deduct the money last month with the total expenses

money_left = (money_in_hand - total)

#now it prints the money_left

print('This is how much you have saved or this is how much left:', money_left)


