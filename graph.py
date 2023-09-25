class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_gr(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_gr()
