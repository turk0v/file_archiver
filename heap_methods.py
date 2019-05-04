
class HeapNode(object):
	
	def __init__(self,symbol,freq):
		self.symbol = symbol
		self.freq = freq
		self.right = None
		self.left = None

	def __repr__(self):
		return "sym:{} -- freq:{} -- left :{} -- right :{}".format(self.symbol,self.freq,self.left,self.right)

	def __cmp__(self, other):
		if(other == None):
			return -1
		if(not isinstance(other, HeapNode)):
			return -1
		return self.freq > other.freq



