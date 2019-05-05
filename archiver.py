from compress import CompressData
import sys

def parse_commands():
	if len(sys.argv) < 2:
		raise Exception("Wrong syntax in args")
	filepath = sys.argv[2]
	flag = sys.argv[1]
	if flag == "-c":
		print("file path is {}\n".format(filepath))
		print("Compressing...\n")

		file_to_compress = CompressData(filepath)
		file_to_compress.compress_file()
	elif flag == "-d":
		print("file path is {}\n".format(filepath))
		print("Decompressig...\n")
		file_to_decompress = CompressData(filepath)
		file_to_decompress.decode_file()


if __name__ == "__main__" :
	parse_commands()
