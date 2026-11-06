# 01 | Variables and arithmetic
# 01. Market Stall Sales Tracker
# Scenario: A trader sells 8 bags of rice at NGN 42,500 each and 5 cartons of noodles at NGN 9,800 each. Delivery
# costs NGN 12,000.
# Your task: Create variables for quantities, unit prices and delivery cost; calculate gross sales, net revenue after
# delivery and average revenue per item. Print labeled results

# Task: Calculate gross sales, net revenue after delivery, and average revenue per item.


rice_qty = 8
rice_price = 42_500
noodles_qty = 5
noodles_price = 9800
delivery_cost = 12_000

gross_sales = rice_qty * rice_price + noodles_qty * noodles_price
net_revenue = gross_sales - delivery_cost
total_items = rice_qty + noodles_qty
average_per_item = net_revenue / total_items

print(f"Gross sales: NGN {gross_sales}")
print(f"Net revenue: NGN {net_revenue}")
print(f"Average per item: NGN {average_per_item:.2f}")



# 2. Ride Fare Calculator
# Scenario: A ride-hailing service charges NGN 900 base fare, NGN 250 per kilometre and NGN 80 per minute. A
# customer travels 12 km in 18 minutes.
# Your task: Store the fare components in variables, calculate the trip fare and add 7.5% service tax. Show fare
# before and after tax.


base_fare = 900
rate_per_km = 250
rate_per_minute = 80
distance_km = 12
distance_minutes = 18
tax_rate = 0.075

fare = base_fare + distance_km * rate_per_km + distance_minutes * rate_per_minute
total = fare + fare * tax_rate

print(f"Fare: NGN {fare:.2f}")
print(f"Total: NGN {total:.2f}")



# 03. Electricity Token Budget
# Scenario: A household has NGN 18,000 for electricity. A prepaid unit costs NGN 145, and a transaction fee of NGN
# 350 applies.
# Your task: Compute the maximum whole units affordable and the money left over after purchase.

# Solution
budget = 18_000
unit_price = 145
transaction_fee = 350
money_for_units = budget - transaction_fee
units = money_for_units // unit_price
balance = money_for_units % unit_price
print(f"Units: {units}")
print(f"Balance: NGN {balance}")