class State:
    '''
    Represents the state of the app.

    Currently, it is just a board with a cursor. Simple enough.
    '''
    def __init__(self, height: int, width: int):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.cursor = (self.height // 2, self.width // 2)

    # State setters:
    def set_cursor_at(self, i: int, j: int):
        self.cursor = (i, j)

    def move_cursor_by(self, di: int, dj: int):
        '''Moves cursor by an offset, but also keeps it in bound.'''
        old_i, old_j = self.cursor
        new_i = max(0, min(self.height - 1, old_i + di))
        new_j = max(0, min(self.width - 1, old_j + dj))
        self.cursor = (new_i, new_j)

    def set_char(self, char: str):
        i, j = self.cursor
        self.board[i][j] = char

    def reset_char(self):
        i, j = self.cursor
        self.board[i][j] = None

    def put_char_and_proceed_cursor(self, char: str):
        self.set_char(char)
        self.move_cursor_by(0, +1)

    def paste_from_string(self, string: str):
        '''Puts a block (as a string) at `self.cursor` (left-top aligned).'''
        block = string.splitlines()
        
        off_i, off_j = self.cursor
        for src_i, row in enumerate(block):
            dst_i = src_i + off_i
            if dst_i >= self.height:
                break
            for src_j, char in enumerate(row):
                dst_j = src_j + off_j
                if dst_j >= self.width:
                    break
                self.board[dst_i][dst_j] = char

    def clear_board(self):
        self.board = [[None] * self.width for _ in range(self.height)]

    # State getters:
    def is_empty(self, i, j):
        c = self.board[i][j]
        return not (c and c != ' ')

    def copy_to_string(self) -> str:
        '''Copy the board (as a smallest block) into a string, 
        triming away the spaces.'''

        non_empty_rows = [i for i in range(self.height) if any(
            not self.is_empty(i, j) for j in range(self.width)
        )]
        if len(non_empty_rows) == 0:
            return []
        i_start, i_end = non_empty_rows[0], non_empty_rows[-1] + 1

        non_empty_cols = [j for j in range(self.width) if any(
            not self.is_empty(i, j) for i in range(i_start, i_end)
        )]
        j_start, j_end = non_empty_cols[0], non_empty_cols[-1] + 1

        block = ["".join(c or ' ' for c in row[j_start : j_end]
            ) for row in self.board[i_start : i_end]
        ]
        return "\n".join(block)
