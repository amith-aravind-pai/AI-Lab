import time
import sys
from collections import deque

# Sample Tree Graph as depicted in image 3
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

def depth_limited_dfs(node, goal, limit, visited_nodes):
    visited_nodes.append(node)
    if node == goal:
        return True
    if limit <= 0:
        return False
    
    for neighbor in graph.get(node, []):
        if depth_limited_dfs(neighbor, goal, limit - 1, visited_nodes):
            return True
    return False

def iddfs(start, goal, max_depth=10):
    visited_order = []
    for depth in range(max_depth + 1):
        step_visited = []
        if depth_limited_dfs(start, goal, depth, step_visited):
            visited_order.extend(step_visited)
            return True, visited_order, depth
        visited_order.extend(step_visited)
    return False, visited_order, max_depth

def dfs(start, goal):
    stack = [start]
    visited_order = []
    max_space = 0
    
    while stack:
        max_space = max(max_space, len(stack))
        node = stack.pop()
        visited_order.append(node)
        
        if node == goal:
            return True, visited_order, max_space
            
        # Reverse to maintain left-to-right traversal order
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited_order:
                stack.append(neighbor)
                
    return False, visited_order, max_space

def bfs(start, goal):
    queue = deque([start])
    visited_order = []
    max_space = 0
    
    while queue:
        max_space = max(max_space, len(queue))
        node = queue.popleft()
        visited_order.append(node)
        
        if node == goal:
            return True, visited_order, max_space
            
        for neighbor in graph.get(node, []):
            if neighbor not in visited_order and neighbor not in queue:
                queue.append(neighbor)
                
    return False, visited_order, max_space

start_node = 'A'
goal_node = 'G'

print(f"Searching for goal '{goal_node}' starting from '{start_node}'...\n")

t0 = time.perf_counter()
found_iddfs, path_iddfs, found_depth = iddfs(start_node, goal_node)
t1 = time.perf_counter()
time_iddfs = (t1 - t0) * 1000

t0 = time.perf_counter()
found_dfs, path_dfs, space_dfs = dfs(start_node, goal_node)
t1 = time.perf_counter()
time_dfs = (t1 - t0) * 1000

t0 = time.perf_counter()
found_bfs, path_bfs, space_bfs = bfs(start_node, goal_node)
t1 = time.perf_counter()
time_bfs = (t1 - t0) * 1000

print(f"IDDFS Traversal Sequence : {' -> '.join(path_iddfs)} (Found at depth {found_depth})")
print(f"DFS Traversal Sequence   : {' -> '.join(path_dfs)}")
print(f"BFS Traversal Sequence   : {' -> '.join(path_bfs)}")
print("\n" + "="*60)
print(f"{'Algorithm':<10} | {'Time (ms)':<12} | {'Time Complexity':<18} | {'Space Complexity':<16}")
print("="*60)
print(f"{'BFS':<10} | {time_bfs:<12.4f} | {'O(b^d)':<18} | {'O(b^d)':<16}")
print(f"{'DFS':<10} | {time_dfs:<12.4f} | {'O(b^m)':<18} | {'O(b*m)':<16}")
print(f"{'IDDFS':<10} | {time_iddfs:<12.4f} | {'O(b^d)':<18} | {'O(b*d)':<16}")
print("="*60)
print("Where: b = branching factor, d = goal depth, m = maximum graph depth.")