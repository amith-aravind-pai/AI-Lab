import copy

class PuzzleState:
    def __init__(self, board, g=0, h=0, parent=None):
        self.board = board
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

def find_coord(tile, board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == tile:
                return (r, c)
    return None

def manhattan_distance(board, goal_board):
    total_cost = 0
    for tile in range(1, 9):
        c_c = find_coord(tile, board)
        g_c = find_coord(tile, goal_board)
        if c_c and g_c:
            total_cost += abs(c_c[0] - g_c[0]) + abs(c_c[1] - g_c[1])
    return total_cost

def misplaced_tiles(board, goal_board):
    total_cost = 0
    for tile in range(1, 9):
        c_c = find_coord(tile, board)
        g_c = find_coord(tile, goal_board)
        if c_c != g_c:
            total_cost += 1
    return total_cost

def get_neighbors(state):
    neighbors = []
    r, c = find_coord(0, state.board)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_board = copy.deepcopy(state.board)
            new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
            neighbors.append(new_board)
    return neighbors

def print_board(board):
    for row in board:
        print(" ".join(str(val) if val != 0 else " " for val in row))
    print("-" * 10)

def solve_8_puzzle(initial_board, goal_board, heuristic_fn):
    start_state = PuzzleState(initial_board, g=0, h=heuristic_fn(initial_board, goal_board))
    
    open_list = [start_state]
    visited = set()
    
    while open_list:
        open_list.sort(key=lambda state: state.f)
        current_state = open_list.pop(0)
        
        board_tuple = tuple(tuple(row) for row in current_state.board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        
        if current_state.board == goal_board:
            path = []
            curr = current_state
            while curr:
                path.append(curr.board)
                curr = curr.parent
            return path[::-1], len(visited)
            
        for nb_board in get_neighbors(current_state):
            nb_tuple = tuple(tuple(row) for row in nb_board)
            if nb_tuple not in visited:
                g = current_state.g + 1
                h = heuristic_fn(nb_board, goal_board)
                child_state = PuzzleState(nb_board, g=g, h=h, parent=current_state)
                open_list.append(child_state)
                
    return None, len(visited)

initial_board = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal_board = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

print("=== Solving 8-Puzzle with Manhattan Distance ===")
path, nodes_visited = solve_8_puzzle(initial_board, goal_board, manhattan_distance)

if path:
    print(f"Solution found in {len(path) - 1} moves (Visited {nodes_visited} states):\n")
    for step, board in enumerate(path):
        print(f"Move {step}:")
        print_board(board)
else:
    print("No solution found.")