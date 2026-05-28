class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # loop through each row and check if numbers 1-9. if duplicates, return false
            # if true, check columns
            # loop through each column and check if numbers 1-9. if duplicates false
                # if true, check each 3x3 for duplicates
        
        # use set trick

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = collections.defaultdict(set)

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                if (board[row][column] in rows[row] or 
                board[row][column] in columns[column] or 
                board[row][column] in squares[(row//3, column//3)]):
                    return False
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                squares[(row//3, column//3)].add(board[row][column])
        
        return True
