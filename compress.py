from huffman import HuffmanCompress
from lzw import LZW
import os

class CompressData(object):
	def __init__(self,file_in_path):
		self.in_path = file_in_path
		self.lzw_codes = {}
		self.huf_codes = {}
		self.code_intervals = []

	def run_encoding_algorithm(self,text):
		"""Run LZW after Huffman"""
		huf_res = HuffmanCompress(text)
		lzw_res = LZW(huf_res.compress_data())
		res = lzw_res.encode_text()
		self.huf_codes = huf_res.codes_dict
		self.lzw_codes = lzw_res.code_dict
		self.code_intervals = lzw_res.encoded_insert_length
		return res




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

	def remove_padding(self,padded_text):
		padded_info = padded_text[:8]
		extra_padding = int(padded_info,2)
		padded_text = padded_text[8:]
		encoded_text = padded_text[:-1*extra_padding]
		return encoded_text

	def transform_codes_dicts(self):
		"""Concatinate LZW and Huffman dicts"""
		inv_lzw_codes = {v: k for k, v in self.lzw_codes.items()}
		inv_huf_codes = {v: k for k, v in self.huf_codes.items()}
		res_dict = {}
		for key2 in inv_huf_codes:
			if key2 in inv_lzw_codes.values():
				res_dict[self.lzw_codes[key2]] = inv_huf_codes[key2]
		for key in inv_lzw_codes:
			if (inv_lzw_codes[key] == ''):
				res_dict[key] = ''
		return res_dict

	def decode_text(self,encoded_text):
		dec_text = ""
		decode_dict = self.transform_codes_dicts()
		for i in self.code_intervals:
			tmp_smb = encoded_text[:i]
			encoded_text = encoded_text[i:]
			for key in decode_dict.keys():
				if tmp_smb == key:
					dec_text += decode_dict[key]

		return dec_text


	def print_decompression_results(self,file1,file2):
		file1_size = os.stat(file1).st_size
		file2_size = os.stat(file2).st_size
		print("Before decompression size {}".format(file1_size))
		print("After decompression size {}".format(file2_size))

	def decode_file(self):
		file_in_name_tmp = os.path.splitext(self.in_path)[0]
		file_out_name = file_in_name_tmp + "_decomp" + ".txt"
		file_in_name = file_in_name_tmp + ".bin"

		with open(file_in_name,'rb') as file_in,open(file_out_name,'w') as file_out:
			bit_string = ""
			print(file_in_name)
			print(file_out_name)

			byte = file_in.read(1)
			while(byte != b""):
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file_in.read(1)

			encoded_text = self.remove_padding(bit_string)
			dec_text = self.decode_text(encoded_text)

			file_out.write(dec_text)
		self.print_decompression_results(file_in_name,file_out_name)


s = CompressData("numbers.txt")
s.compress_file()
s.decode_file()













