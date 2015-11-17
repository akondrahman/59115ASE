import random
rand = random.random
any  = random.choice
seed = random.seed
exp  = lambda n: math.e**n
ln   = lambda n: math.log(n,math.e)
g    = lambda n: round(n,2)

# def median(lst,ordered=False):
#   lst = lst if ordered else sorted(lst)
#   n   = len(lst)
#   p   = n // 2
#   if (n % 2):  return lst[p]
#   p,q = p-1,p
#   q   = max(0,(min(q,n)))
#   return (lst[p] + lst[q]) * 0.5

# def gt(x,y): return x > y
# def lt(x,y): return x < y

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
      h1 = t1.l[t1.m] #mth element of list 1
      h2 = t2.l[t2.m] #mth element of list 2
      h3 = t2.l[t2.m+1] if t2.m+1 < t2.n else None # next element if it is not end of list else None
      # print "h1:", h1, ""
      if h1 > h2:
        t1.m  += 1; t1.gt += t2.n - t2.m  
      elif h1 == h2:
        # if h3 and gt(h1,h3) < 0:
        if h3 and h1 > h3:
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
  # print t1 
  gt,eq= loop(t1, t1, t2)
  a12_value=gt/(n1*n2) + eq/2/(n1*n2)
  return a12_value

#For bootstrap below

def sampleWithReplacement(lst):
  "returns a list same size as list"
  def any(n)  : return random.uniform(0,n)
  def one(lst): return lst[ int(any(len(lst))) ]
  return [one(lst) for _ in lst]


def testStatistic(y,z): 
    """Checks if two means are different, tempered
     by the sample size of 'y' and 'z'"""
    tmp1 = tmp2 = 0
    for y1 in y.all: tmp1 += (y1 - y.mu)**2 
    for z1 in z.all: tmp2 += (z1 - z.mu)**2
    s1    = (float(tmp1)/(y.n - 1))**0.5
    s2    = (float(tmp2)/(z.n - 1))**0.5
    delta = z.mu - y.mu
    if s1+s2:
      delta =  delta/((s1/y.n + s2/z.n)**0.5)
    return delta


def bootstrap(y0,z0,conf=0.01,b=1000):
  """The bootstrap hypothesis test from
     p220 to 223 of Efron's book 'An
    introduction to the boostrap."""
  class total():
    "quick and dirty data collector"
    def __init__(i,some=[]):
      i.sum = i.n = i.mu = 0 ; i.all=[]
      for one in some: i.put(one)
    def put(i,x):
      i.all.append(x);
      i.sum +=x; i.n += 1; i.mu = float(i.sum)/i.n
    def __add__(i1,i2): return total(i1.all + i2.all)
  y, z   = total(y0), total(z0)
  x      = y + z
  tobs   = testStatistic(y,z)
  yhat   = [y1 - y.mu + x.mu for y1 in y.all]
  zhat   = [z1 - z.mu + x.mu for z1 in z.all]
  bigger = 0.0
  for i in range(b):
    if testStatistic(total(sampleWithReplacement(yhat)),
                     total(sampleWithReplacement(zhat))) > tobs:
      bigger += 1
  return bigger / b < conf


def _bootstraped(): 
  def worker(n=1000,
             mu1=10,  sigma1=1,
             mu2=10.2, sigma2=1):
    def g(mu,sigma) : return random.gauss(mu,sigma)
    x = [g(mu1,sigma1) for i in range(n)]
    y = [g(mu2,sigma2) for i in range(n)]
    return n,mu1,sigma1,mu2,sigma2,\
        'different' if bootstrap(x,y) else 'same'
  # very different means, same std
  print worker(mu1=10, sigma1=10, 
               mu2=100, sigma2=10)
  # similar means and std
  print worker(mu1= 10.1, sigma1=1, 
               mu2= 10.2, sigma2=1)
  # slightly different means, same std
  print worker(mu1= 10.1, sigma1= 1, 
               mu2= 10.8, sigma2= 1)
  # different in mu eater by large std
  print worker(mu1= 10.1, sigma1= 10, 
               mu2= 10.8, sigma2= 1)


def different(l1,l2):
  #return bootstrap(l1,l2) and a12(l2,l1)
  return a12(l2,l1) and bootstrap(l1,l2)


#Now code below for clustering

def scottknott(data,cohen=0.3,small=3, useA12=False,epsilon=0.01):
  """Recursively split data, maximizing delta of
  the expected value of the mean before and 
  after the splits. 
  Reject splits with under 3 items"""
  all  = reduce(lambda x,y:x+y,data)
  same = lambda l,r: abs(l.median() - r.median()) <= all.s()*cohen
  if useA12: 
    same = lambda l, r:   not different(l.all,r.all) 
  big  = lambda    n: n > small    
  return rdiv(data,all,minMu,big,same,epsilon)

