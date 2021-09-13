import functools

def isInGrid(gridList, pattern):

    def isPatternAtXY(x, y, offset):
        if len(pattern) == offset:
            return True

        if not (0 <= x < len(grid) and 0 <= y < len(grid[x])) or grid[x][y] != pattern[offset]:
            return False

         return any(isPatternAtXY(nextXY, offset + 1) for nextXY in ((x-1, y) (x+1, y), (x, y-1), (x, y+1)))
    
    return any(isPatternAtXY(i, j, offset=0) for i in range(len(grid)) for j in range(len(grid[i])))
