from Cluster import Cluster
from Point import Point
import numpy as np
import math
from sklearn import datasets


def removeNeighbour(item):
    if item in neighbours:
        neighbours.remove(item)


def removePoint(item, list):
    if item in list:
        unvisited_points.remove(item)


def distance(first, second):
    return math.sqrt(
        ((first.x() - second.x()) ** 2) +
        ((first.y() - second.y()) ** 2) +
        ((first.z() - second.z()) ** 2) +
        ((first.o() - second.o()) ** 2)
    )


"""
load dataset
"""
iris = datasets.load_iris()
#print(iris.data)
dataset = iris.data

epsilon = 0.39
minPoints = 4

clusters = []


points = []
unvisited_points = []
noise_points = []

for data in dataset:
    p = Point(data[0], data[1], data[2], data[3])
    points.append(p)
    unvisited_points.append(p)

while len(unvisited_points) > 0:
    neighbours = []


    start_point_index = np.random.randint(0, len(unvisited_points))
    start_point = unvisited_points[start_point_index]

    start_point.setVisited(True)
    if start_point in unvisited_points:
        unvisited_points.remove(start_point)


    for point in points:
        if distance(point, start_point) <= epsilon:
            neighbours.append(point)

    removeNeighbour(start_point)


    if len(neighbours) < minPoints:
        noise_points.append(start_point)
        removePoint(start_point, unvisited_points)

    else:
      


        cluster = Cluster()

        cluster.addPoints(neighbours)
        cluster.addPoint(start_point)
        clusters.append(cluster)

  
        while len(neighbours) > 0:
    
            selected_neighbour = neighbours.pop()


            cluster.addPoint(selected_neighbour)

            removePoint(selected_neighbour, unvisited_points)
            selected_neighbour.setVisited(True)

            for point_1 in points:
                if point_1.getVisited() == False and distance(point_1, selected_neighbour) <= epsilon:
                    neighbours.append(point_1)


print("Epsilon: {}" . format(epsilon))
print("MinPoints: {}" . format(minPoints), end='\n\n')

print("Cluster count: {}" . format(len(clusters)))

cluster_count = 0

rates = []

for cluster in clusters:
    cluster_count += 1
    print("Cluster {}th: {}" . format(cluster_count, len(cluster.points())))
    rates.append(len(cluster.points()))

print("Noise count: {}" . format(len(noise_points)), end='\n\n')
