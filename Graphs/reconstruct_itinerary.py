class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        tickets.sort()
        for t in tickets:
            if t[0] not in graph:
                graph[t[0]] = []
            graph[t[0]].append(t[1])

        res = ["JFK"]
        def helper(cur):
            if len(res) == len(tickets) + 1:
                return True
            elif cur not in graph:
                return False
            else:
                neighbors = list(graph[cur])

                for i in range(len(neighbors)):
                    item = graph[cur].pop(i)
                    res.append(item)
                    if helper(item):
                        return True
                    graph[cur].insert(i, item)
                    res.pop()

                return False
        
        helper("JFK")
        return res
