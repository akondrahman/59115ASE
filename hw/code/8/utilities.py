def median(lst,ordered=False):
  lst = lst if ordered else sorted(lst)
  n   = len(lst)
  p   = n // 2
  if (n % 2):  return lst[p]
  p,q = p-1,p
  q   = max(0,(min(q,n)))
  return (lst[p] + lst[q]) * 0.5


class o():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,pretty(d[k])) 
                     for k in i.show()])+ '}'
  def show(i):
    return [k for k in sorted(i.__dict__.keys()) 
            if not "_" in k]

#Note: This is a12 FAST
def a12(lst1,lst2):
  """how often is lst1 often more than y in lst2?
  assumes lst1 nums are meant to be greater than lst2"""

  def loop(t,t1,t2): 
    while t1.m < t1.n and t2.m < t2.n:
      h1 = t1.l[t1.m]
      h2 = t2.l[t2.m]
      h3 = t2.l[t2.m+1] if t2.m+1 < t2.n else None 
      if h1 > h2:
        t1.m  += 1; t1.gt += t2.n - t2.m
      elif h1 == h2:
        if h3 and gt(h1,h3) < 0:
            t1.gt += t2.n - t2.m  - 1
        t1.m  += 1; t1.eq += 1; t2.eq += 1
      else:
        t2,t1  = t1,t2
    return t.gt*1.0, t.eq*1.0
  #--------------------------
  lst1 = sorted(lst1,reverse=True)
  lst2 = sorted(lst2,reverse=True)
  n1   = len(lst1)
  n2   = len(lst2)
  t1   = o(l=lst1,m=0,eq=0,gt=0,n=n1)
  t2   = o(l=lst2,m=0,eq=0,gt=0,n=n2)
  gt,eq= loop(t1, t1, t2)
  a12_value=gt/(n1*n2) + eq/2/(n1*n2)
  return a12_value



if __name__ == '__main__':
	lst = [1,2,3,4,5]
	median = median(lst)
	print "median=", median

	print "--------------"

	lst1=[1,2,3,4,5]
	lst2=[100,100,0,100,100]
	a12_output = a12(lst1,lst2)
	print "a12_output:=", a12_output

