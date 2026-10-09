board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")
    print()

def global_win_check(player):
    for i in range(3):
        if board[i].count(player) == 3 or [board[j][i] for j in range(3)].count(player) == 3:
            return True
    if [board[i][i] for i in range(3)].count(player) == 3 or [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    return False

def row_check(player, index):
    return board[index].count(player) == 2 and board[index].count(' ') == 1

def col_check(player, index):
    col = [board[i][index] for i in range(3)]
    return col.count(player) == 2 and col.count(' ') == 1

def diag_check(player, diag_id):
    diag = [board[i][i] for i in range(3)] if diag_id == 0 else [board[i][2-i] for i in range(3)]
    return diag.count(player) == 2 and diag.count(' ') == 1

def get_empty_col(row_index):
    return board[row_index].index(' ')

def get_empty_row(col_index):
    return [board[i][col_index] for i in range(3)].index(' ')

def get_empty_diag(diag_id):
    coords = [(i, i) for i in range(3)] if diag_id == 0 else [(i, 2-i) for i in range(3)]
    for r, c in coords:
        if board[r][c] == ' ':
            return r, c

def play_tic_tac_toe():
    for turn in range(9):
        print_board()

        if turn % 2 == 0:
            print("User's Turn:")
            x = int(input("Enter row (0-2): "))
            y = int(input("Enter col (0-2): "))

            if board[x][y] != ' ':
                print("Space taken! Choose another spot.")
                continue

            board[x][y] = 'X'

            if global_win_check('X'):
                print_board()
                print("User won!")
                return
            continue

        print("Bot's Turn:")
        bot_moved = False

        for j in range(3):
            if row_check('O', j):
                z = get_empty_col(j)
                board[j][z] = 'O'
                bot_moved = True
                break
            elif col_check('O', j):
                z = get_empty_row(j)
                board[z][j] = 'O'
                bot_moved = True
                break

        if not bot_moved:
            if diag_check('O', 0):
                r, c = get_empty_diag(0)
                board[r][c] = 'O'
                bot_moved = True
            elif diag_check('O', 1):
                r, c = get_empty_diag(1)
                board[r][c] = 'O'
                bot_moved = True

        if bot_moved and global_win_check('O'):
            print_board()
            print("Bot wins!")
            return

        if not bot_moved:
            for j in range(3):
                if row_check('X', j):
                    z = get_empty_col(j)
                    board[j][z] = 'O'
                    bot_moved = True
                    break
                elif col_check('X', j):
                    z = get_empty_row(j)
                    board[z][j] = 'O'
                    bot_moved = True
                    break

        if not bot_moved:
            if diag_check('X', 0):
                r, c = get_empty_diag(0)
                board[r][c] = 'O'
                bot_moved = True
            elif diag_check('X', 1):
                r, c = get_empty_diag(1)
                board[r][c] = 'O'
                bot_moved = True

        if not bot_moved:
            for r in range(3):
                for c in range(3):
                    if board[r][c] == ' ':
                        board[r][c] = 'O'
                        bot_moved = True
                        break
                if bot_moved:
                    break

    print_board()
    print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
