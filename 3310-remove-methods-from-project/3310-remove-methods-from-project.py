class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj=[]
        from collections import deque
        for i in range(n):
            adj.append([])
        for u,v in invocations:
            adj[u].append(v)
        suspicious=[False]*n
        q=deque([k])
        suspicious[k]=True
        while q:
            node=q.popleft()
            for neighbor in adj[node]:
                if not suspicious[neighbor]:
                    suspicious[neighbor]=True
                    q.append(neighbor)
        for u,v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        ans=[]
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)
        return ans
