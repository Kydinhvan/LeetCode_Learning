# Last updated: 1/22/2026, 12:12:37 PM
import heapq
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        # 0 buy: look at sell order with smallest price in backlog
            # if sell <=  buy: remove both from backlog
            # else: backlog <- buy

        # 1 sell: look at largest price of buy order in backlog
            # if buy >=  sell: remove both from backlog
            # else: backlog <- sell
        
        # brute: for each i, check each n: O(n^2)
        # need largest and smallest buy or sell from backlog -> min max heap
        # while order amount > 0 and sell <=  buy and sell, 
        sell_min_heap = []
        buy_max_heap = []
        for price, amount, order_type in orders:    
            if order_type == 1: # sell order
                while amount > 0 and buy_max_heap and -buy_max_heap[0][0] >= price:
                    b_price, b_amount= heapq.heappop(buy_max_heap) # price neg
                    small = min(b_amount, amount)
                    amount -= small # either 0 or leftover
                    b_amount -= small # either left over or 0
                    if b_amount > 0: # leftover buy order, put back in backlog
                        heapq.heappush(buy_max_heap, (b_price,b_amount))
                    
                if amount > 0: # leftover sell order, put in backlog
                    heapq.heappush(sell_min_heap, (price,amount))

            elif order_type == 0: # buy order
                while amount > 0 and sell_min_heap and sell_min_heap[0][0] <= price:
                    s_price, s_amount = heapq.heappop(sell_min_heap)
                    small = min(s_amount, amount)
                    amount -= small
                    s_amount -= small
                    if s_amount > 0: # leftover sell order, put back in backlog
                        heapq.heappush(sell_min_heap, (s_price,s_amount))
                    

                if amount > 0: # leftover buy order, put in backlog
                    heapq.heappush(buy_max_heap, (-price,amount)) # goes in as neg

        total = 0
        for price, amount in sell_min_heap:  
            total += amount
        for price, amount in buy_max_heap: 
            total += amount 
        return total % (10**9 + 7)