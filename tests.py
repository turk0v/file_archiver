import unittest
from huffman import HuffmanCompress
from lzw import LZW

class CompressTest(unittest.TestCase):

	def test_huf_freq_dict(self):
		txt = "beep boop beer!"
		proper_res = {'!': 1, ' ': 2, 'b': 3, 'e': 4, 'o': 2, 'p': 2, 'r': 1}
		code = HuffmanCompress(txt)
		self.assertEqual(code.build_freq_dict(),proper_res)

	def test_huf_code_dict(self):
		txt = "beep boop beer!"
		proper_res = {'!': '0110', ' ': '110', 'b': '00', 'e': '10', 'o': '111', 'p': '010', 'r': '0111'}
		code = HuffmanCompress(txt)
		code.build_freq_dict()
		code.make_heap()
		code.merge_nodes()
		self.assertEqual(code.make_codes(),proper_res)

	def test_huf_compress_integr(self):
		txt = "beep boop beer!"
		proper_res = "00 10 10 010 110 00 111 111 010 110 00 10 10 0111 0110 "
		code = HuffmanCompress(txt)
		self.assertEqual(code.compress_data(),proper_res)


	def test_lzw_encode_text(self):
		txt = "beep boop beer!"
		code = LZW(txt)
		self.assertEqual(code.encode_text(),"0110")



if __name__ == "__main__":
	unittest.main()