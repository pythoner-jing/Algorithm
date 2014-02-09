#!/usr/bin/env python
#coding:utf-8

#八数码生成演算

import cantor 
import toolkit 
import copy 
import time

sq = [
1, 2, 3, 
4, 5, 6, 
7, 8, 9
]

unvisited = toolkit.Queue()
exist = [0] * cantor.factorial(9)
counter = 1

def test_square(sq):
	p = 1 
	for x in range(3):
		for y in range(3):
			if sq[x][y] != p:
				return False
			p += 1
	return True

class Node:
	def __init__(self, parent, sq):
		self.sq = sq
		self.parent = parent
		self.childs = []

	def __str__(self):
		return self.sq

def gen_sq(sq):
	global counter
	root = Node(None, sq)
	unvisited.enqueue(root)
	exist[cantor.cantor(root.sq) - 1] = 1

	while(not unvisited.is_empty()):
		current = unvisited.head()
		current.childs = [Node(current, x) for x in gen_childs(current.sq) if not exist[cantor.cantor(x) - 1]] 
		for x in current.childs: 
			exist[cantor.cantor(x.sq) - 1] = 1
			counter += 1
		map(lambda x : unvisited.enqueue(x), current.childs)
		unvisited.dequeue()

def gen_childs(sq):
	x = sq.index(9)

	row = x / 3
	col = x % 3

	sq = [copy.deepcopy(sq) for i in range(4)]
	p = [0] * 4

	#up
	p[0] = (row - 1) * 3 + col
	#right
	p[1] = row * 3 + col + 1
	#down
	p[2] = (row + 1) * 3 + col
	#left
	p[3] = row * 3 + col - 1

	for i in range(4):
		if p[i] < 0 or p[i] > 8:
			p[i] = -1 

	childs = []

	for i in range(4):
		if p[i] >= 0:
			sq[i][x], sq[i][p[i]] = sq[i][p[i]], sq[i][x]
			childs.append(sq[i])

	return childs

def print_sq(sq):
	for i, v in enumerate(sq):
		if i % 3 == 0:
			print
		print v,
	print

print "开始演算"
start = time.time()
gen_sq(sq)
print "耗时", time.time() - start

print "有解集大小", counter
print "全集大小", cantor.factorial(9)
print "有解集百分比", float(counter) / cantor.factorial(9)
