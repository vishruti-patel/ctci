"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---
Approach:

we need 2 variables which is buy_price and profit to start with. 
Now we need to set some value for buy_price hence started with prices[0]. 
To set the actual value of buy_price, we compare it with other values by iterating over array and if any current price value is lesser than buy_price value, we update it with current price value.
"""



"""

def buy_sell(stock_price):
    buying_price = stock_price[0]
    profit = 0

    for p in stock_price:
        if p < buying_price:
            buying_price = p

        profit = max(profit, p - buying_price)

    return profit

print(buy_sell([7,1,5,3,6,4]))
"""


prices = [7,1,5,3,6,4]
buy_price = prices[0]
profit = 0

for i in range(1, len(prices)):
    if prices[i] < buy_price:
        buy_price = prices[i]

    profit = max(profit, prices[i] - buy_price)

print(profit)



