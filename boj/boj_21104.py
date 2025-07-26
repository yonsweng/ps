from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())
    minerals = []
    for _ in range(n):
        l, r = map(int, stdin.readline().split())
        minerals.append((l, r))
    positions = []
    for _ in range(m):
        a = int(stdin.readline().strip())
        positions.append(a)

    # Create events for sweep line algorithm
    events = []
    for j, (left, right) in enumerate(minerals):
        events.append((left, 1, j))    # mineral starts
        events.append((right, -1, j))  # mineral ends (right+1 to handle inclusive range)
    
    # Add position queries
    for i, pos in enumerate(positions):
        events.append((pos, 0, i))
    
    # Sort events by position
    events.sort(key=lambda x: (x[0], -x[1]))
    
    # Sweep line to find overlaps
    MOD = 998244353
    answer = 0
    previous_minerals = set()
    additional_minerals = set()
    disappeared_minerals = set()
    current_power = 1  # pow(2, 0, MOD) = 1
    intersection_power = 1  # pow(2, 0, MOD) = 1, tracks intersection incrementally
    
    for pos, event_type, idx in events:
        if event_type == 1:  # mineral starts
            if idx in disappeared_minerals:
                # Mineral was previously active but disappeared, now it's back
                disappeared_minerals.discard(idx)
                intersection_power = (intersection_power * 2) % MOD  # This mineral is back in intersection
            elif idx not in previous_minerals:
                # New mineral not seen before
                additional_minerals.add(idx)
            # Mineral is now active, update current_power
            current_power = (current_power * 2) % MOD  # multiply by 2 for each new mineral
        elif event_type == -1:  # mineral ends
            if idx in additional_minerals:
                # Mineral was added in this sweep, now it's gone
                additional_minerals.discard(idx)
            elif idx in previous_minerals:
                # Mineral was in previous state, now it's disappeared
                disappeared_minerals.add(idx)
                intersection_power = (intersection_power * pow(2, MOD - 2, MOD)) % MOD  # This mineral is no longer in intersection
            # Mineral is no longer active, update current_power
            current_power = (current_power * pow(2, MOD - 2, MOD)) % MOD  # divide by 2 using modular inverse
        else:  # position query (event_type == 0)
            answer = (answer + current_power - intersection_power) % MOD
            
            # Update previous_minerals for next query without copying
            # Move minerals from additional_minerals to previous_minerals
            previous_minerals.update(additional_minerals)
            # Remove disappeared minerals from previous_minerals
            previous_minerals.difference_update(disappeared_minerals)
            
            # Update intersection_power for next query: all current minerals will be in next intersection
            # intersection_power = pow(2, len(previous_minerals), MOD)
            # We can calculate this incrementally: multiply by 2 for each additional mineral
            for _ in additional_minerals:
                intersection_power = (intersection_power * 2) % MOD
            
            # Reset tracking sets
            additional_minerals.clear()
            disappeared_minerals.clear()

    print(answer)

if __name__ == "__main__":
    solve()
