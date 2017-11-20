class Graph:
    def __init__(self, dict=None, directed=True):
        self.dict = dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """
        Convert a directed graph into undirected by adding symmetric edges
        """
        for a in list(self.dict.keys()):
            for(b, dist) in self.dict[a].items():
                self.__connect(b, a, dist)

    def __connect(self, a, b, dist):
        """
        Add one way edge between a and b
        """
        self.dict.setdefault(a, {})[b] = dist

    def connect(self, a, b, distance=1):
        self.__connect(a, b, distance)
        if not directed:
            self.__connect(b, a, distance)
