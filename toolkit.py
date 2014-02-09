#!/user/bin/env python
#coding:utf-8

class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if self.stack != []:
			return self.stack.pop(-1)
		else:
			return None
	def top(self):
		if self.stack != []:
			return self.stack[-1]
		else:
			return None

	def length(self):
		return len(self.stack)

	def is_empty(self):
		return self.stack == []

	def __str__(self):
		return str(self.stack)

class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self, index = 0):
		if self.queue != []:
			return self.queue.pop(index)
		else:
			return None

	def head(self):
		if self.queue != []:
			return self.queue[0]
		else:
			return None

	def tail(self):
		if self.queue != []:
			return self.queue[-1]
		else:
			return None

	def length(self):
		return len(self.queue)
	
	def is_empty(self):
		return self.queue == []

	def __str__(self):
		return str(self.queue)

	def index(self, item):
		return self.queue.index(item)
