# Python program to find nth catalan number
 
def findCatalan(n):
  
    # Table to store results of subproblems
    catalan = [0] * (n + 1)

    # Initialize first two values in the table
    catalan[0] = catalan[1] = 1

    # Fill entries in catalan[] using the recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    # Return the last entry
    return catalan[n]


n = 6
res = findCatalan(n)
print(res)