from huffman import HuffmanCompress
from lzw import LZW
import os

class CompressData(object):
	def __init__(self,file_in_path):
		self.in_path = file_in_path

	def run_encoding_algorithm(self,text):
		"""Run LZW after Huffman"""
		huf_res = HuffmanCompress(text)
		lzw_res = LZW(huf_res.compress_data())
		return (lzw_res.encode_text())



	def add_padding_to_binary(self,text):
		"""Convert encoded text to proper size binary size"""
		encoded_text = text
		extra_zero = 8 - len(encoded_text) % 8
		for i in range(extra_zero):
			encoded_text += "0"
		padded_info = "{0:08b}".format(extra_zero)
		encoded_text = padded_info + encoded_text
		return encoded_text

	def make_byte_array(self,b_text):
		"""Create byte text form converted encoded text"""
		if(len(b_text) % 8 != 0):
			print("bad binary convertion")
			return

		b_array = bytearray()
		for i in range(0,len(b_text),8):
			b_intstance = b_text[i:i+8]
			b_array.append(int(b_intstance,2))
		return b_array

	def print_size_results(self,file1,file2):
		file1_size = os.stat(file1).st_size
		file2_size = os.stat(file2).st_size
		print("Before compression size {}".format(file1_size))
		print("After compression size {}".format(file2_size))
		print("Compression coef is {:.{pres}f}".format((float(file1_size)/file2_size),pres = 4))

	def compress_file(self):
		file_in_name = os.path.splitext(self.in_path)[0]
		file_out_name = file_in_name + ".bin"

		with open(self.in_path,"r+") as file_in, open(file_out_name,"wb") as file_out:
			text_in = file_in.read()
			text_in = text_in.rstrip()
			encoded_text = self.add_padding_to_binary(self.run_encoding_algorithm(text_in))
			res = self.make_byte_array(encoded_text)
			file_out.write(bytes(res))
		self.print_size_results(self.in_path,file_out_name)

