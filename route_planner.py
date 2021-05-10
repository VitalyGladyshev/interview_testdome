""" +
Route Planner

Back to questions
As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable,
before using more computationally intensive procedures for finding the optimal route.
The roads on the map are rasterized and produce a matrix of boolean values - True if the road is present
or False if it is not. The roads in the matrix are connected only if the road is immediately left, right,
below or above it.
Finish the route_exists method so that it returns True if the destination is reachable or False if it is not.
The from_row and from_column parameters are the starting row and column in the map_matrix.
The to_row and to_column are the destination row and column in the map_matrix.
The map_matrix parameter is the above mentioned matrix produced from the map.

For example, for the given rasterized map, the code below should return True since the destination is reachable:

map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

route_exists(0, 0, 2, 2, map_matrix)
"""

from collections import deque


def route_exists(from_row, from_column, to_row, to_column, grid):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def get_neighbours(row_nb, col_nb):
        for row_difference, col_difference in directions:
            new_row = row_nb + row_difference
            new_col = col_nb + col_difference
            if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                continue
            if not grid[new_row][new_col]:
                continue
            yield new_row, new_col

    if not grid[from_row][from_column] or not grid[to_row][to_column]:
        return False

    queue = deque([(from_row, from_column)])
    visited = {(from_row, from_column)}
    current_distance = 1

    while queue:
        nodes_of_current_distance = len(queue)
        for _ in range(nodes_of_current_distance):
            row, col = queue.popleft()
            if (row, col) == (to_row, to_column):
                return True
            for neighbour in get_neighbours(row, col):
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                queue.append(neighbour)
        current_distance += 1

    return False


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ]

    print(route_exists(0, 0, 2, 2, map_matrix))
