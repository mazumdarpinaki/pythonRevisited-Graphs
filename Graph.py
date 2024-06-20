#adjacencyMatrix
"""
vertexData=['A','B','C','D']

adjacencyMatrix=[[0,1,1,1],[1,0,1,0],[1,1,0,0],[1,0,0,0]]

def print_AdjacencyMatrix(matrix):
	print("Adjacency Matrix")
	for row in matrix:
		print (row)

print ("vertex Data : ",vertexData)
print_AdjacencyMatrix(adjacencyMatrix)

def print_connections(matrix,vertices):
	print('\nconnections for each vertex: ')
	for i in range (len(vertices)):
		print(f'{vertices[i]}: ',end =' ')
		for j in range (len(vertices)):
			if matrix[i][j]:
				print(vertices[j],end=' ')
		print()
print_connections(adjacencyMatrix,vertexData)


#Graph implementation using class

	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

class Graph:
	def __init__(self,size):
		self.size=size;
		self.adj_matrix=[[0]*size for _ in range(size)]
		self.vertex_data=['']*size
	
	def add_edge(self,u,v):
		if 0<=u<self.size and 0<=v<self.size:
			self.adj_matrix[u][v]=1
			self.adj_matrix[v][u]=1

	def add_vertex_data(self,vertex,data):
		if 0<=vertex<self.size:
			self.vertex_data[vertex]=data
		
	def print_graph(self):
		print("Adjacency matrix :")
		for row in self.adj_matrix:
			print(' '.join(map(str,row)))
		print("\nVertex data")
		for vertex ,data in enumerate(self.vertex_data):
			print(f'Vertex {vertex} : {data}')

		


g=Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2)

g.add_vertex_data(0,'A')
g.add_vertex_data(1,'B')
g.add_vertex_data(2,'C')
g.add_vertex_data(3,'D')

g.print_graph()

#implementation of directed and weighted graph
class Graph:
	def __init__(self,size):
		self.size=size
		self.adj_matrix=[[0]*size for _ in range(size)]
		self.vertex_data=[' ']*size

	def add_edge(self,u,v,weight):
		if 0<=u<self.size and 0<=v<self.size:
			self.adj_matrix[u][v]=weight
	def add_vertex_data(self,vertex,data):
		if 0<=vertex<self.size:
			self.vertex_data[vertex]=data

	def print_graph(self):
		print("Adjacency matrix")
		for row in self.adj_matrix:
			print(" ".join(map(lambda x: str(x) if  x is not None else '0',row)))
		print('\nVertex data')
		for vertex,data in enumerate(self.vertex_data):
			print(f'Vertex {vertex}: {data}')


g=Graph(4)
g.add_edge(0,1,3)
g.add_edge(0,2,2)
g.add_edge(3,0,4)
g.add_edge(2,1,1)

g.add_vertex_data(0,'A')
g.add_vertex_data(1,'B')
g.add_vertex_data(2,'C')
g.add_vertex_data(3,'D')

g.print_graph()

"""

# DFS code
class Graph():
	def __init__(self,size):
		self.size=size
		self.adj_matrix=[[0]*size for _ in range (self.size)]
		self.vertex_data=[' ']*self.size
		
	def add_edge(self,u,v):
		if 0<=u<self.size and 0<=v<self.size:
			self.adj_matrix[u][v]=1
			#self.adj_matrix[v][u]=1   # hide for directed graph
		
	def add_vertex_data(self,v,data):
		if 0<=v<self.size:
			self.vertex_data[v]=data
		
	def print_graph(self):
		print("Adjacency matrix")
		for row in self.adj_matrix:
			print(' '.join(map(str,row)))
		
		print("\nVertex Data")
		for vertex,data in enumerate(self.vertex_data):
			print(f'Vertex {vertex}: {data}')

		
	def dfs_util(self,v,visited):
		visited[v]=True
		print(self.vertex_data[v],end = ' ')
		for i in range (self.size):
			if self.adj_matrix[v][i]==1 and not visited[i]:
				self.dfs_util(i,visited)

		
	def dfs(self,start_vertex_data):
		visited=[False]*self.size
		start_vertex_index=self.vertex_data.index(start_vertex_data)
		self.dfs_util(start_vertex_index,visited)


		
#BFS-Breadth First Search	

	def bfs(self,start_vertex_data):
		queue=[self.vertex_data.index(start_vertex_data)]
		visited=[False]*self.size
		visited[queue[0]]=True

		while queue:
			start_vertex_index=queue.pop(0)
			print(self.vertex_data[start_vertex_index],end=' ')
			for i in range (self.size):
				if self.adj_matrix[start_vertex_index][i]==1 and not visited[i]:
					queue.append(i)
					visited[i]=True


#DFS Cycle detection for undirected graphs

	def dfs_util_cycle(self,v,visited,parent):
		visited[v]=True
		for i in range(self.size):
			if self.adj_matrix[v][i]==1:
				if not visited[i]:
					if self.dfs_util_cycle(i,visited,parent):
						return True
				elif parent !=i:
					return True
		return False
		
	def is_Cycle(self):
		visited=[False]*self.size

		for i in range (self.size):
			if not visited[i]:
				if self.dfs_util_cycle(i,visited,-1):
					return True
		return False

	#DFS Cycle detection for directed graphs
		
	
	def dfs_util_cycle_dir(self,v,visited,recStack):
		visited[v]=True
		recStack[v]=True

		for i in range(self.size):
			if self.adj_matrix[v][i]:
				if not visited[i]:
					if self.dfs_util_cycle_dir(i,visited,recStack):
						return True
				elif recStack[i]:
					return True
		recStack[v]=False
		return False

	def is_Cycle(self):
		visited=[False]*self.size
		recStack=[False]*self.size

		for i in range(self.size):
			if not visited[i]:
				print()
				if self.dfs_util_cycle_dir(i,visited,recStack):
					return True

		return False
	
		
		
		


"""		
g=Graph(7)
g.add_vertex_data(0,'A')
g.add_vertex_data(1,'B')
g.add_vertex_data(2,'C')
g.add_vertex_data(3,'D')
g.add_vertex_data(4,'E')
g.add_vertex_data(5,'F')
g.add_vertex_data(6,'G')	

g.add_edge(0,2) #A-C
g.add_edge(0,3)	#A-D
g.add_edge(3,0)	#D-A
g.add_edge(0,4)	#A-E
g.add_edge(2,1)	#C-B
g.add_edge(2,5)	#C-F
g.add_edge(2,6)	#C-G
g.add_edge(2,4)	#C-E
g.add_edge(1,5)	#B-F

g.print_graph()

print('\nDepth first search starting from vertex D')
g.dfs('D')
print()

print('\nBreadth first search starting from vertex D')
g.bfs('D')
print()

print("\nGraph has cycle:", g.is_Cycle())
print()

"""


#DFS Cycle detection for directed graphs
		
	
	
g = Graph(7)

g.add_vertex_data(0,'A')
g.add_vertex_data(1,'B')
g.add_vertex_data(2,'C')
g.add_vertex_data(3,'D')
g.add_vertex_data(4,'E')
g.add_vertex_data(5,'F')
g.add_vertex_data(6,'G')	


g.add_edge(3, 0)  # D -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 1)  # C -> B
g.add_edge(2, 4)  # C -> E
g.add_edge(1, 5)  # B -> F
g.add_edge(4, 0)  # E -> A
g.add_edge(2, 6)  # C -> G

g.print_graph()

print("Graph-Directed has cycle:", g.is_Cycle())
































