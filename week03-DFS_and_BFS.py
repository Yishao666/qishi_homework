# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:57:10 2019

@author: luhao
"""

# Lintcode 376 二叉树的路径和

def answer376(root, target):
    res = []
        
    def dfs(root,path):
        if not root:
            return
        if not (root.left or root.right):
            if sum(path)+root.val==target:
                res.append(path+[root.val])
            return
        dfs(root.left,path+[root.val])
        dfs(root.right,path+[root.val])
    dfs(root,[])
    return res



# lintcode 164 不同的二叉树
def answer164(n):
    def dfs(low,high):
        if low>high:
            return [None]
        out = []
        for mid in range(low,high+1):
            left = dfs(low,mid-1)
            right = dfs(mid+1,high)
            for l in left:
                for r in right:
                    head = TreeNode(mid)
                    head.left = l
                    head.right = r
                    out.append(head)
        return out
    
    return dfs(1,n)

# leetcode 200 the number of islands
'''
Runtime: 112 ms, faster than 88.42% of Python online submissions for Number of Islands.
Memory Usage: 19 MB, less than 39.78% of Python online submissions for Number of Islands.
'''
def answer200(grid):
    count = 0
        
    def dfs(i, j):
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        
        if i > 0 and grid[i-1][j] == '1':
            dfs(i-1,j)
        if i < len(grid)-1 and grid[i+1][j] == '1':
            dfs(i+1,j)
        if j > 0 and grid[i][j-1] == '1':
            dfs(i,j-1)
        if j < len(grid[0])-1 and grid[i][j+1] == '1':
            dfs(i,j+1)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

# leetcode 107
'''
Runtime: 32 ms, faster than 20.69% of Python online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 12.2 MB, less than 73.58% of Python online submissions for Binary Tree Level Order Traversal II.
'''
def answer107(root):
    if not root:
        return []
    # 要自己再学一学怎么implement deque
    res = []
    queue = [root]
    
    while queue:
        size = len(queue)
        ans = []
        for i in range(size):
            node = queue.pop()
            ans.append(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        
        res.insert(0, ans)
    
    return res