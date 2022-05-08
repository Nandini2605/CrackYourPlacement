class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    letter, board[i][j] = board[i][j], -1
                    if self.backtrack(letter, 1, word, board, i, j):
                        return True
                    board[i][j] = letter
        return False
    
    def backtrack(self, letter, k, word, board, x, y):
        if k == len(word):
            return True
        else:
            for x1,y1 in ((x+1,y), (x-1,y), (x, y+1), (x, y-1)):
                if 0<=x1<len(board) and 0<=y1<len(board[0]) and board[x1][y1] == word[k]:
                    letter, board[x1][y1] = board[x1][y1], -1
                    if self.backtrack(letter, k+1, word, board, x1, y1):
                        return True
                    board[x1][y1] = letter
            return False
 
 
'''
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''
