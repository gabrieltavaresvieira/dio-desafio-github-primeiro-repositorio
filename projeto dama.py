class Board:
    def __init__(self):
        self.board = [[0, 2, 0, 2, 0, 2, 0, 2],
                      [2, 0, 2, 0, 2, 0, 2, 0],
                      [0, 2, 0, 2, 0, 2, 0, 2],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0]]

    def print_board(self):
        for i in range(8):
            print(self.board[i])

    def move_piece(self, from_pos, to_pos):
        from_row, from_col = map(int, from_pos.split(","))
        to_row, to_col = map(int, to_pos.split(","))

        piece = self.board[from_row][from_col]
        if piece == 0:
            print("Não há peça na posição de origem.")
            return False

        if self.board[to_row][to_col] != 0:
            print("A posição de destino já está ocupada.")
            return False

        if piece == 1 and to_row > from_row:
            print("Peças brancas só podem se mover para cima.")
            return False

        if piece == 2 and to_row < from_row:
            print("Peças pretas só podem se mover para baixo.")
            return False

        if abs(from_row - to_row) == 1 and abs(from_col - to_col) == 1:
            # Movimento simples
            self.board[from_row][from_col] = 0
            self.board[to_row][to_col] = piece
        elif abs(from_row - to_row) == 2 and abs(from_col - to_col) == 2:
            # Movimento com captura
            middle_row = (from_row + to_row) // 2
            middle_col = (from_col + to_col) // 2

            middle_piece = self.board[middle_row][middle_col]
            if middle_piece == 0 or middle_piece == piece:
                print("Não há peça para ser capturada.")
                return False

            self.board[from_row][from_col] = 0
            self.board[middle_row][middle_col] = 0
            self.board[to_row][to_col] = piece
        else:
            print("Movimento inválido.")
            return False

        return True
