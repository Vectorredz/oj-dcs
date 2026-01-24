def max_matching(a):  # Kuhn's
    n = len(a)
    m = len(a[0])
    assert all(len(row) == m for row in a)

    adj = [[j for j in range(m) if a[i][j]] for i in range(n)]

    # nodes are marked 0 to n-1 on the left
    # nodes are marked 0 to m-1 on the right
    # for a node i on the left,  r[i] is its matching node on the right
    # for a node j on the right, l[j] is its matching node on the left
    # -1 if a node is unmatched
    r = [-1]*n
    l = [-1]*m

    def try_matching(i):
        assert not vis[i]
        vis[i] = True
        for j in adj[i]:
            if l[j] == -1 or not vis[l[j]] and try_matching(l[j]):
                r[i] = j
                l[j] = i
                return True

        return False

    max_matching = 0
    for s in range(n):
        # try augmenting from s
        vis = [False]*n  # unvisit all nodes before every iteration
        max_matching += try_matching(s)

    assert max_matching == sum(j != -1 for j in r)
    assert max_matching == sum(i != -1 for i in l)
    for idx, i in enumerate(l):
        if l[i] != -1:
            print(idx, i)
    return max_matching


if __name__ == '__main__':
    print(max_matching((
        (1, 1),
        (1,0),
        (1,0)
    )))

    # print(max_matching((
    #     (1, 1, 1),
    #     (0, 0, 1),
    #     (0, 0, 1),
    # )))