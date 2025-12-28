exercise: https://leetcode.com/problems/word-break/description/

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
  '''
  This function determines wether the string s
  can be segmented into space separated sequence
  of one or more words in wordDict. 
  The same word in wordDict can be used multiple
  times.
  '''
  last=[]
  dp=[0]*(len(s)) #dp[i]=1 if the string s[i:] can be constructed using words from wordDict
  for j in wordDict:
    if s.endswith(j):
      dp[-len(j)]=1
      last.append(-len(j))
  while last!=[]:
    t=last.pop()
    for k in wordDict:
      if len(k)-t<=len(s) and s.endswith(k,0,t) and dp[t-len(k)]==0:
        if t-len(k)==0:
          return True
        dp[t-len(k)]=1
        last.append(t-len(k))
  return bool(dp[0])
