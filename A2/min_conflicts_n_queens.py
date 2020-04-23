import numpy as np
### WARNING: DO NOT CHANGE THE NAME OF THIS FILE, ITS FUNCTION SIGNATURE OR IMPORT STATEMENTS


def min_conflicts_n_queens(initialization: list) -> (list, int):
    """
    Solve the N-queens problem with no conflicts (i.e. each row, column, and diagonal contains at most 1 queen).
    Given an initialization for the N-queens problem, which may contain conflicts, this function uses the min-conflicts
    heuristic(see AIMA, pg. 221) to produce a conflict-free solution.

    Be sure to break 'ties' (in terms of minimial conflicts produced by a placement in a row) randomly.
    You should have a hard limit of 1000 steps, as your algorithm should be able to find a solution in far fewer (this
    is assuming you implemented initialize_greedy_n_queens.py correctly).

    Return the solution and the number of steps taken as a tuple. You will only be graded on the solution, but the
    number of steps is useful for your debugging and learning. If this algorithm and your initialization algorithm are
    implemented correctly, you should only take an average of 50 steps for values of N up to 1e6.

    As usual, do not change the import statements at the top of the file. You may import your initialize_greedy_n_queens
    function for testing on your machine, but it will be removed on the autograder (our test script will import both of
    your functions).

    On failure to find a solution after 1000 steps, return the tuple ([], -1).

    :param initialization: numpy array of shape (N,) where the i-th entry is the row of the queen in the ith column (may
                           contain conflicts)

    :return: solution - numpy array of shape (N,) containing a-conflict free assignment of queens (i-th entry represents
    the row of the i-th column, indexed from 0 to N-1)
             num_steps - number of steps (i.e. reassignment of 1 queen's position) required to find the solution.
    """

    N = len(initialization)
    solution = initialization.copy()
    num_steps = 0
    max_steps = 1000
    for idx in range(max_steps):
        ## YOUR CODE HERE
        conflicts = set([])
        for i in range(0,N):
            indices = np.where(solution == i)[0]
            if len(indices) > 1:
                for index in indices:
                    conflicts.add(index)
        rows = np.zeros(N)
        right = np.zeros(2 * N - 1)
        left = np.zeros(2 * N - 1)
        for i in range(N):
            rows[int(solution[i])] += 1
            right[int(solution[i]) + i] += 1
            left[int(N - 1 + solution[i] - i)] += 1


        for index in np.where(right > 1)[0]:
            for i in range(N):
                if solution[i] + i == index:
                    conflicts.add(i)
        for index in np.where(left > 1)[0]:
            for i in range(N):
                if N - 1 + solution[i] - i == index:
                    conflicts.add(i)
        conflicts = list(conflicts)
        if conflicts == []:
            return solution,num_steps
        var = np.random.choice(conflicts)
        solution[var] = -1

        num_conflicts = np.zeros(N,int)
        for j in range(N):
            num_conflicts[j] = rows[j] + right[j + var] + left[N - 1 + j - var]

        solution[var] = np.random.choice(np.where(num_conflicts == min(num_conflicts))[0])
    return solution, num_steps


if __name__ == '__main__':
    # Test your code here!
    from initialize_greedy_n_queens import initialize_greedy_n_queens
    from support import plot_n_queens_solution

    N = 10
    # Use this after implementing initialize_greedy_n_queens.py
    assignment_initial = initialize_greedy_n_queens(N)
    # Plot the initial greedy assignment
    plot_n_queens_solution(assignment_initial)

    assignment_solved, n_steps = min_conflicts_n_queens(assignment_initial)
    # Plot the solution produced by your algorithm
    plot_n_queens_solution(assignment_solved)
