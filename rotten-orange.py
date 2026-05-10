# O(m*n) time, O(m*n) space
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # DFS 
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r, c, time):
            # If out of bounds OR cell is empty OR we found a faster way to rot this orange already
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0:
                return
            # we've found an orange that's already been rotted, do not overwrite
            if 1 < grid[r][c] < time: 
                return

            grid[r][c] = time
            for dr, dc in directions:
                dfs(r + dr, c + dc, time + 1)

        # Start DFS from every initially rotten orange (value 2)
        # Why? because the rotten orange might be on an island (unreachable from previous searches)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    # We pass 2 as the starting time so the next orange becomes 3
                    dfs(r, c, 2)
 
        max_time = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1  # A fresh orange was never reached
                max_time = max(max_time, grid[r][c])

        # If max_time is 0 (all empty) or 2 (no spread), return 0. 
        # Otherwise, subtract the initial offset of 2.
        return max(0, max_time - 2)
# BFS
# O(m*n) time, O(m*n) space
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh += 1
                if grid[r][c]==2:
                    q.append([r,c])

        while len(q)>0 and fresh > 0:

            for i in range(len(q)):
                r,c = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions: 
                    row = r + dr 
                    col = c + dc 
                    if row < 0 or row > len(grid) or col < 0 or col > len(grid[0]) or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh == 0 else -1 













