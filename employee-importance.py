# BFS 
# O(n) time, O(n) space
# Definition for Employee.
class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        self.map = {emp.id: emp for emp in employees}
        queue=deque([id])
        result=0
        while len(queue)>0:
            eid = queue.popleft()
            emp = self.map[eid]
            result += emp.importance

            for subId in emp.subordinates:
                queue.append(subId)

        return result 


# DFS 
# O(n) time, O(n) space
class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        self.map = {emp.id: emp for emp in employees}
        self.result = 0
        self.dfs(id)
        return self.result 

    def dfs(self, id):
        emp = self.map[id]
        self.result += emp.importance
        for subId in emp.subordinates:
            self.dfs(subId) 