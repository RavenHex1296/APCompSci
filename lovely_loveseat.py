lovely_loveseat_description = "This is a colorful loveseat with leather and cushions."
lovely_loveseat_price = 727

lovely_couch_description = "This can fit four people and comes with cushions. The end seats have built in leg rests."
lovely_couch_price = 727

lovely_armchair_description = "This includes leather and can recline. Has a built in leg rest as well"
lovely_armchair_price = 72.7

sales_tax = 0.0825

descriptions = [lovely_loveseat_description, lovely_couch_description, lovely_armchair_description]
prices = [lovely_loveseat_price, lovely_couch_price, lovely_armchair_price]

customer_total = 0
customer_itemization = ""

user_answer = int(input("Do you want a loveseat (1), couch (2), or armchair (3)? Enter the number of the item you want"))

customer_total += prices[user_answer]
customer_itemization += descriptions[user_answer]

print(customer_itemization, "It costs $" + str(customer_total) + ".")