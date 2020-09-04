def maxProfit(prices):
    buy = []
    sell = []
    status = 'not buy'

    for i in range(len(prices) - 1):

        if status == 'not buy' and prices[i + 1] >= prices[i]:
            buy.append(i)
            status = 'buy'

        if status == 'buy' and prices[i + 1] < prices[i]:
            sell.append(i)
            status = 'not buy'

        if i == len(prices) - 2 and status == 'buy':
            sell.append(len(prices) - 1)

    profit = 0

    for k in range(len(sell)):
        profit += prices[sell[k]] - prices[buy[k]]

    return profit