def rdiv(data,  # a list of class Nums
         all,   # all the data combined into one num
         div,   # function: find the best split
         big,   # function: rejects small splits
         same, # function: rejects similar splits
         epsilon): # small enough to split two parts
  """Looks for ways to split sorted data, 
  Recurses into each split. Assigns a 'rank' number
  to all the leaf splits found in this way. 
  """
  def recurse(parts,all,rank=0):
    "Split, then recurse on each part."
    cut,left,right = maybeIgnore(div(parts,all,big,epsilon),
                                 same,parts)
    if cut: 
      # if cut, rank "right" higher than "left"
      rank = recurse(parts[:cut],left,rank) + 1
      rank = recurse(parts[cut:],right,rank)
    else: 
      # if no cut, then all get same rank
      for part in parts: 
        part.rank = rank
    return rank
  recurse(sorted(data),all)
  return data

def maybeIgnore((cut,left,right), same,parts):
  if cut:
    if same(sum(parts[:cut],Num('upto')),
            sum(parts[cut:],Num('above'))):    
      cut = left = right = None
  return cut,left,right

def minMu(parts,all,big,epsilon):
  """Find a cut in the parts that maximizes
  the expected value of the difference in
  the mean before and after the cut.
  Reject splits that are insignificantly
  different or that generate very small subsets.
  """
  cut,left,right = None,None,None
  before, mu     =  0, all.mu
  for i,l,r in leftRight(parts,epsilon):
    if big(l.n) and big(r.n):
      n   = all.n * 1.0
      now = l.n/n*(mu- l.mu)**2 + r.n/n*(mu- r.mu)**2  
      if now > before:
        before,cut,left,right = now,i,l,r
  return cut,left,right

def leftRight(parts,epsilon=0.01):
  """Iterator. For all items in 'parts',
  return everything to the left and everything
  from here to the end. For reasons of
  efficiency, take a first pass over the data
  to pre-compute and cache right-hand-sides
  """
  rights = {}
  n = j = len(parts) - 1
  while j > 0:
    rights[j] = parts[j]
    if j < n: rights[j] += rights[j+1]
    j -=1
  left = parts[0]
  for i,one in enumerate(parts):
    if i> 0: 
      if parts[i]._median - parts[i-1]._median > epsilon:
        yield i,left,rights[i]
      left += one

def rdivDemo(data):
  def z(x):
    return int(100 * (x - lo) / (hi - lo + 0.00001))
  data = map(lambda lst:Num(lst[0],lst[1:]),
             data)
  print ""
  ranks=[]
  for x in scottknott(data,useA12=True):
    ranks += [(x.rank,x.median(),x)]
  all=[]
  for _,__,x in sorted(ranks): all += x.all
  all = sorted(all)
  lo, hi = all[0], all[-1]
  line = "----------------------------------------------------"
  last = None
  print  ('%4s , %12s ,    %s   , %4s ' % \
               ('rank', 'name', 'med', 'iqr'))+ "\n"+ line
  for _,__,x in sorted(ranks):
    q1,q2,q3 = x.quartiles()
    print  ('%4s , %12s ,    %4s  ,  %4s ' % \
                 (x.rank+1, x.name, q2, q3 - q1))  + \
              xtile(x.all,lo=lo,hi=hi,width=30,show="%5.2f")
    last = x.rank 

def rdiv0():
  rdivDemo([
        ["x1",0.34, 0.49, 0.51, 0.6],
        ["x2",6,  7,  8,  9] ])

def rdiv1():
  rdivDemo([
        ["x1",0.1,  0.2,  0.3,  0.4],
        ["x2",0.1,  0.2,  0.3,  0.4],
        ["x3",6,  7,  8,  9] ])

# def rdiv2():
#   rdivDemo([
#         ["x1",0.34, 0.49, 0.51, 0.6],
#         ["x2",0.6,  0.7,  0.8,  0.9],
#         ["x3",0.15, 0.25, 0.4,  0.35],
#         ["x4",0.6,  0.7,  0.8,  0.9],
#         ["x5",0.1,  0.2,  0.3,  0.4] ])


def rdiv2():
  rdivDemo([
      ["x1",101, 100, 99,   101],
      ["x2",101, 100, 99,   101],
      ["x3",0.15, 0.22, 0.4, 0.3],
      ["x4",0.6, 0.7, 0.8,   0.9],
      ["x5", 0.1,0.2,0.3,0.4] ])

def rdiv3():
  rdivDemo([
      ["x1",101, 100, 99,   101,  99.5],
      ["x2",101, 100, 99,   101, 100],
      ["x3",101, 100, 99.5, 101,  99],
      ["x4",101, 100, 99,   101, 100] ])

def rdiv5():
  rdivDemo([
      ["x1",11,11,11],
      ["x2",11,11,11],
      ["x3",11,11,11]])

