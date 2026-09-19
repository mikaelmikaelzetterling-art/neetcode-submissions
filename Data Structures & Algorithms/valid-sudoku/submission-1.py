class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rader
        for row in range(9):
            seen = set()

            for value in board[row]:
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Kolumner
        for col in range(9):
            seen = set()

            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # 3x3-boxar
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        value = board[row][col]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True