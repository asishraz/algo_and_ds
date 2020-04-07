'''
gcd(m,n)
list out factors of m
list out factors of n
then find the largest number appears on  both the lists
factors of m lie in the range of 1 and m, not greater than m
test each number in this range
if the number divides m without a remainder, then add to the list of factors


e.g ; gcd(14,63)
14 = range(1,14) => 1,2,7,14 are the factors  => f(m)
63 = range(1,63) => 1,3,7,9,21,63 are the factors => f(n)

now generate list of common factors:
 by taking any of the list, say 14
 and check whether the numbers  appears to the other list or not
 factors of 14 (1,2,7,14) and only (1,7) appears on other list
 (1,7) is the final list or the common factors => cf


now return the highest number/factor in the final list or the rightmost value

'''

m = int(input()) #14
n = int(input()) #63


def gcd(m,n):
	fm = []
	
	
	for i in range(1,m+1):
		if m%i == 0:
			fm.append(i)

	print(fm)

	fn = []
	for j in range(1,n+1):
		if n%j == 0:
			fn.append(j)
	print(fn)

	cf = []
	for i in fm:
		if i in fn:
			cf.append(i)

	print(cf)
	print(cf[-1])

gcd(m,n)








