def guess_friends(n, f):
    # Check if the total number of friends is even
    total_friends = sum(f)
    if total_friends % 2 != 0:
        # If the total number of friends is odd, it's impossible
        return {'count': -1, 'pairs': []}

    # Create a list of people with their friend count and sort it by friend count in descending order
    people = [(i, f[i]) for i in range(n)]
    people.sort(key=lambda x: x[1], reverse=True)

    # To store the result pairs
    pairs = []

    # Create a list to track remaining friend counts
    friends_left = [f[i] for i in range(n)]

    for i in range(n):
        if friends_left[people[i][0]] == 0:
            continue
        
        person1 = people[i][0]
        for j in range(i + 1, n):
            if friends_left[people[j][0]] == 0:
                continue

            person2 = people[j][0]
            if friends_left[person1] > 0 and friends_left[person2] > 0:
                # Create a pair
                pairs.append((person1, person2))
                friends_left[person1] -= 1
                friends_left[person2] -= 1

    # After all the pairing, if any person still has unfulfilled friend counts, return impossible
    if any(friends_left[i] > 0 for i in range(n)):
        return {'count': -1, 'pairs': []}

    return {'count': len(pairs), 'pairs': pairs}

print(guess_friends(6, (2,2,0,2,1,3)))