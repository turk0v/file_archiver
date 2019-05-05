from compress import CompressData
from decompress import DecompressData
import sys

def parse_commands():
	if len(sys.argv) < 2:
		raise Exception("Wrong syntax in args")
	filepath = sys.argv[2]
	flag = sys.argv[1]
	print("file path is {}\n".format(filepath))
	if flag == "-c":
		print("Compressing...\n")

		file_to_compress = CompressData(filepath)
		file_to_compress.compress_file()
	elif flag == "-d":
		print("Decompressig...\n")
		file_to_decompress = DecompressData(filepath)
		file_to_decompress.decode_file()


if __name__ == "__main__" :
	parse_commands()
