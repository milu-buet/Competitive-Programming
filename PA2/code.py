# Md Lutfar Rahman
# mrahman9@memphis.edu
# U00621586 



from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
import numpy 
import matplotlib.pyplot as plt
import math


def getPoints():
	points = []
	f = open('points')
	for line in f.readlines():
		p = line.split()
		x = float(p[0])
		y = float(p[1])
		points.append([x,y])

	return numpy.array(points)



###############################################################
def dist(p1,p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def check2PEdge(points, vor, min_v, i, j):
	for edge in vor.ridge_vertices:
			c1 = min_v == edge[0] and edge[1] > -1 and dist(vor.vertices[edge[1]], points[i]) == dist(vor.vertices[edge[1]], points[j])
			c2 = min_v == edge[1] and edge[0] > -1 and dist(vor.vertices[edge[0]], points[i]) == dist(vor.vertices[edge[0]], points[j])
			if c1 or c2:
				print("edge: %s -- %s"%(vor.vertices[edge[0]], vor.vertices[edge[1]]))
				return edge
	return None


def checkInfEdge(points, vor, min_v, i, j):
	for edge in vor.ridge_vertices:
			c1 = min_v == edge[0] and edge[1] == -1
			c2 = min_v == edge[1] and edge[0] == -1 
			if c1 or c2:
				print("Inf edge: %s -- %s"%(-1, vor.vertices[edge[1]]))
				return edge
	return None


def getMinV(points, vor, i, j):
	min_dist = math.inf
	min_v = None
	for k, vv in enumerate(vor.vertices):
		if dist(vv, points[i]) == dist(vv, points[j]) and  dist(vv, points[i]) <= min_dist:
			min_dist = dist(vv, points[i])
			min_v = k
	return min_v,min_dist



#Solves problem I
def I(points, vor, i,j):
	#print(vor.ridge_vertices)
	#print(vor.vertices)
	#fig = voronoi_plot_2d(vor)
	#fig.show()

	min_v,min_dist = getMinV(points, vor, i, j)

	if min_v is None:
		print("NO")
		return False
	else:
		Edge2P = check2PEdge(points, vor, min_v, i, j)
		if Edge2P:
			#print(Edge2P)
			print("Yes")
			return True

		EdgeInf = checkInfEdge(points, vor, min_v, i, j)
		if EdgeInf:
			#print(EdgeInf)
			print("Yes")
			return True
		else:
			print("NO")
			return False
#######################################################################################
#Solves problem II
def II(points, tri, px, py):
	pass
	#print(tri.simplices)


	to_search = numpy.array([[px,py]])
	inds = tri.find_simplex(to_search)
	#print(inds)
	if inds[0] > 0:
		triangle = tri.simplices[inds[0]]
		p0 = points[triangle[0]]
		p1 = points[triangle[1]]
		p2 = points[triangle[2]]
		print(p0,p1,p2)
	else:
		print("OUT OF TRIANGULATION")

	#plt.triplot(points[:,0], points[:,1], tri.simplices)
	#plt.plot(points[:,0], points[:,1], 'o')
	#plt.show()



#points = getPoints()
#vor = Voronoi(points)
#I(points, vor, 0, 3)
#print(vor.__dict__)

#tri = Delaunay(points)
#II(points, tri, .5, .6)



# fig = voronoi_plot_2d(vor)
# fig.show()

# tri = Delaunay(points)
# plt.triplot(points[:,0], points[:,1], tri.simplices)
# plt.plot(points[:,0], points[:,1], 'o')
# plt.show()

#print(vor)




if __name__ == "__main__":
	points = getPoints()
	vor = Voronoi(points)
	tri = Delaunay(points)

	while True:
		I_or_II = input("I=Voroni, II=Delauney, x=Exit:")
		print(I_or_II)

		if I_or_II == 'I':
			p = input("i,j=").split(",")
			i = int(p[0])
			j = int(p[1])
			I(points, vor,i,j)

		elif I_or_II == 'II':
			p = input("px,py=").split(",")
			px = float(p[0])
			py = float(p[1])
			II(points, tri, px, py)

		else:
			break

    
