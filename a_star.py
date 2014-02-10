#!/usr/bin/env python
#coding:utf-8

#author:jing

#演示传说中的A星算法


import toolkit as tk
import copy

#迷宫地图
#0 - 通途
#1 - 障碍
#目的是用最小开销找出从(4, 2)到(1, 2)的最小路径
maze = [
[1, 1, 1, 1, 1, 1, 1, 1],		
[1, 0, 0, 0, 0, 0, 0, 1],		
[1, 1, 1, 1, 1, 0, 0, 1],		
[1, 0, 0, 0, 1, 0, 0, 1],		
[1, 0, 0, 0, 1, 0, 0, 1],		
[1, 0, 1, 0, 1, 0, 0, 1],		
[1, 0, 0, 0, 0, 0, 0, 1],		
[1, 1, 1, 1, 1, 1, 1, 1]	
]

#(2, 3) -> (6, 4)
maze2 = [
[1, 1, 1, 1, 1, 1, 1, 1],		
[1, 0, 0, 0, 0, 0, 0, 1],		
[1, 0, 0, 0, 1, 0, 0, 1],		
[1, 0, 0, 0, 1, 0, 0, 1],		
[1, 0, 0, 0, 1, 0, 0, 1],		
[1, 0, 1, 0, 1, 0, 0, 1],		
[1, 0, 0, 0, 0, 0, 0, 1],		
[1, 1, 1, 1, 1, 1, 1, 1]	
]


#纪录打开过的路径
path_on_maze = [[None] * 8 for i in range(8)]

#方向偏移
#up, right, down, left
offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#纪录路径状态
st_blank = 0
st_opened = 1 
st_closed = 2


#路径节点
class Path:
	def __init__(self, parent, pos):
		self.parent = parent
		self.pos = pos
		#到达该方块最少的移动量
		self.g = 0
		#该方块到达目的地预估剩余的移动量
		self.h = 0
		#路径的整体开销 f = g + h
		self.f = 0
		self.status = st_blank 

	def __str__(self):
		return str(self.pos[0]) + " " + str(self.pos[1]) + " " + str(self.f)

#纪录已打开但未被使用的路径坐标
class Opened(tk.Stack):
	#弹出一个最小开销的路径
	def pop(self):
		if self.stack != []:
			min_index = len(self.stack) - 1
			for i, v in enumerate(self.stack[::-1]):
				if v.f < self.stack[min_index].f:
					min_index = len(self.stack) - i - 1 
			return self.stack.pop(min_index)
		else:
			return None

	def push(self, path):
		self.stack.append(path)

	def set_path(self, path):
		for i, v in enumerate(self.stack):
			if v.pos[0] == path.pos[0] and v.pos[1] == path.pos[1]:
				self.stack[i] = path

#打开附近路径
def open_path(maze, path_parent, pos_target):
	for k in offset:
		#不是障碍
		if (not maze[path_parent.pos[0] + k[0]][path_parent.pos[1] + k[1]]):
			path = Path(path_parent, (path_parent.pos[0] + k[0], path_parent.pos[1] + k[1]))
			path.g = path_parent.g + 1
			path.h = distance(path.pos, pos_target) 
			path.f = path.g + path.h
			path.status = st_opened
			#不是障碍且被打开过
			try:
				if path_on_maze[path_parent.pos[0] + k[0]][path_parent.pos[1] + k[1]]:
					#如果现在的代价小于原先的代价且不在关闭状态，取代该路径
					if path.f < path_on_maze[path.pos[0]][path.pos[1]].f and path_on_maze[path_parent.pos[0] + k[0]][path_parent.pos[1] + k[1]].status == st_opened:
						path_on_maze[path.pos[0]][path.pos[1]] = path
						opened.set_path(path)
				#不是障碍且没有被打开过
				else:
					path_on_maze[path.pos[0]][path.pos[1]] = path
					opened.push(path)
			except Exception, e:
				print path_parent.pos[0] + k[0], path_parent.pos[1] + k[1]

#代价估算函数
def distance(pos_current, pos_target):
	return abs(pos_current[0] - pos_target[0]) + abs(pos_current[1] - pos_target[1])

def print_trace(path):
	if path == None:
		return
	else:
		print_trace(path.parent)
		print str(path.pos)

#生成捷径
def gen_shortcut(maze, pos_start, pos_target):
	s = Path(None, pos_start)
	s.status = st_closed
	path_on_maze[pos_start[0]][pos_start[1]] = s
	open_path(maze, s, pos_target)

	while(not opened.is_empty()):
		current = opened.pop()
		current.status = st_closed
		if current.pos[0] == pos_target[0] and current.pos[1] == pos_target[1]:
			print_trace(current)
			return
		open_path(maze, current, pos_target)

opened = Opened()

gen_shortcut(maze2, (2, 3), (5, 5))
