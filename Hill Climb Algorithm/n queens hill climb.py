def count_incremental_conflicts(partial_state, next_queen_row):
    conflicts = 0
    next_col = len(partial_state)
    for col, row in enumerate(partial_state):
        if row == next_queen_row:
            conflicts += 1
        elif abs(row - next_queen_row) == abs(col - next_col):
            conflicts += 1
    return conflicts

def solve_queens_incremental():
    partial_state = []
    n = 8
    
    for col in range(n):
        best_row = 0
        min_conflicts = float('inf')
        candidate_rows = list(range(n))
        random.shuffle(candidate_rows)
        
        for row in candidate_rows:
            conflicts = count_incremental_conflicts(partial_state, row)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_row = row
                
        partial_state.append(best_row)
        print(f"Column {col} placed at Row {best_row} (conflicts with existing: {min_conflicts})")
        
    return partial_state

print("=== Starting Incremental Greedy Placement ===")
final_state = solve_queens_incremental()
total_final_conflicts = calculate_conflicts(final_state)
print(f"\nFinal Board State: {final_state}")
print(f"Total board conflicts: {total_final_conflicts}")
if total_final_conflicts == 0:
    print("Successfully found a perfect solution using incremental greedy construction!")
else:
    print("Constructed state contains some conflicts due to the greedy nature (no backtracking used).")

print("\nVisualizing the resulting board:")
print_board(final_state)