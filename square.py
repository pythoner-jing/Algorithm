#!/usr/bin/env python
#coding:utf-8

#八数码求解

import cantor 
import toolkit 
import copy 
import time
import random

sq = [
1, 2, 3, 
4, 5, 6, 
7, 8, 9
]

#未访问的节点
unvisited = toolkit.Queue()
unvisited_search = toolkit.Queue()
#纪录访问过的节点
exist = [0] * cantor.factorial(9)
exist_search = [0] * cantor.factorial(9)
counter = 1

#测试八数码正确性
def test_square(sq):
	for i in range(9):
		if sq[i] != i + 1:
			return False
	return True

#节点
class Node:
	def __init__(self, parent, sq):
		self.sq = sq
		self.parent = parent
		self.childs = []

	def __str__(self):
		return self.sq

#生成有解集
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

#根据因子返回一个节点
def gen_sq2(sq, factor):
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
		if counter >= factor:
			return current
		map(lambda x : unvisited.enqueue(x), current.childs)
		unvisited.dequeue()

#求解八数码
def search(sq):
	root = Node(None, sq) 
	unvisited_search.enqueue(root)
	exist_search[cantor.cantor(root.sq) - 1] = 1

	while(not unvisited_search.is_empty()):
		current = unvisited_search.head()
		current.childs = [Node(current, x) for x in gen_childs(current.sq) if not exist_search[cantor.cantor(x) - 1]] 
		if test_square(current.sq):
			print_trace(current)
			break
		for x in current.childs: 
			exist_search[cantor.cantor(x.sq) - 1] = 1
		map(lambda x : unvisited_search.enqueue(x), current.childs)
		unvisited_search.dequeue()

#打印求解过程
def print_trace(node):
	if node == None:
		return
	print_trace(node.parent)
	print_sq(node.sq)

#产生子节点
def gen_childs(sq):
	x = sq.index(9)

	row = x / 3
	col = x % 3

	sq = [copy.deepcopy(sq) for i in range(4)]
	p = [0] * 4

	#上次二逼的地方
	#up
	p[0] = row - 1 >= 0 and (row - 1) * 3 + col or -1
	#right
	p[1] = col + 1 <= 2 and row * 3 + col + 1 or -1
	#down
	p[2] = row + 1 <= 2 and (row + 1) * 3 + col or -1
	#left
	p[3] = col - 1 >= 0 and row * 3 + col - 1 or -1

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
		if v == 9:
			print " ",
		else:
			print v,
	print

if __name__ == "__main__":
	#print "开始演算"
	#start = time.time()
	#gen_sq(sq)
	#print "耗时", time.time() - start
	#
	#print "有解集大小", counter
	#print "全集大小", cantor.factorial(9)
	#print "有解集百分比", float(counter) / cantor.factorial(9)

	node = gen_sq2(sq, random.randint(100, 200))
	search(node.sq)
