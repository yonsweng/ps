from collections import deque
from itertools import permutations
from sys import stdin


def bfs_shortest_path(grid, start, end, N):
    """BFS to find shortest path distance between two points"""
    if start == end:
        return 0
    
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if (nx, ny) == end:
                    return dist + 1
                
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    
    return float('inf')  # No path found


def find_optimal_path(grid, H, groups, sharp, N):
    """Find optimal ordering for each group to minimize total path length"""
    best_paths = {}
    best_distances = {}
    
    for group_name, positions in groups.items():
        best_dist = float('inf')
        best_order = None
        
        # Try all permutations of the group
        for perm in permutations(positions):
            total_dist = 0
            current_pos = H
            
            # Calculate path through this permutation
            for next_pos in perm:
                dist = bfs_shortest_path(grid, current_pos, next_pos, N)
                if dist == float('inf'):
                    total_dist = float('inf')
                    break
                total_dist += dist
                current_pos = next_pos
            
            # Add distance from last position to #
            if total_dist != float('inf'):
                final_dist = bfs_shortest_path(grid, current_pos, sharp, N)
                if final_dist != float('inf'):
                    total_dist += final_dist
                else:
                    total_dist = float('inf')
            
            # Update best if this is better
            if total_dist < best_dist:
                best_dist = total_dist
                best_order = perm
        
        best_paths[group_name] = best_order
        best_distances[group_name] = best_dist
    
    return best_paths, best_distances


def solve():
    N = int(stdin.readline().strip())
    m = [list(stdin.readline().strip()) for _ in range(N)]
    H = (0, 0)
    sharp = (0, 0)
    W, C, B, J = [], [], [], []
    
    for i in range(N):
        for j in range(N):
            if m[i][j] == 'H':
                H = (i, j)
            elif m[i][j] == '#':
                sharp = (i, j)
            elif m[i][j] == 'W':
                W.append((i, j))
            elif m[i][j] == 'C':
                C.append((i, j))
            elif m[i][j] == 'B':
                B.append((i, j))
            elif m[i][j] == 'J':
                J.append((i, j))
    
    # Group the positions
    groups = {'W': W, 'C': C, 'B': B, 'J': J}
    
    # Find optimal paths
    best_paths, best_distances = find_optimal_path(m, H, groups, sharp, N)
    
    # Store results
    Wd = best_distances['W']
    Cd = best_distances['C'] 
    Bd = best_distances['B']
    Jd = best_distances['J']
    
    # Find minimum distance and print corresponding class
    min_distance = min(Wd, Cd, Bd, Jd)
    
    if Jd == min_distance:
        print("Assassin")
    elif Cd == min_distance:
        print("Healer")
    elif Bd == min_distance:
        print("Mage")
    elif Wd == min_distance:
        print("Tanker")


if __name__ == "__main__":
    solve()
