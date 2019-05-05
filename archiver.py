from compress import CompressData
import sys

def parse_commands():
	if len(sys.argv) <= 1:
		raise Exception("Wrong syntax in args, you forgot filepath")
	filepath = sys.argv[1]
	print("file path is {}\n".format(filepath))
	print("Compressing...\n")
	file_to_compress = CompressData(filepath)
	file_to_compress.compress_file()
	try:
		if sys.argv[2] == "-d":
			print("Decompressig...\n")
			file_to_compress.decode_file()
		if sys.argv[2] != "-d":
			raise Exception("Wrong flag used")
	except IndexError as e:
		pass




if __name__ == "__main__" :
	parse_commands()
