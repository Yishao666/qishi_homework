# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:04:24 2019

@author: Lu Haoyi
"""
# 这块儿内容感觉学的不是很好，就做出来两道题，之后好好学一学，再把其他题补上

'''
207. Course Schedule

Runtime: 472 ms, faster than 12.90% of Python online submissions for Course Schedule.
Memory Usage: 13 MB, less than 96.91% of Python online submissions for Course Schedule.
'''
from collections import deque
def canFinish(self, numCourses, prerequisites):
    indegree = [0] * numCourses
    for pairs in prerequisites:
        indegree[pairs[0]] += 1
        
    queue = deque ([])
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
    remain = numCourses
    while len(queue) != 0:
        node = queue.popleft()
        remain -= 1
        for pairs in prerequisites:
            if pairs[1] == node:
                indegree[pairs[0]] -= 1
                if indegree[pairs[0]] == 0:
                    queue.append(pairs[0])
    return remain == 0

'''
787. Cheapest Flights Within K Stops

Runtime: 80 ms, faster than 65.91% of Python online submissions for Cheapest Flights Within K Stops.
Memory Usage: 18 MB, less than 13.12% of Python online submissions for Cheapest Flights Within K Stops.
'''
from collections import defaultdict
def findCheapestPrice(self, n, flights, src, dst, K):
    flight_dict = defaultdict(list)
    for flight in flights:
        flight_dict[flight[0]].append((flight[1], flight[2]))
        
    pq = [(0, src, K+1)]
    
    while len(pq) != 0:
        price, city, remaining_stops = heapq.heappop(pq)
        if city == dst:
            return price
        if remaining_stops > 0:
            for neighbor, cost in flight_dict[city]:
                heapq.heappush(pq, (price + cost, neighbor, remaining_stops - 1))
    return -1

















