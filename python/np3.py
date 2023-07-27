def r(m):
  seen = set()
  for i in range(len(m)-1,-1,-1):
    if m[i] in seen:
      m.remove(m[i])
    else:
      seen.add(m[i])
  return(m)
print(r([8,6,4,6,8]))
