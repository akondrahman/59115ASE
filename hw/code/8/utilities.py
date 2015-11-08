def median(lst,ordered=False):
  lst = lst if ordered else sorted(lst)
  n   = len(lst)
  p   = n // 2
  if (n % 2):  return lst[p]
  p,q = p-1,p
  q   = max(0,(min(q,n)))
  return (lst[p] + lst[q]) * 0.5


if __name__ == '__main__':
	lst = [1,2,3,4,5]

	median = median(lst)

	print "median=", median