def rdiv6():
  rdivDemo([
      ["x1",11,11,11],
      ["x2",11,11,11],
      ["x4",32,33,34,35]])

def rdiv7():
  rdivDemo([
    ["x1"] +  [rand()**0.5 for _ in range(256)],
    ["x2"] +  [rand()**2   for _ in range(256)],
    ["x3"] +  [rand()      for _ in range(256)]
  ])



## Some more miscellaneous functions

def median(lst,ordered=False):
  if not ordered: lst= sorted(lst)
  n = len(lst)
  p = n//2
  if n % 2: return lst[p]
  q = p - 1
  q = max(0,min(q,n))
  return (lst[p] + lst[q])/2

def msecs(f):
  import time
  t1 = time.time()
  f()
  return (time.time() - t1) * 1000

def pairs(lst):
  "Return all pairs of items i,i+1 from a list."
  last=lst[0]
  for i in lst[1:]:
    yield last,i
    last = i

def xtile(lst,lo=0,hi=100,width=50,
             chops=[0.1 ,0.3,0.5,0.7,0.9],
             marks=["-" ," "," ","-"," "],
             bar="|",star="*",show=" %3.0f"):
  """The function _xtile_ takes a list of (possibly)
  unsorted numbers and presents them as a horizontal
  xtile chart (in ascii format). The default is a 
  contracted _quintile_ that shows the 
  10,30,50,70,90 breaks in the data (but this can be 
  changed- see the optional flags of the function).
  """
  def pos(p)   : return ordered[int(len(lst)*p)]
  def place(x) : 
    return int(width*float((x - lo))/(hi - lo+0.00001))
  def pretty(lst) : 
    return ', '.join([show % x for x in lst])
  ordered = sorted(lst)
  lo      = min(lo,ordered[0])
  hi      = max(hi,ordered[-1])
  what    = [pos(p)   for p in chops]
  where   = [place(n) for n in  what]
  out     = [" "] * width
  for one,two in pairs(where):
    for i in range(one,two): 
      out[i] = marks[0]
    marks = marks[1:]
  out[int(width/2)]    = bar
  out[place(pos(0.5))] = star 
  return '('+''.join(out) +  ")," +  pretty(what)

def _tileX() :
  import random
  random.seed(1)
  nums = [random.random()**2 for _ in range(100)]
  print xtile(nums,lo=0,hi=1.0,width=25,show=" %5.2f")

class Num:
  "An Accumulator for numbers"
  def __init__(i,name,inits=[]): 
    i.n = i.m2 = i.mu = 0.0
    i.all=[]
    i._median=None
    i.name = name
    i.rank = 0
    for x in inits: i.add(x)
  def s(i)       : return (i.m2/(i.n - 1))**0.5
  def add(i,x):
    i._median=None
    i.n   += 1   
    i.all += [x]
    delta  = x - i.mu
    i.mu  += delta*1.0/i.n
    i.m2  += delta*(x - i.mu)
  def __add__(i,j):
    return Num(i.name + j.name,i.all + j.all)
  def quartiles(i):
    def p(x) : return int(100*g(xs[x]))
    i.median()
    xs = i.all
    n  = int(len(xs)*0.25)
    return p(n) , p(2*n) , p(3*n)
  def median(i):
    if not i._median:
      i.all = sorted(i.all)
      i._median=median(i.all)
    return i._median
  def __lt__(i,j):
    return i.median() < j.median() 
  def spread(i):
    i.all=sorted(i.all)
    n1=i.n*0.25
    n2=i.n*0.75
    if len(i.all) <= 1:
      return 0
    if len(i.all) == 2:
      return i.all[1] - i.all[0]
    else:
      return i.all[int(n2)] - i.all[int(n1)]
      

#def doLoss():
#      
#def computeLoss(era0List, eraNList): 
#  for it_ in era0List:
#    for ite_ in eraNList:
#      doLoss(ite_, it_) 
      

def _rdivs():
  seed(1)
  rdiv0() 
  print "+++++++++++++++++++++++++"
  rdiv1()
  print "+++++++++++++++++++++++++"
  rdiv2()
  print "+++++++++++++++++++++++++"
  rdiv3() 
  print "+++++++++++++++++++++++++"
  rdiv5()
  print "+++++++++++++++++++++++++"
  rdiv6()
  print "+++++++++++++++++++++++++"
  rdiv7()
  print "+++++++++++++++++++++++++"

if __name__ == '__main__':
	lst = [1,2,3,4,5]
	# median = median(lst)
	# print "median=", median

	# print "--------------"

	lst1=[1,2,3,4,5]
	lst2=[100,100,0,100,100]
	a12_output = a12(lst1,lst2)
	print "a12_output:=", a12_output
	print "---------"

	_bootstraped()
	_rdivs()