class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows=len(board)
        cols=len(board[0])
        cnt=0
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='X':
                    if (i==0 or board[i-1][j]!='X') and (j==0 or board[i][j-1]!='X'):
                        cnt+=1
        return cnt