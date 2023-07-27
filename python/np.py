def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist.append(i)
  return(factorlist)

def prime(n):
  return(factors(n)==[1,n])

def primepartition(n):
  for i in range(1,n//2+1):
    if prime(i) and prime(n-i):
      return(True)
  return(False)
print(primepartition(499525))
