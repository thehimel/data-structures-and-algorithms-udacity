
"""
Route Planner

Build a route-planner algorithm like the one used in Google Maps to calculate
the shortest path between two points on a map.

Given the coordinates of locations as map.interactions and roads as map.roads.
Using A* algorithm, find the shortest path between 2 locations on the map.
"""

import math
import heapq


def get_xy(xy):
    return xy[0], xy[1]


def distance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return d


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __eq__(self, other):
        return self.value == other.value

    # Need this comparison to implement the priority queue
    def __lt__(self, other):
        return self.priority < other.priority


def find_path(predecessor, start, goal):
    present = goal
    path = []

    while start != present:
        path.append(present)
        present = predecessor[present]

    # Finally add the start
    path.append(start)

    # Get list from start to goal
    path.reverse()

    return path


def shortest_path(M, start, goal):

    frontier = []
    heapq.heapify(frontier)

    insec = M.intersections
    roads = M.roads

    start_node = Node(start, 0)
    goal_node = Node(goal, 0)
    heapq.heappush(frontier, start_node)

    source = {}
    source[start] = None

    present_cost = {}
    present_cost[start] = 0

    while len(frontier) > 0:
        node = heapq.heappop(frontier)

        if node == goal_node:
            break

        for next_road in roads[node.value]:
            x, y = get_xy(insec[node.value])
            next_x, next_y = get_xy(insec[next_road])
            g = present_cost[node.value] + distance(x, y, next_x, next_y)

            explored = present_cost.keys()

            if next_road not in explored or g < present_cost[next_road]:
                present_cost[next_road] = g

                goal_x, goal_y = get_xy(insec[goal])
                h = distance(goal_x, goal_y, next_x, next_y)
                f = g + h

                next_node = Node(next_road, f)
                heapq.heappush(frontier, next_node)
                source[next_road] = node.value

    return find_path(source, start, goal)
