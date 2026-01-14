def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    ''' 
    this function computes the optimal way to schedule jobs that start at startTime end at endTime
    and give a profit expressed by the array profit. The optimal way is the one that maximizes the
    total profit. To select which are the jobs to schedule we use a dinamical programming approach
    by recursively constructing the optimal way to schedule the jobs that end before a certain hour.
    For the dynamic programming part we use a dictionary to avoid excessive use of memory.
    Space complexity: O(n)    n=len(profit)
    Time complexity: O(n*log n) n=len(profit)
    '''
    values=list(set(startTime+endTime))
    values.sort()
    #values store all possible start and end time
    profit_dp={x:0 for x in values}
    #profit_dp is the dictionary we will use for the DP part of the algorithm
    #profit_dp[x] keep track of the best possible profit using time only until x
    jobs=list(zip(startTime,endTime,profit))
    jobs.sort(key=lambda x: (x[1],x[0]))
    #the jobs are sorted first by ending time and then by starting time
    j=0
    #j keeps track of the position in the total compressed timeline up to which
    #we have propagated the DP. It is needed as it might be that in constructing 
    #the schedule there are gaps in time. It ensures that profit_dp[x] stores the
    #maximum profit using jobs that end before or at most at time x
    for x,y,z in jobs:
        while x>values[j]:
                profit_dp[values[j+1]]=max(profit_dp[values[j+1]],profit_dp[values[j]])
                j+=1
    #in this way we are sure that profit_dp[x] is the maximum of all possible profits 
    #using the first x hours
        
        profit_dp[y]=max(profit_dp[y],profit_dp[x]+z)
    #we decide if scheduling the job x,y,z increase the profit
    return max(profit_dp.values())
    #it might be that the best profit is before the final time as we propagated the 
    #maximum only up to the beginning of the last possible job
