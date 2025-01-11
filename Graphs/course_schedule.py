class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph(prereq):
            g = {}

            for a, b in prereq:
                if a in g:
                    g[a].add(b)
                else:
                    g[a] = set([b])

            return g

        mem = {}
        def cycle_exists(g, fast, q):
            if len(q) > 0 and q[0] == fast:
                return False
            elif fast not in g:
                return True
            elif fast in mem:
                return mem[fast]
            else:
                if len(q) > 0:
                    q.pop(0)
                fast1 = list(g[fast])
                for op1 in fast1:
                    if op1 in g:
                        fast2 = list(g[op1])
                        for op2 in fast2:
                            if not cycle_exists(g, op2, q + [op1, op2]):
                                return False
                mem[fast] = True
                return mem[fast]

        graph = build_graph(prerequisites)
        for root, children in list(graph.items()):
            if not cycle_exists(graph, root, []):
                return False

        return True
