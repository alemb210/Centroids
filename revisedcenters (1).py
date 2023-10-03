import csv
import math
import random

def coords_float(str):
	strArray = str.split(',')
	for x in range(len(strArray)):
		strArray[x] = 	float(strArray[x])
	return strArray

file = open("./coordinates.csv", "r")
coords = file.readlines()
numLines = len(coords)
print("There are ", numLines, " lines in this file.")
randomCoords = [] 
avgCoords = []
dists = []
tempDists = []
prevAssignedCentroids = []
assignedCentroids = []
sumSquaredDistances = 0
change = 1
iterations = 0

num = int(input("Please enter the number of clusters"))
for x in range(num):
	newCoords = coords_float(random.choice(coords))
	while(newCoords in randomCoords):
		newCoords = coords_float(random.choice(coords)) 
	randomCoords.append(newCoords)
	print(newCoords)

while change != 0:
	dists = []
	prevAssignedCentroids = assignedCentroids
	assignedCentroids = []
	sumSquaredDistances = 0
	for coord in coords:
		coord = coords_float(coord)
		#tempDists length is equal to the number of centroids. It is the distance to each centroid where the # coordinate pair is equivalent to the index + 1 
		if(tempDists != []):
			dists.append(tempDists)
		tempDists = []
		for centroid in randomCoords:
			#Creating a 2D array of each coordinate and its distance to each centroid.
			tempDists.append(math.dist(centroid, coord))
	for centDists in dists:
		#Creating another 2D array with the distance to closest centroid and the number of that centroid.
		assignedCentroids.append([min(centDists), (centDists.index(min(centDists)) + 1)])
		sumSquaredDistances += min(centDists) ** 2
#logging
	#for cent in assignedCentroids:
	#	print("Coordinate #", (assignedCentroids.index(cent) + 1), " ", coords[assignedCentroids.index(cent)], " is closest to Centroid ", cent[1])
	#find new centroids
	for i in range(num):
		latSum = 0
		longSum = 0 
		counter = 0
		loopCounter = 0
		#iterate to find all points that belong to the current cluster (cluster # = (i + 1)), then average 
		for cent in assignedCentroids:
			if cent[1] == (i + 1):
				latSum += coords_float(coords[loopCounter])[0]
				longSum += coords_float(coords[loopCounter])[1]
				counter += 1
			loopCounter += 1
		if counter != 0:
			avgCoords.append([(latSum/counter), (longSum/counter)])
		else:
			avgCoords.append(randomCoords[i])
	randomCoords = avgCoords
	avgCoords = []
#because both prevAssignedCentroids and assignedCentroids are initiated as [], this will only run after 1 iteration.
	if prevAssignedCentroids != []:
		iterations += 1
		change = 1
		#compare to see if any points changed clusters.
		for i in range(len(prevAssignedCentroids)):
			if prevAssignedCentroids[i][1] != assignedCentroids[i][1]:
				change += 1
		change = change - 1
		print(change, " points switched clusters.")
		print("New d2: ", sumSquaredDistances)
	iterations += 1
	print(iterations, " iterations")
