class Heapify(object):
	def __init__(self, items: int) -> None:
		self.heap = []
		self.rank = {}	# why though?
		for i in items:
			self.push(i)
	
	#
	def __len__(self) -> int:
		return len(self.heap) - 1 # keep the first element empty 
	
	#
	def push(self, item: int) -> None:
		if item in self.rank: 
			return None
		last_item_index = len(self.heap)
		self.heap.append(item)
		self.rank[item] = last_item_index
		self.move_up(last_item_index)
	
	#
	def pop(self) -> int:
		root = self.heap[1]
		del self.rank[root]
		#
		x = self.heap.pop()
		if self:
			self.heap[1] = x
			self.rank[x] = 1
			self.move_down(1)
		return root
	
	#
	def move_up(self, item_index: int) -> None:
		x = self.heap[item_index]
		while i > 1 and x < self.heap[i//2]:
			self.heap[i] = self.heap[i//2]
			self.rank[self.heap[i//2]] = i
			i //= 2
		self.heap[i] = x
		self.rank[x] = i

	#
	def move_down(self, item_index: int) -> None:
		x = self.heap[item_index]
		n = len(self.heap)
		#
		while True:
			left = 2 * item_index
			right = left + 1
			if (right < n and self.heap[right] < x) and (self.heap[right] < self.heap[left]):
				self.heap[i] = self.heap[right]
				self.rank[self.heap[right]] = item_index
				item_index = right
			elif left < n and self.heap[left] < x:
				self.heap[item_index] = self.heap[left]
				self.rank[self.heap[left]] = item_index
				item_index = left
			else:
				self.heap[item_index] = self.heap[x]
				self.rank[x] = item_index
				return

	#
	def update(self, old: int, new: int) -> None:
		i = self.rank[old]
		del self.rank[old]
		self.heap[i] = new
		self.rank[new] = i
		if old < new:
			self.move_down(i)
		else:
			self.move_up(i)
	#
	def __str__(self) -> None:
		print(self.heap)