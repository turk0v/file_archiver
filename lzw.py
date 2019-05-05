import math

class LZW(object):
	def __init__(self,text_in):
		self.text_in = text_in
		self.code_dict = {}
		self.encoded_text = ""
		self.encoded_insert_length = []

	def get_next_code(self,number):
		dict_symb_length = int(math.ceil(math.log(len(self.text_in.split(" ")),2)))
		# return "{0:0{n}b}".format(number,n = 5)
		return format(number,"b")


	def make_code_dict(self):
		current_code = 1
		for symbol in self.text_in.split(" "):
			if symbol in self.code_dict.keys():
				pass
			else:
				self.code_dict[symbol] = self.get_next_code(current_code)
				current_code += 1


	def encode_text(self):
		self.make_code_dict()
		for symbol in self.text_in.split(" "):
			if symbol in self.code_dict.keys():
				self.encoded_text += self.code_dict[symbol]
				self.encoded_insert_length.append(len(self.code_dict[symbol]))
		return self.encoded_text




