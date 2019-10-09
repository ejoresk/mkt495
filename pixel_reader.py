from os import rename
from pathlib import Path as path
from PIL import Image

# maximum or recommended image dimensions by platform
dimensions = {"Facebook": [1200, 630], "Instagram": [1080, 1080], "Twitter": [1024, 512]}

def pixel_reader(batch):
	# open list of image filenames + read by line
	image_list = open(input("Path to image filenames?"), "r").readlines()

	for i in image_list[1:]:
		# standardize image dimensions + create rgba arrays
		dimensions_lookup = dimensions[image_list[0].rstrip()]
		image = Image.open(i.rstrip()).resize(dimensions_lookup, Image.ANTIALIAS)
		pixel_value_array = str(list(image.getdata()))

		# create + write image-wise rgba arrays to files
		image_name = i.rstrip() + ".pixels"
		path(image_name).touch()

		filename = open(image_name, "r+")
		filename.write(pixel_value_array)
		filename.close()

		rename(image_name, batch + "/" + image_name)

