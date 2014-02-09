#/usr/bin/evn python
#coding:utf-8

#康托展开演示

fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
m = len(fac)

def factorial(x):
	if x == 0 or x == 1:
		return 1
	else:
		return x * factorial(x - 1)

def cantor(lst):
	tmp = None
	n = len(lst)
	num = 0
	for i in range(n):
		tmp = 0
		for j in range(i + 1, n):
			if lst[j] < lst[i]:
				tmp += 1
		if(n - i - 1 < m):
			num += fac[n - i - 1] * tmp
		else:
			num += factorial(n - i - 1) * tmp
	return num + 1
