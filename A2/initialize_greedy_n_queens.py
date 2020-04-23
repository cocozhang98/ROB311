import numpy as np
### WARNING: DO NOT CHANGE THE NAME OF THIS FILE, ITS FUNCTION SIGNATURE OR IMPORT STATEMENTS


def initialize_greedy_n_queens(N: int) -> list:
    """
    This function takes an integer N and produces an initial assignment that greedily (in terms of minimizing conflicts)
    assigns the row for each successive column. Note that if placing the i-th column's queen in multiple row positions j
    produces the same minimal number of conflicts, then you must break the tie RANDOMLY! This strongly affects the
    algorithm's performance!

    Example:
    Input N = 4 might produce greedy_init = np.array([0, 3, 1, 2]), which represents the following "chessboard":

     _ _ _ _
    |Q|_|_|_|
    |_|_|Q|_|
    |_|_|_|Q|
    |_|Q|_|_|

    which has one diagonal conflict between its two rightmost columns.

    You many only use numpy, which is imported as np, for this question. Access all functions needed via this name (np)
    as any additional import statements will be removed by the autograder.

    :param N: integer representing the size of the NxN chessboard
    :return: numpy array of shape (N,) containing an initial solution using greedy min-conflicts (this may contain
    conflicts). The i-th entry's value j represents the row  given as 0 <= j < N.
    """
    greedy_init = np.zeros(N,int)
    # First queen goes in a random spot
    greedy_init[0] = np.random.randint(0, N)
    ### YOUR CODE GOES HERE
    conflicts = np.zeros((N,N),int)
    for i in range(1,N):
        if greedy_init[0] + i < N:
            conflicts[greedy_init[0]+i, i] += 1
        if greedy_init[0] - i >= 0:
            conflicts[greedy_init[0] - i, i] += 1
    for m in range(0,N):
        conflicts[greedy_init[0],m] += 1

    for i in range(1,N):
        greedy_init[i] = np.random.choice(np.where(conflicts[:,i] == min(conflicts[:,i]))[0])

        for j in range(1, N-i):
            if greedy_init[i] + j < N:
                conflicts[greedy_init[i] + j, i + j] += 1
            if greedy_init[i] - j >= 0:
                conflicts[greedy_init[i] - j, i + j] += 1
        for m in range(i, N):
            conflicts[greedy_init[i],m] += 1
    return greedy_init


if __name__ == '__main__':
    # You can test your code here
    print(initialize_greedy_n_queens(5))
    pass
