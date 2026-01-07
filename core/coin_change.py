from collections import deque

def coin_change(coin_values, amount):
  ''' this function computes the minimum number of coins 
      needed to obtain the requested amount. We assume that we
      can use as many coins of each type as we wish.
      The idea is to use a queue to
      simulate an analogous of a BFS tree search on 
      the amounts that can be obtained from the set 
      of coins.
      Space complexity: O(amount)
      Time complexity: O(amount*len(coin_values)).
      Note: if gcd of coin_values is >1, than BFS approach
      is optimal compared to classical DP. If gcd=1 and
      amount big enough, the two approach are computationally
      equivalent.
      '''
    if amount<0:
        return -1
    if amount==0:
        return 0
    dp=[0]*(amount+1)
    #dp[i]==0 means either i=0 (reachable with 0 coins) or
    #i is not visited yet
    new_found=deque([0])
    while new_found:
        last_found=new_found.popleft()
        for i in coin_values:
            if last_found+i<=amount:
                if dp[last_found+i]==0:
                  #last_found+i>0 hence we are checking 
                  #if last_found+i was visited
                  dp[last_found+i]=dp[last_found]+1
                  new_found.append(last_found+i)
    if dp[amount]==0:
        return -1
    else:
        return dp[amount]
