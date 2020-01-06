class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solutions(object):
    def cloneGraph(self, node):
        d = dict()
        q = [node]
        d[node] = Node(node.val, [])
        while q:
            n = q.pop(0)
            newnode = d[n]
            for x in n.neighbors:
                if d.get(x):
                    newnode.neighbors.append(d.get(x))
                else:
                    d[x] = Node(x.val, [])
                    newnode.neighbors.append(d[x])
                    q.append(x)
        return d[node]
    # DFS
    def cloneGraph2(self, node):
        d = dict()
        stack = [node]
        d[node] = Node(node.val, [])
        while stack:
            curr = stack.pop()
            n = d[curr]
            for x in curr.neighbors:
                if d.get(x):
                    n.neighbors.append(d[x])
                else:
                    d[x] = Node(x.val, [])
                    stack.append(x)
                    n.neighbors.append(d[x])
        return d[node]

