class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # loop through each row and check if numbers 1-9. if duplicates, return false
            # if true, check columns
            # loop through each column and check if numbers 1-9. if duplicates false
                # if true, check each 3x3 for duplicates

        # check rows
        for i in range(len(board)):
            duplicates = {}
            for num in board[i]:
                if num == ".":
                    continue
                else:
                    duplicates[num] = duplicates.get(num, 0) + 1
        
            for n, c in duplicates.items():
                if c > 1:
                    return False
        
        # check columns
        for i in range(len(board[0])):
            duplicates = {}
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    duplicates[board[j][i]] = duplicates.get(board[j][i], 0) + 1
        
            for n, c in duplicates.items():
                if c > 1:
                    return False
                
        # check squares
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):

                duplicates = {}

                for r in range(boxRow, boxRow + 3):
                    for c in range(boxCol, boxCol + 3):

                        value = board[r][c]

                        if value == ".":
                            continue
                        else:
                            duplicates[value] = duplicates.get(value, 0) + 1
                
                for n, c in duplicates.items():
                    if c > 1:
                        return False
            
        return True
            