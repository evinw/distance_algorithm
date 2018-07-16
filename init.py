class nodes:
	def __init__(self, u, v, weight):
		self.u=u
		self.v=v
		self.weight=weight

graph=[]
graph.append(nodes(0, 1, 7))
graph.append(nodes(0, 2, 9))
graph.append(nodes(0, 3, 14))
graph.append(nodes(1, 2, 10))
graph.append(nodes(1, 5, 15))
graph.append(nodes(2, 3, 2))
graph.append(nodes(2, 5, 11))
graph.append(nodes(3, 4, 9))
graph.append(nodes(4, 5, 6))

vertex=range(6)
distance=range(6)
for i in distance:
	distance[i]=100

distance[0]=0
list1=distance

def min_dist(a):
	global graph, distance, vertex, dist,list1
	for each in graph:
		if each.u==a and distance[each.v]>(distance[a]+each.weight):
			distance[each.v]=(distance[a]+each.weight)
	print distance
	evin_distance()
	
def evin_distance():
	global vertex, distance
	while(vertex!=[]):
		x=smallest(distance)
		k=vertex[x]
		del vertex[x]
		min_dist(k)
	


def smallest(a):
	k = 0
	i = 1

	while i < len(a):
		if a[k]>a[i]:
			k=i
		i+=1

	return k

	
evin_distance()