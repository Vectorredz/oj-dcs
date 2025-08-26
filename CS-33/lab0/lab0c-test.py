from collections import deque

def reachable_rooms(grid: list[str], s: tuple[int,int]) -> list[tuple[int,int]]:
    R, C = len(grid), len(grid[0])
    def inbounds(i,j): return 0<=i<R and 0<=j<C
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
    # helper to convert room coord -> grid coord
    def room_to_grid(ri,rj): return 2*ri+1, 2*rj+1

    sr, sc = s
    gi, gj = room_to_grid(sr, sc)
    if not (inbounds(gi,gj) and grid[gi][gj] == ' '):
        return []

    q = deque()
    q.append((sr, sc, ""))            # last_color is "" at start
    seen = {(sr, sc, "")}
    reachable = set()

    while q:
        print(seen)
        ri, rj, last = q.popleft()
        reachable.add((ri, rj))
        gi, gj = room_to_grid(ri, rj)

        for di, dj in dirs:
            sep_i, sep_j = gi + di, gj + dj        # separator cell
            dest_gi, dest_gj = gi + 2*di, gj + 2*dj  # destination room cell
            if not (inbounds(sep_i, sep_j) and inbounds(dest_gi, dest_gj)): 
                continue
            sep = grid[sep_i][sep_j]
            if sep == '#': 
                continue
            if grid[dest_gi][dest_gj] != ' ':
                continue
            nri, nrj = (dest_gi - 1)//2, (dest_gj - 1)//2

            # if the next cell is a room
            if sep == '.' or sep == ' ':
                st = (nri,nrj,last)
                if st not in seen:
                    seen.add(st); 
                    q.append(st)
            # if not a room
            elif sep in ('R','B'):
                # can move if last is empty (first door) or different from sep
                if last == "" or last != sep:
                    st = (nri,nrj, sep)
                    if st not in seen:
                        seen.add(st); q.append(st)
    print(sorted(reachable))
    return sorted(reachable)



reachable_rooms([
        "#######",
        "# B B #",
        "###R###",
        "# R R #",
        "###R###",
        "# R R #",
        "#######",
    ], (1, 1))


