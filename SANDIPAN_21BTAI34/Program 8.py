def mean(l):
  return sum(l)/len(l)
def median(l):
  l.sort()
  length=len(l)
  if le%2==0:
    return l[length//2-1],l[length//2]
  return l[length//2]
def mode(l):
  count=0
  el=None
  for i in l:
    if l.count(i)>count:
      el=i
      count=l.count(i)
  return el
def range(l):
  return max(l)-min(l)
lst=[10,20,30,40,50,60,70,80,90,100]
print(mean(lst))
print(median(lst))
print(mode(lst))
print(range(lst))
