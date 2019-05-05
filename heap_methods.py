
class HeapNode(object):
	
	def __init__(self,symbol,freq):
		self.symbol = symbol
		self.freq = freq
		self.right = None
		self.left = None

	def __repr__(self):
		return "sym:{} -- freq:{} -- left :{} -- right :{}".format(self.symbol,self.freq,self.left,self.right)

	def __lt__(self, other):
	    return self.freq < other.freq

	def __eq__(self, other):
	    if(other == None):
	        return False
	    if(not isinstance(other, HeapNode)):
	        return False
	    return self.freq == other.freq



