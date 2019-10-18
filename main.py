from os import makedirs
from pixel_reader import pixel_reader
# from rgba_handler import rgba_averager, rgba_parser

if __name__ == "__main__":
	# create batch folder
	batch = input("Batch name?")
	makedirs(batch)

	# create rgba arrays + populate batch folder
	image_list_file = pixel_reader(batch)

	# parse rgba arrays + write averages to file
#	rgba_parser(batch, image_list_file)
#	rgba_averager()

