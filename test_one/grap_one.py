class NewGraph:
    def __init__(self):
        self.my_graph = {}

    def _print_g(self):
        for x in self.my_graph:
            print(x, ':', self.my_graph[x])

    def _add_vertex(self, vertex):
        if vertex not in self.my_graph.keys():
            self.my_graph[vertex] = []
            return True
        return False

    def _add_edge(self, v1, v2):
        if v1 in self.my_graph.keys() and v2 in self.my_graph.keys():
            self.my_graph[v1].append(v2)
            self.my_graph[v2].append(v1)
            return True
        return False

    def _remove_edge(self, v1, v2):
        if v1 in self.my_graph.keys() and v2 in self.my_graph.keys():
            try:
                self.my_graph[v1].remove(v2)
                self.my_graph[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def _remove_vertex(self, vertex):
        if vertex in self.my_graph.keys():
            for new_vx in self.my_graph[vertex]:
                self.my_graph[new_vx].remove(vertex)
            del self.my_graph[vertex]
            return True
        return False


new_gr = NewGraph()
new_gr._add_vertex('A')
new_gr._add_vertex('B')
new_gr._add_vertex('C')
new_gr._add_vertex('D')

new_gr._add_edge('A', 'B')
new_gr._add_edge('A', 'C')
new_gr._add_edge('A', 'D')
new_gr._add_edge('B', 'D')
new_gr._add_edge('C', 'D')

new_gr._remove_vertex('D')

new_gr._print_g()
