def sigma(term, a, next, b):
   if(a > b):
      return 0
   return term(a) + sigma(term, next(a), next, b)

def term(x):
   return 2 ** x

def next(x)
