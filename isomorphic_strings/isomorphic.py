def isomorphic(s, t):
  if len(s) != len(t):
    return False
  d1 = {}
  d2 = {}
  for i in range(len(s)):
    if s[i] not in d1:
      d1[s[i]] = ''
    d1[s[i]] += str(i)+','
    if t[i] not in d2:
      d2[t[i]] = ''
    d2[t[i]] += str(i)+','
  return set(d1.values()) == set(d2.values())  

print(isomorphic('paper', 'title'))
