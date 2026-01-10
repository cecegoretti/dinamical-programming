def partition(self, s: str) -> List[List[str]]:
    '''
    this funcion return a list containing all 
    possible partition of s into 
    palindromic substring. This is done by presaving which 
    substring of s are palindromic and then by applying
    a dinamical programming process.
    We backtrack all possible palindromic decomposition 
    of every substring of s by constructing them by 
    induction on the lenght of the first piece of the 
    decomposition.
    Space complexity: O(len(s)**2)
    Time complexity is heavily influenced on 
        the partition in palindromic substring
        of the pieces of s
        best scenario: O(len(s)**3)
        worst scenarion: O(len(s)**3*2**len(s))
    '''
    dp=[[[] for _ in range(len(s))] for _ in range(len(s))]
    pal = [[False]*len(s) for _ in range(len(s))]
    for i in range(len(s)):
        pal[i][i] = True
    for l in range(2, len(s)+1):
        for i in range(len(s)-l+1):
            j = i+l-1
            pal[i][j] = s[i]==s[j] and (l==2 or pal[i+1][j-1])

    for j in range(len(s)):
        dp[j][j]=[[s[j]]]
    for j in range(1,len(s)):
        for t in range(len(s)-j):
            if pal[t][t+j]:
                dp[t][t+j].append([s[t:t+j+1]])
            for e in range(j):
                if pal[t][t+e]:
                    z=s[t:t+e+1]
                    for m in dp[t+e+1][t+j]:
                        dp[t][t+j].append([z]+m)
    return dp[0][len(s)-1]
