import random

def euclideanDistance(point0, point1):
    return ((point0[0] - point1[0])**2 + (point0[1] - point1[1])**2) ** 0.5


points = [(1,1), (2,1), (3,1), (4,1), (5,1)]
temp_points = [point for point in points]

distances = []
for point0 in temp_points:
    temp_points.remove(point0)
    for point1 in temp_points:
        distances.append(euclideanDistance(point0, point1))
        
print(distances)
print(f"Minimum distance = {min(distances)}")