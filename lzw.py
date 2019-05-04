import math

class LZW(object):
	def __init__(self,text_in):
		self.text_in = text_in
		self.code_dict = {}
		self.encoded_text = ""

	def get_next_code(self,number):
		return format(number,"b")


	def make_code_dict(self):
		dict_symb_length = int(math.ceil(math.log(len(self.text_in.split(" ")),2)))
		current_code = 0
		for symbol in self.text_in.split(" "):
			if symbol in self.code_dict.keys():
				pass
			else:
				self.code_dict[symbol] = self.get_next_code(current_code)
				current_code += 1


	def encode_text(self):
		self.make_code_dict()
		print(self.code_dict)
		for symbol in self.text_in.split(" "):
			if symbol in self.code_dict.keys():
				self.encoded_text += self.code_dict[symbol]
		return self.encoded_text




