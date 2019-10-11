#travelling salesman problem
import doctest
from itertools import permutations

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


def total_distance(points):
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


def travelling_salesman(points, start=None):
    if start is None:
        start = points[0]
    return min([perm for perm in permutations(points) if perm[0] == start], key=total_distance)


def optimized_travelling_salesman(points, start=None):
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path


doctest.testmod()
points = [[0, 0], [1, 5.7], [2, 3], [3, 7],
               [0.5, 9], [3, 5], [9, 1], [10, 5]]
print("""The minimum distance to visit all the following points: {}
starting at {} is {}.

The optimized algorithm yields a path long {}.""".format(
tuple(points),
points[0],
total_distance(travelling_salesman(points)),
total_distance(optimized_travelling_salesman(points))))
