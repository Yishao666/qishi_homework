# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:32:12 2019

@author: Lu Haoyi
"""
'''
190. Reverse Bits

Runtime: 12 ms, faster than 95.52% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 42.19% of Python online submissions for Reverse Bits.
'''
def reverseBits(self, n):
    res = 0
    for i in range(32):
        res = (res<<1) + (n&1)
        n /= 2
    return res

'''
201. Bitwise AND of Numbers Range

Runtime: 40 ms, faster than 86.88% of Python online submissions for Bitwise AND of Numbers Range.
Memory Usage: 11.7 MB, less than 73.33% of Python online submissions for Bitwise AND of Numbers Range.
'''
def rangeBitwiseAnd(self, m, n):
    count = 0
    while(m != n):
        m >>= 1
        n >>= 1
        count += 1
    return m<<count

'''
338. Counting Bits

Runtime: 64 ms, faster than 89.75% of Python online submissions for Counting Bits.
Memory Usage: 15.8 MB, less than 37.37% of Python online submissions for Counting Bits.
'''
def countBits(self, num):
    bits = [0]* (num+1)
    for i in range(1, num+1):
        bits[i] = bits[i>>1] + (i%2)
    return bits

'''
1125. Smallest Sufficient Team

Runtime: 28 ms, faster than 98.85% of Python online submissions for Smallest Sufficient Team.
Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Smallest Sufficient Team.
'''


def smallestSufficientTeam(self, req_skills, people):
    # create bitmap
    n = len(req_skills)
    people_skills = []
    skill_people = [[] for i in range(n)]
    skill_index = {req_skills[i]: i for i in range(n)}
    for i in range(len(people)):
        num = 0
        for s in people[i]:
            if s in skill_index:
                skill_people[skill_index[s]].append(i)
                num |= (1 << skill_index[s])
        people_skills.append(num)
    
    res = {2**n - 1: []}
    for i in range(n):
        temp = {}
        for skill_set, team in res.iteritems():
            index = int(math.floor(math.log(skill_set, 2)))
            for p in skill_people[index]:
                p_skill = people_skills[p]
                remain = skill_set & (~p_skill)
                new_team = team + [p]
                if remain == 0:
                    return new_team
                temp[remain] = new_team
        res = temp
    return None

'''
260. Single Number III

Runtime: 48 ms, faster than 58.83% of Python online submissions for Single Number III.
Memory Usage: 13.1 MB, less than 64.77% of Python online submissions for Single Number III.
'''

def singleNumber(self, nums):
    diff = 0
    for num in nums:
        diff ^= num
    count = 0
    while (diff & (1 << count)) == 0:
        count += 1
    res = [0, 0]
    for num in nums:
        if num & (1 << count) == 0:
            res[0] ^= num
        else:
            res[1] ^= num
    return res

'''
477. Total Hamming Distance

Runtime: 452 ms, faster than 61.34% of Python online submissions for Total Hamming Distance.
Memory Usage: 12.7 MB, less than 68.18% of Python online submissions for Total Hamming Distance.
'''
def totalHammingDistance(self, nums):
    total = 0
    for i in range(32):
        count = 0
        for j in range(len(nums)):
            count += (nums[j] >> i) & 1
        total += (count * (len(nums) - count))
    return total
                