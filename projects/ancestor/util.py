class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set() # returns a sorted, non repeating collection like a list or dictionary, if no given iterable parameter is provided, it makes an empty set
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """     
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        # Create and empty Set to store the visited vertices
        visited = set()
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:    
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:    
                # Mark is as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        return visited

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                self.dft_recursive(child_vertex, visited)

    
    # def dft_recursive(self, starting_vertex, visited=set()):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.
    #     This should be done using recursion.
    #     """
    #     if starting_vertex not in visited:
    #         visited.add(starting_vertex)
    #         print(starting_vertex)
    #         for neighbor in self.vertices[starting_vertex]:
    #             self.dft_recursive(neighbor, visited)
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        visited = set()
        qq.enqueue([starting_vertex])
        while qq.size() > 0:
            path = qq.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path) # create deep copy instead of ref
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

