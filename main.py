import os
from pixel_reader import pixel_reader as pr
# from rgba_handler import rgba_averager, rgba_parser as rgbaa, rgbap

if __name__ == "__main__":
	# create batch folder
	batch = input("Batch name?")
	os.makedirs(batch)

	# create rgba arrays + populate batch folder
	pr(batch)

	# parse rgba arrays + write averages to file
#	rgbap()
#	rgbaa()

