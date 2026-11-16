def dynamic_programming_tabulation(A, X):
    """
    Calculates the optimal value using bottom-up tabulation based on recurrent relation phi.
    Time Complexity: O(N * X)
    Space Complexity: O(N * X)
    """
    N = len(A)
    
    tab = [[0] * (X + 1) for _ in range(N + 1)]
    
    for x in range(X + 1):
        tab[0][x] = 0
        
    for n in range(1, N + 1):
        for x in range(X + 1):
            if A[n - 1] > x:
                tab[n][x] = tab[n - 1][x]
            else:
                without_element = tab[n - 1][x]
                with_element = tab[n - 1][x - A[n - 1]] + A[n - 1]
                tab[n][x] = max(without_element, with_element)
                
    return tab[N][X]