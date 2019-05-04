import unittest
from huffman import HuffmanCompress

class HuffmanCompressTest(unittest.TestCase):

	def test_freq_dict(self):
		txt = "beep boop beer!"
		proper_res = {'!': 1, ' ': 2, 'b': 3, 'e': 4, 'o': 2, 'p': 2, 'r': 1}
		code = HuffmanCompress(txt)
		self.assertTrue(code.build_freq_dict(),proper_res)

	def test_code_dict(self):
		txt = "beep boop beer!"
		proper_res = {'!': '0110', ' ': '110', 'b': '00', 'e': '10', 'o': '111', 'p': '010', 'r': '0111'}
		code = HuffmanCompress(txt)
		code.build_freq_dict()
		code.make_heap()
		code.merge_nodes()
		self.assertTrue(code.make_codes(),proper_res)

	def test_compress_integr(self):
		txt = "beep boop beer!"
		proper_res = "0010100101100011111101011000101001110110"
		code = HuffmanCompress(txt)
		self.assertTrue(code.compress_data(),proper_res)



if __name__ == "__main__":
	unittest.main()