from PIL import Image

# maximum or recommended image dimensions by platform
dimensions = {"Facebook": [1200, 630], "Instagram": [1080, 1080], "Twitter": [1024, 512]}

def pixel_reader():
	# open list of image filenames + read by line
	image_list = open(input("Path to image filenames?"), "r")

	for i in image_list[1:]:
		# create image-wise rgba arrays
		image = Image.open(i).resize(dimensions[image_list[0]], Image.ANTIALIAS)
		pixel_value_array = str(list(image.getdata()))
		filename.write(pixel_value_array)

		# create + write image-wise rgba arrays to files
		image_name = i + ".pixels"
		filename = open(image_name, "r+")

