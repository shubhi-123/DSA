class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        adj=[[] for _ in range(n)]
        for i in range(1,n):
            adj[parent[i]].append(i)

        new_parent=parent[:]
        last={}
        prev=[-1]*n
        stack=[(0,0)]

        while stack:
            node,state=stack.pop()
            if state==0:
                prev[node]=last.get(s[node],-1)
                if prev[node]!=-1:
                    new_parent[node]=prev[node]
                last[s[node]]=node
                stack.append((node,1))
                for child in reversed(adj[node]):
                    stack.append((child,0))
            else:
                if prev[node]==-1:
                    del last[s[node]]
                else:
                    last[s[node]]=prev[node]

        tree=[[] for _ in range(n)]
        for i in range(1,n):
            tree[new_parent[i]].append(i)

        ans=[1]*n
        order=[0]
        for node in order:
            order.extend(tree[node])

        for node in reversed(order[1:]):
            ans[new_parent[node]]+=ans[node]

        return ans