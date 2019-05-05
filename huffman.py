import heapq
from heap_methods import HeapNode

class HuffmanCompress(object):

	def __init__(self,txt_in):
		self.txt_in = txt_in
		self.freq_dict = {}
		self.codes_dict = {}
		self.heap = []
		self.compressed_txt = ""

	def build_freq_dict(self):
		char_list = list(self.txt_in)
		for char in char_list:
			if char in self.freq_dict.keys():
				self.freq_dict[char] += 1
			else:
				self.freq_dict[char] = 1
		return(self.freq_dict)

	def make_heap(self):
		for key in self.freq_dict:
			node = HeapNode(key,self.freq_dict[key])
			heapq.heappush(self.heap,node)
		return(self.heap)

	def merge_nodes(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)
		return(self.heap)

	def make_code_iter(self,cur_code,node):
		if(node == None):
			return
		if(node.symbol != None):
			self.codes_dict[node.symbol] = cur_code
			# print(self.codes_dict)
		self.make_code_iter(cur_code+"0",node.left)
		self.make_code_iter(cur_code+"1",node.right)

	def make_codes(self):
		cur_code = ""
		start_node = heapq.heappop(self.heap)
		self.make_code_iter(cur_code,start_node)
		return(self.codes_dict)


	def compress_data(self):
		self.build_freq_dict()
		self.make_heap()
		self.merge_nodes()
		self.make_codes()
		for sym in self.txt_in:
			for key in self.codes_dict.keys():
				if (sym == key):
					self.compressed_txt += self.codes_dict[key]+" "

		return(self.compressed_txt)









