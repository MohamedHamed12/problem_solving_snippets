@classmethod
def bipartite_graph(cls, n, edges, zero_index_edges=True):
        class BipartiteGraph(cls):
            def __init__(self, n=n, edges=edges, zero_index_edges=zero_index_edges):
                """attribute bipartite graph"""
                super().__init__(n=2*n)
                self.m = n
                for u, v in edges:
                    if not zero_index_edges:
                        u -= 1
                        v -= 1
                    self.unite(u, v+self.m)
                    self.unite(u+self.m, v)
                self.is_bipartite_graph = all([not self.same(u, u+self.m) for u in range(self.m)])
                return
 
            def get_bipartite_members(self) -> dict:
                """
                Return:
                -------
                dict : {parent: {0: set, 1: set}}
                    A connected graph containing a `parent` node and two groups of nodes.
                """
                m = self.m
                if self.is_bipartite_graph:
                    bipartite_members = {x: {0: set(), 1: set()} for x in self.get_parents() if x < self.m}
                    for x in self.nodes:
                        if self.find(x) < self.m:
                            bipartite_members[self.find(x)][x>=self.m].add(x%self.m)
                    return bipartite_members
                else:
                    # this graph is not bipartite graph!!
                    return None
 
            def get_members(self):
                members = {x: set([]) for x in self.get_parents() if x < self.m}
                for x in self.nodes:
                    if self.find(x) < self.m:
                        members[self.find(x)].add(x%self.m)
                return members
 
            def get_parents(self):
                return set([x for x in self._parents_set if x < self.m])
 
        return BipartiteGraph(n, edges, zero_index_edges)
 