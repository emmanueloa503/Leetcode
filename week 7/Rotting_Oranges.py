class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) 
                elif grid[r][c] == 1:
                    fresh_count += 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        time_elapsed = 0

        while queue:
            r, c, time_elapsed = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, time_elapsed + 1))

        if fresh_count > 0:
            return -1
        return time_elapsed
       